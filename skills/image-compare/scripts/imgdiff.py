#!/usr/bin/env python3
"""Compare two images: changed pixels, SSIM, changed regions, diff picture.
imgdiff.py BEFORE AFTER [--out diff.png] [--tolerance 0] [--fit pad|resize] [--ignore X,Y,W,H ...] [--max-changed 0.5]"""
import argparse, json, sys
import numpy as np
from PIL import Image, ImageDraw, ImageOps
from scipy import ndimage
from skimage.metrics import structural_similarity

def load(path):
    im = ImageOps.exif_transpose(Image.open(path)).convert('RGBA')
    return Image.alpha_composite(Image.new('RGBA', im.size, 'white'), im).convert('RGB')  # transparency -> white

p = argparse.ArgumentParser()
p.add_argument('before'); p.add_argument('after')
p.add_argument('--out', default='diff.png')
p.add_argument('--tolerance', type=int, default=0, help='largest per-channel difference (0-255) still treated as equal')
p.add_argument('--fit', choices=['pad', 'resize'], default='pad', help='what to do when the sizes differ')
p.add_argument('--ignore', nargs='*', default=[], help='rectangles X,Y,W,H to leave out (clock, avatar, ad slot)')
p.add_argument('--max-changed', type=float, help='exit with 1 when more than this percent of pixels changed')
args = p.parse_args()
from pathlib import Path
output = Path(args.out).expanduser().resolve()
inputs = {Path(args.before).expanduser().resolve(), Path(args.after).expanduser().resolve()}
if output in inputs:
    p.error('--out must not overwrite an input image')
if output.exists():
    p.error('--out already exists; choose a new output file')
if not 0 <= args.tolerance <= 255:
    p.error('--tolerance must be between 0 and 255')
if args.max_changed is not None and not 0 <= args.max_changed <= 100:
    p.error('--max-changed must be between 0 and 100')


a, b = load(args.before), load(args.after)
size_a, size_b = a.size, b.size
outside = None
if a.size != b.size and args.fit == 'resize':  # same picture at two scales: bring the larger down to the smaller
    if abs(a.width / a.height - b.width / b.height) > 0.01:
        sys.exit(f'aspect ratios differ ({a.size} vs {b.size}): crop both to the same area, or use --fit pad')
    small = min(a.size, b.size)
    a, b = (im if im.size == small else im.resize(small, Image.Resampling.LANCZOS) for im in (a, b))
elif a.size != b.size:  # same scale, different extent: anchor top-left, count the uncovered strip as changed
    w, h = max(a.width, b.width), max(a.height, b.height)
    outside = np.ones((h, w), bool)
    outside[:min(a.height, b.height), :min(a.width, b.width)] = False
    padded = [Image.new('RGB', (w, h), 'white'), Image.new('RGB', (w, h), 'white')]
    padded[0].paste(a, (0, 0)); padded[1].paste(b, (0, 0))
    a, b = padded

x, y = np.asarray(a).astype(np.int16), np.asarray(b).astype(np.int16)
for box in args.ignore:
    bx, by, bw, bh = (int(v) for v in box.split(','))
    x[by:by + bh, bx:bx + bw] = y[by:by + bh, bx:bx + bw] = 127
delta = np.abs(x - y).max(axis=2)
changed = delta > args.tolerance
if outside is not None:
    changed |= outside
for box in args.ignore:
    bx, by, bw, bh = (int(v) for v in box.split(','))
    if bx < 0 or by < 0 or bw < 0 or bh < 0:
        p.error('--ignore coordinates and sizes must be non-negative')
    changed[by:by + bh, bx:bx + bw] = False
ssim = None
if min(a.size) >= 7:  # the default SSIM window is 7x7
    ssim = round(float(structural_similarity(x.astype(np.uint8), y.astype(np.uint8), channel_axis=2, data_range=255)), 4)

# Grow every changed pixel by 8 px, so changes up to 16 px apart join: one word or one button is one region.
labels, _ = ndimage.label(ndimage.binary_dilation(changed, iterations=8))
regions = []
for i, sl in enumerate(ndimage.find_objects(labels), start=1):
    ys, xs = np.nonzero(changed[sl] & (labels[sl] == i))
    left, top = sl[1].start + int(xs.min()), sl[0].start + int(ys.min())
    regions.append({'box': [left, top, int(xs.max() - xs.min()) + 1, int(ys.max() - ys.min()) + 1], 'changed_pixels': len(ys)})
regions.sort(key=lambda r: -r['changed_pixels'])

faded = (np.asarray(a.convert('L')).astype(np.float32) * 0.25 + 191).astype(np.uint8)
picture = np.stack([faded] * 3, axis=2)
picture[changed] = (220, 0, 60)
out = Image.fromarray(picture)
draw = ImageDraw.Draw(out)
for r in regions[:20]:
    left, top, w, h = r['box']
    draw.rectangle([left - 4, top - 4, left + w + 3, top + h + 3], outline=(0, 90, 200), width=2)
with output.open("xb") as output_stream:
    out.save(output_stream, format="PNG")

percent = 100 * changed.mean()
print(json.dumps({
    'before': list(size_a), 'after': list(size_b), 'compared_at': list(a.size),
    'fit': None if size_a == size_b else args.fit, 'tolerance': args.tolerance,
    'identical': bool(delta.max() == 0 and outside is None),
    'changed_pixels': int(changed.sum()), 'changed_percent': round(percent, 3),
    'largest_channel_difference': int(delta.max()), 'ssim': ssim,
    'regions': regions[:20], 'regions_total': len(regions), 'diff_image': args.out}, indent=2))
sys.exit(1 if args.max_changed is not None and percent > args.max_changed else 0)