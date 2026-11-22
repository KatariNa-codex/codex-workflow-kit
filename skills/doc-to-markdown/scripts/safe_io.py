"""No-clobber local output helpers; no implicit overwrite option."""
from pathlib import Path
import stat

def checked_path(path):
    path=Path(path).absolute()
    for item in (path,*path.parents):
        if item.is_symlink() or (item.exists() and getattr(item.lstat(),'st_file_attributes',0)&1024):
            raise ValueError('Output links/junctions are not supported')
    return path.resolve()

def require_new(path):
    path=checked_path(path)
    if path.exists():raise FileExistsError('Choose a fresh output: '+str(path))
    return path

def preflight(source,output,assets=None):
    source=Path(source).resolve();output=require_new(output)
    if output==source:raise ValueError('Input and output must differ')
    if assets is not None:
        assets=require_new(assets)
        if source==assets or source.is_relative_to(assets) or output==assets or output.is_relative_to(assets):
            raise ValueError('Assets must be separate from input and markdown output')

def fresh_dir(path):
    path=require_new(path);path.mkdir(parents=True,exist_ok=False);return path

def write_new(path,text):
    path=require_new(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('x',encoding='utf-8',newline='\n') as f:f.write(text)

def child_path(root,name):
    root=Path(root).resolve();dest=(root/name).resolve()
    if not dest.is_relative_to(root) or dest==root:raise ValueError('Asset path escapes output directory')
    return dest
