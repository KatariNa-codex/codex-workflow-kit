---
license: MIT
name: mermaid-tools
description: Extracts Mermaid diagrams from markdown files and generates high-quality PNG images using bundled scripts. Activates when working with Mermaid diagrams, converting diagrams to PNG, extracting diagrams from markdown, or processing markdown files with embedded Mermaid code.
---

# Mermaid Tools

Extract Mermaid fenced blocks from an authorized Markdown input and render PNG files using existing Mermaid CLI. Follow host and project rules. Use the portable Python entry on Windows or Unix:

`python -B scripts/extract_and_generate.py INPUT.md NEW_OUTPUT_DIRECTORY`

The output directory must not exist, including empty directories. Existing inputs and outputs are preserved. Only files returned by this extraction are rendered; unrelated .mmd files are never globbed. Extraction uses exclusive writes. Failure may leave new partial output, which is not deleted automatically. No dependency installation, npm download, Chrome installation or browser setup is performed.

Renderer discovery uses shutil.which('mmdc'). A Windows .cmd/.bat/.ps1 shim is never executed through a shell: the helper requires existing node and adjacent node_modules/@mermaid-js/mermaid-cli/src/cli.js and calls them directly. Otherwise it fails clearly. Existing Mermaid CLI/Puppeteer/browser dependencies must already work. The older extract-and-generate.sh entry is deprecated and exits 2 with the Python entry instruction; its unsafe glob/Unix rendering path was removed. Additional old shell flags are no longer accepted by that entry.

Rendering failures, missing or malformed PNG files return nonzero and never print full success. PNG validation checks signature, dimensions, chunks, CRC, bounded zlib decoding and IEND; it does not inspect text readability, layout or meaning and is not full visual QA. Review the resulting diagrams visually before delivery.

Verification 2026-11-07: synthetic files and mocked subprocess renderer cover success, renderer nonzero, invalid/truncated PNG, unrelated-file preservation, fresh-directory refusal and Windows node routing. No real mmdc/node/browser execution or automatic trigger benchmark was performed. No claim of full visual rendering validation is made.
