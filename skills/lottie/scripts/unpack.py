"""Unpack trusted local fixtures into a fresh current work folder; no overwrites."""
import gzip, json, pathlib, shutil, sys
def main(files):
    plans=[]
    for name in files:
        src=pathlib.Path(name);raw=src.read_bytes()
        if len(raw)>10_000_000:raise ValueError('input too large')
        if raw[:2]==b'\x1f\x8b':
            import io
            with gzip.GzipFile(fileobj=io.BytesIO(raw)) as f:raw=f.read(10_000_001)
        if len(raw)>10_000_000:raise ValueError('expanded input too large')
        data=json.loads(raw);target=pathlib.Path('tgs')/(src.stem+'.json')
        if target.exists() or target in [x[0] for x in plans]:raise FileExistsError(str(target))
        plans.append((target,data))
    viewer=pathlib.Path('sheet.html')
    if viewer.exists():raise FileExistsError(str(viewer))
    for folder in ['tgs','out','sheets','iso']:pathlib.Path(folder).mkdir(exist_ok=True)
    for target,data in plans:
        with target.open('x',encoding='utf-8') as f:json.dump(data,f,ensure_ascii=False)
    with viewer.open('x',encoding='utf-8') as f:f.write(pathlib.Path(__file__).with_name('sheet.html').read_text(encoding='utf-8'))
if __name__=='__main__':main(sys.argv[1:])
