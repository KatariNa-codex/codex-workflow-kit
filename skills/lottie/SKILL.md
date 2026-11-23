---
name: lottie
description: Create and inspect Lottie JSON and animated TGS files with Python in a fresh task folder. Use for animation geometry, loops and TGS export.
---

# Lottie and animated TGS

For new work, start in a fresh task folder. Import lot from scripts/lot.py. Use Comp, layer, insert and save to write the Lottie JSON and compressed TGS. Comp.save refuses an existing output and checks basic TGS constraints. Use scripts/unpack.py to inspect a copy of an existing TGS. Python provides the core runtime. Pillow and NumPy are needed only for the optional image comparison helpers. Review a rendered preview separately before handing off animation artwork.
