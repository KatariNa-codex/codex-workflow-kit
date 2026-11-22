#!/usr/bin/env python3
"""Local independent offline Codex export evidence reader (not upstream code)."""
import argparse,hashlib,json,pathlib,re
MAX_BYTES=32*1024*1024
MAX_LINE_BYTES=2*1024*1024
MAX_DEPTH=64
MAX_LINES=20000

def result_status(value):
 if isinstance(value,list):
  statuses=[result_status(x.get('text',x.get('content'))) if isinstance(x,dict) and x.get('type') in ('input_text','text','output_text') else 'unknown' for x in value]
  return statuses[0] if statuses and all(x==statuses[0] for x in statuses) else 'unknown'

 if isinstance(value,str):
  try:value=json.loads(value)
  except ValueError:
   codes=set(re.findall(r'(?mi)^Process exited with code (-?\d+)\s*$',value))
   return ('success' if int(next(iter(codes)))==0 else 'failed') if len(codes)==1 else 'unknown'
 if not isinstance(value,dict):return 'unknown'
 if value.get('isError') is True or value.get('is_error') is True or value.get('error'):return 'failed'
 if 'content' in value and 'exit_code' not in value:return result_status(value['content'])
 code=value.get('exit_code')
 if isinstance(code,int) and not isinstance(code,bool):return 'success' if code==0 else 'failed'
 return 'unknown'

def evaluate(text):
 if len(text.encode('utf-8'))>MAX_BYTES:raise ValueError('Input exceeds 32 MiB')
 return evaluate_lines(text.splitlines())

def check_depth(value, depth=0):
 if depth>MAX_DEPTH:raise ValueError('JSON nesting limit exceeded')
 if isinstance(value,dict):
  for v in value.values():check_depth(v,depth+1)
 elif isinstance(value,list):
  for v in value:check_depth(v,depth+1)

def evaluate_lines(lines):
 """Bounded streaming API; source line numbers remain original (1 based)."""
 calls={};results={};claims=[];unrecognized=[];total_bytes=0
 for n,line in enumerate(lines,1):
  total_bytes+=len(line.encode("utf-8"))
  if total_bytes>MAX_BYTES:raise ValueError("Input exceeds 32 MiB")
  if n>MAX_LINES:raise ValueError("Too many events")
  if len(line.encode("utf-8"))>MAX_LINE_BYTES:raise ValueError("Line exceeds 2 MiB")
  if not line.strip():continue
  try:event=json.loads(line)
  except (ValueError,RecursionError):raise ValueError(f'Malformed or deeply nested JSON at line {n}') from None
  check_depth(event)
  if not isinstance(event,dict):raise ValueError(f'Event must be object at line {n}')
  kind=event.get('type');p=event.get('payload')
  if kind not in ('response_item','event_msg') or not isinstance(p,dict):unrecognized.append(n);continue
  typ=p.get('type');cid=p.get('call_id');source={'line':n,'event_type':kind,'payload_type':typ}
  if kind=='response_item' and typ in ('function_call','custom_tool_call'):
   if not isinstance(cid,str) or not cid:raise ValueError(f'Missing call_id at line {n}')
   args=p.get('arguments',p.get('input',{}))
   if isinstance(args,str):
    try:args=json.loads(args)
    except ValueError:pass
   # Preserve command metadata only as untrusted data; never execute it.
   command=args.get('cmd',args.get('command')) if isinstance(args,dict) else None
   fingerprint=hashlib.sha256(json.dumps(args,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
   if cid in calls and (calls[cid]['name']!=p.get('name') or calls[cid]['arguments_sha256']!=fingerprint):raise ValueError('Conflicting duplicate call_id')
   calls[cid]={'name':p.get('name'),'arguments_sha256':fingerprint,'source':source}
  elif kind=='response_item' and typ in ('function_call_output','custom_tool_call_output'):
   if not isinstance(cid,str) or not cid:raise ValueError(f'Missing result call_id at line {n}')
   results.setdefault(cid,[]).append({'status':('unknown' if calls.get(cid,{}).get('name') in ('functions.exec','exec') else result_status(p.get('output'))),'source':source,'priority':2})
  elif kind=='event_msg' and typ=='item_completed' and isinstance(p.get('item'),dict) and p['item'].get('type')=='CommandExecution':
   item=p['item'];cid=item.get('id')
   if not isinstance(cid,str) or not cid:unrecognized.append(n);continue
   command=item.get('command')
   fingerprint=hashlib.sha256(json.dumps(command,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
   if cid in calls and calls[cid]['arguments_sha256']!=fingerprint:raise ValueError('Conflicting command id')
   calls.setdefault(cid,{'name':'CommandExecution','arguments_sha256':fingerprint,'source':source})
   status=result_status(item) if item.get('status') in ('completed','Completed','failed','Failed') else 'unknown'
   results.setdefault(cid,[]).append({'status':status,'source':source,'priority':1})
  elif kind=='event_msg' and typ in ('exec_command_end','command_execution_end'):
   if not isinstance(cid,str) or not cid:unrecognized.append(n);continue
   results.setdefault(cid,[]).append({'status':result_status(p),'source':source,'priority':1})
  elif (kind=='response_item' and typ=='message' and p.get('role')=='assistant') or (kind=='event_msg' and typ=='agent_message'):
   claims.append(source)
  else:unrecognized.append(n)
 actions=[]
 for cid,call in calls.items():
  evidence=results.get(cid,[])
  known={e['status'] for e in evidence if e['status']!='unknown'}
  status=known.pop() if len(known)==1 and call['name'] not in ('functions.exec','exec') else 'unknown'
  actions.append({'call_id':cid,**call,'status':status,'result_sources':[e['source'] for e in evidence],'conflict':len({e['status'] for e in evidence if e['status']!='unknown'})>1})
 statuses=[a['status'] for a in actions]
 overall='failed' if 'failed' in statuses else 'success' if statuses and all(x=='success' for x in statuses) and not unrecognized and not any(cid not in calls for cid in results) else 'unknown'
 return {'kind':'tool-execution-evidence-only','overall':overall,'task_correctness':'unknown','score':None,'remote_judge':False,'actions':actions,'assistant_claim_sources':claims,'unsupported_event_lines':unrecognized,'orphan_result_ids':[cid for cid in results if cid not in calls],'artifacts':'unknown: inspect separately; exit 0 does not prove file correctness','trace_truthfulness':'not independently established'}

def evaluate_file(path, max_source_lines=None):
 """Read an explicitly authorized export only; never copy source/private bodies."""
 path=pathlib.Path(path)
 if not path.is_file() or path.is_symlink():raise ValueError('Regular export required')
 if path.stat().st_size>MAX_BYTES:raise ValueError('Input exceeds 32 MiB')
 digest=hashlib.sha256();counts={'bytes':0,'lines':0}
 def lines():
  with path.open('rb') as handle:
   while max_source_lines is None or counts['lines']<max_source_lines:
    raw=handle.readline(MAX_LINE_BYTES+1)
    if not raw:break
    if len(raw)>MAX_LINE_BYTES:raise ValueError('Line exceeds 2 MiB')
    counts['bytes']+=len(raw);counts['lines']+=1
    if counts['bytes']>MAX_BYTES:raise ValueError('Input exceeds 32 MiB')
    digest.update(raw)
    yield raw.decode('utf-8-sig' if counts['lines']==1 else 'utf-8')
 result=evaluate_lines(lines())
 result['source']={'sha256':digest.hexdigest(),**counts}
 return result


def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('trace',help='Explicitly authorized export only');p.add_argument('--output',required=True);a=p.parse_args()
 src=pathlib.Path(a.trace);out=pathlib.Path(a.output)
 if src.is_symlink() or not src.is_file():p.error('Trace must be a regular explicit export')
 if src.stat().st_size>MAX_BYTES:p.error('Input exceeds 32 MiB')
 if out.exists():p.error('Output exists; choose a fresh path')
 result=evaluate_file(src)
 result['source']['path']=str(src.resolve())
 out.parent.mkdir(parents=True,exist_ok=True)
 with out.open('x',encoding='utf-8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
 print('Offline evidence report written; task correctness remains unknown')
if __name__=='__main__':main()
