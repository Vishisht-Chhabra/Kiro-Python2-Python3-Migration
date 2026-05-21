"""String Formatting Demonstration - Python 2 percent-style formatting."""

import string


def run():
    """Demonstrate Python 2 percent-style string formatting."""

    print "=== Python 2 String Formatting Demo ==="
    print ""

    # Basic format specifiers: %s, %d, %f
    print "--- Basic format specifiers (%s, %d, %f) ---"
    name = "Alice"
    age = 30
    height = 5.6
    print "String: 'Hello, %s!' => " + ("Hello, %s!" % name)
    print "Integer: '%s is %d years old' => " + ("%s is %d years old" % (name, age))
    print "Float: 'Height: %f meters' => " + ("Height: %f meters" % height)
    print "Float precision: 'Height: %.1f meters' => " + ("Height: %.1f meters" % height)
    print ""

    # Named placeholders with dictionary
    print "--- Named placeholders with dictionary ---"
    data = {"name": "Bob", "city": "Seattle", "temp": 72}
    result = "%(name)s lives in %(city)s where it is %(temp)d degrees" % data
    print "Template: '%(name)s lives in %(city)s where it is %(temp)d degrees'"
    print "Data: %s" % repr(data)
    print "Result: %s" % result
    print ""

    # Multiple positional arguments with tuple
    print "--- Multiple positional arguments with tuple ---"
    values = ("Python", 2, 7, "legacy")
    result = "%s version %d.%d is %s" % values
    print "Template: '%s version %d.%d is %s'"
    print "Tuple: %s" % repr(values)
    print "Result: %s" % result
    print ""

    # Padding and alignment
    print "--- Padding and alignment ---"
    print "Right-aligned: '%10s'" % "hello"
    print "Left-aligned: '%-10s'" % "hello"
    print "Zero-padded: '%05d'" % 42
    print ""

    # string.Template class usage
    print "--- string.Template class ---"
    tmpl = string.Template("$who likes $what")
    result = tmpl.substitute(who="Alice", what="Python")
    print "Template: '$who likes $what'"
    print "substitute(who='Alice', what='Python') => %s" % result
    print ""

    # safe_substitute doesn't raise on missing keys
    tmpl2 = string.Template("$name is $age years old and likes $hobby")
    result2 = tmpl2.safe_substitute(name="Charlie", age=25)
    print "Template: '$name is $age years old and likes $hobby'"
    print "safe_substitute(name='Charlie', age=25) => %s" % result2
