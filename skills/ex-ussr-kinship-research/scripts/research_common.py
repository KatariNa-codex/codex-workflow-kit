"""UTF-8 CLI helper retained from the upstream common module."""
import sys


def configure_utf8_stdio():
    """Keep CLI output readable when an agent captures a legacy-encoded pipe."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            reconfigure(encoding="utf-8")
