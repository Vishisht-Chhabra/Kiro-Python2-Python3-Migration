"""String Formatting Demonstration - Python 2 vs Python 3.

Python 2 supported %-formatting and string.Template substitution. Python 3
keeps both of those (the %-style examples below still work unchanged) and
adds two newer formatting forms:

    - str.format()        ("{0} is {1}".format(name, age))
    - f-strings (3.6+)    (f"{name} is {age}")

This demo shows all four formatting styles side by side so the Python 3
additions can be compared against their %-formatting predecessors.
"""

import string


def run():
    """Demonstrate Python 3 string formatting alongside %-style and Template."""

    print("=== Python 3 String Formatting Demo ===")
    print("")

    # Basic format specifiers: %s, %d, %f (still valid in Python 3)
    print("--- Basic format specifiers (%s, %d, %f) ---")
    name = "Alice"
    age = 30
    height = 5.6
    print("String: 'Hello, %s!' => " + ("Hello, %s!" % name))
    print("Integer: '%s is %d years old' => " + ("%s is %d years old" % (name, age)))
    print("Float: 'Height: %f meters' => " + ("Height: %f meters" % height))
    print("Float precision: 'Height: %.1f meters' => " + ("Height: %.1f meters" % height))
    print("")

    # Named placeholders with dictionary
    print("--- Named placeholders with dictionary ---")
    data = {"name": "Bob", "city": "Seattle", "temp": 72}
    result = "%(name)s lives in %(city)s where it is %(temp)d degrees" % data
    print("Template: '%(name)s lives in %(city)s where it is %(temp)d degrees'")
    print("Data: %s" % repr(data))
    print("Result: %s" % result)
    print("")

    # Multiple positional arguments with tuple
    print("--- Multiple positional arguments with tuple ---")
    values = ("Python", 3, 11, "current")
    result = "%s version %d.%d is %s" % values
    print("Template: '%s version %d.%d is %s'")
    print("Tuple: %s" % repr(values))
    print("Result: %s" % result)
    print("")

    # Padding and alignment
    print("--- Padding and alignment ---")
    print("Right-aligned: '%10s'" % "hello")
    print("Left-aligned: '%-10s'" % "hello")
    print("Zero-padded: '%05d'" % 42)
    print("")

    # str.format() - Python 3 alternative to %-formatting
    print("--- str.format() (Python 3 alternative to %-formatting) ---")
    # Numbered positional placeholders
    fmt_numbered = "{0} is {1} years old".format(name, age)
    print("Template: '{0} is {1} years old'.format(name, age) => " + fmt_numbered)
    # Empty {} placeholders use positional order
    fmt_empty = "{} is {} years old".format(name, age)
    print("Template: '{} is {} years old'.format(name, age) => " + fmt_empty)
    # Named placeholders
    fmt_named = "{who} likes {what}".format(who="Alice", what="Python")
    print("Template: '{who} likes {what}'.format(who='Alice', what='Python') => " + fmt_named)
    # Format specifiers (alignment / precision) work too
    fmt_spec = "Height: {:.1f} meters".format(height)
    print("Template: 'Height: {:.1f} meters'.format(height) => " + fmt_spec)
    print("")

    # f-strings - the modern Python 3 formatting form (3.6+)
    print("--- f-strings (Python 3.6+) ---")
    fstr_basic = f"Hello, {name}!"
    print("Expression: f'Hello, {name}!' => " + fstr_basic)
    fstr_multi = f"{name} is {age} years old"
    print("Expression: f'{name} is {age} years old' => " + fstr_multi)
    fstr_expr = f"In five years {name} will be {age + 5}"
    print("Expression: f'In five years {name} will be {age + 5}' => " + fstr_expr)
    fstr_spec = f"Height: {height:.1f} meters"
    print("Expression: f'Height: {height:.1f} meters' => " + fstr_spec)
    print("")

    # string.Template class usage (unchanged from Python 2)
    print("--- string.Template class ---")
    tmpl = string.Template("$who likes $what")
    result = tmpl.substitute(who="Alice", what="Python")
    print("Template: '$who likes $what'")
    print("substitute(who='Alice', what='Python') => %s" % result)
    print("")

    # safe_substitute doesn't raise on missing keys
    tmpl2 = string.Template("$name is $age years old and likes $hobby")
    result2 = tmpl2.safe_substitute(name="Charlie", age=25)
    print("Template: '$name is $age years old and likes $hobby'")
    print("safe_substitute(name='Charlie', age=25) => %s" % result2)
