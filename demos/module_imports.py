"""Module Imports Demonstration - Python 2 vs Python 3.

Python 3 reorganized and renamed several standard-library modules.
This demo shows the Python 3 equivalents of common Python 2 imports.

    Python 2 module               Python 3 module
    ─────────────────────────────────────────────────────────────
    StringIO                  ->  io
    StringIO.StringIO()       ->  io.StringIO()
    urllib2                   ->  urllib.request + urllib.error
    urllib2.Request           ->  urllib.request.Request
    urllib2.URLError          ->  urllib.error.URLError
    ConfigParser              ->  configparser
    ConfigParser.SafeConfigParser -> configparser.ConfigParser
    ─────────────────────────────────────────────────────────────

    Implicit relative imports (Python 2):
        import sibling          # looks in current package first
    Explicit relative imports (Python 3):
        from . import sibling   # required for intra-package imports

Python 2 allowed implicit relative imports: ``import foo`` inside a package
would first search the package directory. Python 3 requires explicit relative
imports (``from . import foo``) or absolute imports (``from package import foo``).
"""

from io import StringIO
from urllib.request import Request
from urllib.error import URLError
import configparser
from . import integer_division


def run():
    """Demonstrate Python 3 module renames and explicit relative imports."""

    print("=== Python 3 Module & Import Features Demo ===")
    print("")

    # --- io.StringIO (was StringIO.StringIO) ---
    print("--- io.StringIO (was StringIO.StringIO) ---")
    buf = StringIO()
    buf.write("Hello from io.StringIO!")
    print("from io import StringIO; StringIO() write and getvalue():")
    print("  buf.getvalue() =", buf.getvalue())
    buf.close()
    print("")

    # --- urllib.request and urllib.error (was urllib2) ---
    print("--- urllib.request / urllib.error (was urllib2) ---")
    print("from urllib.request import Request")
    print("from urllib.error import URLError")
    print("  Request class:", Request)
    print("  URLError class:", URLError)
    print("")

    # --- configparser (was ConfigParser) ---
    print("--- configparser (was ConfigParser) ---")
    config = configparser.ConfigParser()
    config.add_section("database")
    config.set("database", "host", "localhost")
    config.set("database", "port", "5432")
    print("configparser.ConfigParser() usage:")
    print("  config.get('database', 'host') =", config.get("database", "host"))
    print("  config.get('database', 'port') =", config.get("database", "port"))
    # Note: Python 2's ConfigParser.SafeConfigParser is now just
    # configparser.ConfigParser in Python 3 (SafeConfigParser was removed in 3.12).
    print("")

    # --- Explicit relative imports (was implicit relative) ---
    print("--- Explicit relative imports (was implicit relative) ---")
    print("In Python 2, 'import foo' inside a package first looks in the")
    print("package directory (implicit relative import).")
    print("In Python 3, you must use 'from . import foo' (explicit relative)")
    print("or 'from package import foo' (absolute import).")
    print("")
    print("Example: inside demos/ package, we use explicit relative import:")
    print("  'from . import integer_division'")
    print("  Module found:", integer_division.__name__)
