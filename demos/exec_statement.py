"""Exec Statement Demonstration - Python 2 exec as a statement."""


def run():
    """Demonstrate Python 2 exec statement syntax."""

    print "=== Python 2 Exec Statement Demo ==="
    print ""

    # exec as a statement (no parentheses needed in Python 2)
    print "--- exec as a statement (modifying local variables) ---"
    x = 10
    print "Before exec: x =", x
    exec "x = 42"
    print "After exec 'x = 42': x =", x
    print ""

    # exec with code that creates new variables
    print "--- exec creating new variables ---"
    exec "y = x + 8"
    print "After exec 'y = x + 8': y =", y
    print ""

    # exec with explicit global and local namespace dictionaries
    print "--- exec with explicit namespaces ---"
    global_ns = {"__builtins__": __builtins__}
    local_ns = {"a": 5, "b": 10}
    print "Before exec: local_ns =", local_ns
    exec "result = a + b" in global_ns, local_ns
    print "After exec 'result = a + b' in namespaces:"
    print "  local_ns['result'] =", local_ns['result']
    print ""

    # exec with only globals dict
    print "--- exec with globals dict only ---"
    my_globals = {"__builtins__": __builtins__, "value": 100}
    exec "doubled = value * 2" in my_globals
    print "After exec 'doubled = value * 2' in my_globals:"
    print "  my_globals['doubled'] =", my_globals['doubled']
    print ""

    # exec multi-line code
    print "--- exec with multi-line code ---"
    code = """
items = [1, 2, 3, 4, 5]
total = 0
for item in items:
    total = total + item
"""
    ns = {}
    exec code in ns
    print "After exec multi-line code:"
    print "  ns['items'] =", ns['items']
    print "  ns['total'] =", ns['total']
