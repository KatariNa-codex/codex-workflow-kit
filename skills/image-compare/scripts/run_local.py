from pathlib import Path
import json,subprocess,sys
root=Path(__file__).resolve().parent
config=json.loads((root/'local-runtime.json').read_text(encoding='utf-8'))
configured=config.get('python')
if not configured:raise SystemExit('Set the absolute Python path in scripts/local-runtime.json.')
python=Path(configured)
if not python.is_absolute():raise SystemExit('The Python path must be absolute.')
if not python.is_file():raise SystemExit('Verified runtime missing; do not fall back silently: '+str(python))
args=sys.argv[1:]
entry=config.get('entry')
if not entry:
 if not args or args[0] not in config['offline_helpers']:raise SystemExit('Choose tested helper: '+', '.join(config['offline_helpers']))
 entry=args.pop(0)+'.py'
target=root/entry
raise SystemExit(subprocess.call([str(python),'-B',str(target),*args]))
