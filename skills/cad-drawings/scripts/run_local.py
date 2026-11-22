from pathlib import Path
import json,os,sys,subprocess
root=Path(__file__).resolve().parent
config=json.loads((root/'local-runtime.json').read_text(encoding='utf-8'))
configured_python=config.get('python')
if not configured_python:raise SystemExit('Set an absolute path to the verified isolated Python in scripts/local-runtime.json.')
python=Path(configured_python)
if not python.is_absolute():raise SystemExit('The configured Python path must be absolute.')
if not python.is_file():raise SystemExit('Verified runtime missing; do not fall back silently: '+str(python))
oda=config.get('oda')
if oda:
 if not Path(oda).is_file():raise SystemExit('Configured ODA converter missing: '+oda)
 os.environ['CAD_DRAWINGS_ODA']=oda
args=sys.argv[1:]
entry=config.get('entry')
if not entry:
 if not args or args[0] not in config['offline_helpers']:raise SystemExit('Choose tested helper: '+', '.join(config['offline_helpers']))
 entry=args.pop(0)+'.py'
target=root/entry
raise SystemExit(subprocess.call([str(python),'-B',str(target),*args]))
