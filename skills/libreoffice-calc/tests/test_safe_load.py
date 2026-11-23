"""Safety regression: real UNO constants, intercepted document loader; no app startup."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import uno
from uno_bridge import safe_load
from exceptions import UnoBridgeError


class DesktopSpy:
    def __init__(self):
        self.calls = []

    def loadComponentFromURL(self, url, target, flags, props):
        self.calls.append((url, target, flags, props))
        return "intercepted-document"


def prop(name, value):
    result = uno.createUnoStruct("com.sun.star.beans.PropertyValue")
    result.Name, result.Value = name, value
    return result


class SafeLoadTests(unittest.TestCase):
    def test_security_overrides_and_other_properties(self):
        for url in ("file:///C:/temporary/test.xls", "private:factory/scalc"):
            desktop = DesktopSpy()
            result = safe_load(desktop, url, "_blank", 0, (
                prop("MacroExecutionMode", 4), prop("MacroExecutionMode", 2),
                prop("UpdateDocMode", 3), prop("Hidden", False),
                prop("ReadOnly", True),
            ))
            self.assertEqual(result, "intercepted-document")
            props = desktop.calls[0][3]
            values = {p.Name: p.Value for p in props}
            self.assertEqual(values["MacroExecutionMode"], 0)
            self.assertEqual(values["UpdateDocMode"], 0)
            self.assertIs(values["Hidden"], True)
            self.assertIs(values["ReadOnly"], True)
            self.assertEqual(sum(p.Name == "MacroExecutionMode" for p in props), 1)

    def test_rejects_remote_document_before_loader(self):
        for url in ("https://example.com/book.xls", "smb://server/book.xls"):
            desktop = DesktopSpy()
            with self.assertRaises(UnoBridgeError):
                safe_load(desktop, url, "_blank", 0, ())
            self.assertEqual(desktop.calls, [])


if __name__ == "__main__":
    unittest.main()
