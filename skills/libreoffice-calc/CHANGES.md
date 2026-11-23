# Changes

[Upstream revision](https://github.com/dfk1352/LibreOffice-skills/tree/39ea28a197188f220dc504ff1c1d3f8ea1543f91/skills/libreoffice-calc). The original MIT license and author notice are included.

Uses the recipient’s LibreOffice Python with UNO, starts a separate headless instance and applies the Windows process compatibility fixes. Files load with macros and external refresh disabled. Network document paths are rejected.

The release fixes numeric writes in the Python 3.8 bundled with LibreOffice by removing a runtime-only dependency on Python 3.10 union syntax.
