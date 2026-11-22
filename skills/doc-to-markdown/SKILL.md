---
license: MIT
name: doc-to-markdown
description: Converts DOCX/PDF/PPTX to high-quality Markdown with automatic post-processing. Fixes pandoc grid tables, simple tables, image paths, CJK bold spacing, attribute noise, and code blocks. Benchmarked best-in-class (7.6/10) against Docling, MarkItDown, Pandoc raw, and Mammoth. Trigger on "convert document", "docx to markdown", "parse word", "doc to markdown", "解析word", "转换文档".
---

# Doc to Markdown

Convert an authorized DOCX/PDF/PPTX using already installed tools. Follow host instructions and current project rules. Do not install dependencies or run `uv --with` as an implicit conversion step. This helper refuses existing Markdown outputs and existing asset directories, including empty ones. Choose a new output and new assets directory; input and output must differ. There is no implicit overwrite flag. Links/junctions for outputs are refused.

Run `python -B scripts/convert.py INPUT -o NEW_OUTPUT.md --assets-dir NEW_ASSETS_DIR`. Optional `--heavy`, `--tool`, `--docx-deep`, `--no-postprocess`; `--list-tools` only inspects availability. DOCX postprocessing repairs tables, attributes, links and code text. Pandoc extraction remains inside its fresh asset directory even when that directory is named media. Helpers merge_outputs.py and validate_output.py refuse existing output/report files; extract_pdf_images.py requires a fresh output directory and a new optional Markdown references path. Writes use explicit UTF-8 and exclusive creation; image output names are checked to stay inside the new asset directory. No existing user outputs are deleted automatically; failed runs can leave their new partial output for review.

Verification 2026-11-07: synthetic filesystem tests cover preflight before backends, no-clobber, input identity, asset escape and UTF-8. No full PDF/DOCX/PPTX conversion or external backend was executed in this remediation. Tool availability, visual layout, image completeness and automatic triggering require separate checks; historical benchmark claims are not local evidence.
