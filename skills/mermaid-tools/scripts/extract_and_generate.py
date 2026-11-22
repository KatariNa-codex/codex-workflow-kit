#!/usr/bin/env python3
"""Portable no-clobber Mermaid extraction and PNG rendering with existing CLI."""
import argparse,pathlib,shutil,subprocess,sys,struct,zlib
from extract_diagrams import extract_mermaid_diagrams

def discover_renderer():
    executable=shutil.which('mmdc')
    if not executable:raise RuntimeError('Existing mmdc is unavailable; separate setup is required')
    path=pathlib.Path(executable)
    if path.suffix.lower() in ('.cmd','.bat','.ps1'):
        node=shutil.which('node')
        cli=path.parent/'node_modules/@mermaid-js/mermaid-cli/src/cli.js'
        if not node or not cli.is_file():raise RuntimeError('mmdc shim requires an existing node and adjacent Mermaid CLI; no shell fallback')
        return [node,str(cli.resolve())]
    return [str(path)]

def validate_png(path):
    """Check PNG chunks, CRC, dimensions and bounded decompression; not visual QA."""
    path=pathlib.Path(path)
    if not path.is_file() or path.stat().st_size>32*1024*1024:raise ValueError('Missing or oversized PNG')
    data=path.read_bytes()
    if data[:8]!=b'\x89PNG\r\n\x1a\n':raise ValueError('Invalid PNG signature')
    pos=8;dimensions=None;compressed=[];ended=False
    while pos+12<=len(data):
        size=struct.unpack('>I',data[pos:pos+4])[0];kind=data[pos+4:pos+8];end=pos+8+size
        if end+4>len(data):raise ValueError('Truncated PNG chunk')
        payload=data[pos+8:end];crc=struct.unpack('>I',data[end:end+4])[0]
        if zlib.crc32(kind+payload)&0xffffffff!=crc:raise ValueError('PNG CRC mismatch')
        if dimensions is None:
            if kind!=b'IHDR' or size!=13:raise ValueError('PNG missing IHDR')
            w,h=struct.unpack('>II',payload[:8]);dimensions=(w,h)
            if not 0<w<=20000 or not 0<h<=20000 or w*h>25_000_000:raise ValueError('PNG dimensions exceed bounds')
            depth,color,compression,filter_method,interlace=payload[8:]
            channels={0:1,2:3,3:1,4:2,6:4}.get(color)
            valid_depths={0:{1,2,4,8,16},2:{8,16},3:{1,2,4,8},4:{8,16},6:{8,16}}
            if channels is None or depth not in valid_depths[color] or compression or filter_method or interlace:
                raise ValueError('Unsupported PNG header (interlaced images require separate validation)')
            row_bytes=(w*channels*depth+7)//8
            expected=(row_bytes+1)*h
            if expected>128*1024*1024:raise ValueError('PNG decoded size exceeds bounds')
        if kind==b'IDAT':compressed.append(payload)
        if kind==b'IEND':
            if size!=0 or end+4!=len(data):raise ValueError('Invalid PNG end')
            ended=True;break
        pos=end+4
    if not ended or not compressed:raise ValueError('PNG missing image data/end')
    stream=zlib.decompressobj();raw=stream.decompress(b''.join(compressed),expected+1)
    if not stream.eof or stream.unused_data or stream.unconsumed_tail or not raw:raise ValueError('Invalid or oversized compressed PNG data')
    if len(raw)!=expected or any(raw[i]>4 for i in range(0,len(raw),row_bytes+1)):raise ValueError('PNG scanline size/filter is invalid')
    return dimensions

def generate(source,output):
    command=discover_renderer() # Fail without output side effects if dependencies unavailable.
    files=extract_mermaid_diagrams(source,output)
    if not files:raise ValueError('No Mermaid diagrams extracted')
    created=[]
    for item in files:
        png=pathlib.Path(item).with_suffix('.png')
        # Reserve each output exclusively, so mmdc cannot replace an older user's file.
        with png.open('xb'):pass
        result=subprocess.run(command+['-i',str(item),'-o',str(png)],capture_output=True,text=True,encoding='utf-8',errors='replace',shell=False)
        if result.returncode:raise RuntimeError('mmdc failed with exit code '+str(result.returncode))
        validate_png(png);created.append(str(png))
    return created

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('source');parser.add_argument('output');args=parser.parse_args()
    try:files=generate(args.source,args.output)
    except (OSError,ValueError,RuntimeError) as exc:print('Rendering failed: '+str(exc),file=sys.stderr);return 1
    print(f'Generated {len(files)} PNG files; structural validation passed (visual review still required).');return 0
if __name__=='__main__':sys.exit(main())
