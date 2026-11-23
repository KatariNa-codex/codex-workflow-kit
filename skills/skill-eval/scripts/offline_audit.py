#!/usr/bin/env python3
"""Offline static audit entrypoint. Does not import or execute target files."""
import argparse,hashlib,json,os,pathlib,stat,sys
sys.dont_write_bytecode=True
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
from skill_eval.audit.structure_check import check_structure
from skill_eval.audit.security_scan import scan_security,scan_coverage
from skill_eval.audit.permission_analyzer import analyze_permissions
from skill_eval.schemas import calculate_score,calculate_grade

def audit(target):
 root=pathlib.Path(target).absolute()
 if not root.is_dir(): raise ValueError('Target must be a directory')
 count=0
 for base,dirs,files in os.walk(root,followlinks=False):
  for name in dirs+files:
   p=pathlib.Path(base)/name
   if p.is_symlink() or bool(getattr(p.lstat(),'st_file_attributes',0)&getattr(stat,'FILE_ATTRIBUTE_REPARSE_POINT',1024)):
    raise ValueError('Links/junctions are not supported')
   count+=1
   if count>10000: raise ValueError('Target exceeds 10000 entries')
 if root.is_symlink() or bool(getattr(root.lstat(),'st_file_attributes',0)&1024): raise ValueError('Target link refused')
 findings,fm,_=check_structure(root)
 findings+=scan_security(root,include_all=True)+analyze_permissions(root,frontmatter=fm)
 score=calculate_score(findings)
 return {'coverage':scan_coverage(root),'kind':'static-audit-only','score':score,'grade':calculate_grade(score),'safety_proven':False,'functional':'unknown','trigger':'unknown','findings':[f.to_dict() for f in findings]}

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('target');p.add_argument('--output',required=True);a=p.parse_args()
 out=pathlib.Path(a.output)
 if out.exists(): p.error('Output exists; choose a fresh path')
 result=audit(a.target)
 out.parent.mkdir(parents=True,exist_ok=True)
 with out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2)
 print('Static audit written; safety is not proven')
if __name__=='__main__':main()
