"""Module Imports Demonstration - Python 2 module and import features."""


def run():
    """Demonstrate Python 2 module and import features."""

    print "=== Python 2 Module & Import Features Demo ==="
    print ""

    # Importing from StringIO module
    print "--- StringIO module ---"
    import StringIO
    buf = StringIO.StringIO()
    buf.write("Hello from StringIO!")
    print "StringIO.StringIO() write and getvalue():"
    print "  buf.getvalue() =", buf.getvalue()
    buf.close()
    print ""

    # Importing from urllib2 module
    print "--- urllib2 module ---"
    import urllib2
    print "urllib2 module available:", urllib2 is not None
    print "  urllib2.Request class:", urllib2.Request
    print "  urllib2.URLError class:", urllib2.URLError
    print ""

    # Importing from ConfigParser module
    print "--- ConfigParser module ---"
    import ConfigParser
    config = ConfigParser.SafeConfigParser()
    config.add_section("database")
    config.set("database", "host", "localhost")
    config.set("database", "port", "5432")
    print "ConfigParser.SafeConfigParser() usage:"
    print "  config.get('database', 'host') =", config.get("database", "host")
    print "  config.get('database', 'port') =", config.get("database", "port")
    print ""

    # Implicit relative imports
    print "--- Implicit relative imports ---"
    print "In Python 2, 'import foo' inside a package first looks in the"
    print "package directory (implicit relative import)."
    print ""
    print "Example: inside demos/ package, we can do implicit relative import:"
    # Demonstrate by importing a sibling module implicitly
    # In Python 2, this looks in the current package first
    import integer_division
    print "  'import integer_division' works (implicit relative import)"
    print "  Module found:", integer_division.__name__
