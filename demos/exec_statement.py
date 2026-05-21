"""Exec Statement Demonstration - Python 3 exec as a builtin function.

Python 2 (exec is a statement):
  exec "x = 42"
  exec "result = a + b" in global_ns, local_ns
  exec code_str in ns
Python 3 (exec is a builtin function):
  exec("x = 42")
  exec("result = a + b", global_ns, local_ns)
  exec(code_str, ns)

Note on namespace semantics: in Python 3, calling ``exec("x = 42")`` inside
a function does NOT modify the enclosing function's local variables, because
Python 3 resolves function locals statically at compile time. To observe the
variable mutation, pass an explicit namespace dict and inspect it after the
call (see the single-namespace example below).
"""


def run():
    """Demonstrate Python 3 exec function syntax."""

    print("=== Python 3 Exec Function Demo ===")
    print("")

    # exec as a function call with a single namespace dict.
    # In Py2 this was: exec "x = 42"  (mutated function locals)
    # In Py3 we route the assignment through an inspectable dict instead,
    # because exec() cannot mutate a function's static locals.
    print("--- exec with a single namespace (modifying a dict) ---")
    ns = {}
    exec("x = 42", ns)
    print("After exec('x = 42', ns): ns['x'] =", ns['x'])
    print("")

    # exec creating new variables in the same namespace dict.
    # In Py2 this was: exec "y = x + 8"  (read x from locals, write y to locals)
    exec("y = ns['x'] + 8", {"ns": ns}, ns)
    print("After exec('y = ns[\\'x\\'] + 8', ...): ns['y'] =", ns['y'])
    print("")

    # exec with explicit global and local namespace dictionaries.
    # In Py2 this was: exec "result = a + b" in global_ns, local_ns
    print("--- exec with explicit namespaces ---")
    global_ns = {"__builtins__": __builtins__}
    local_ns = {"a": 5, "b": 10}
    print("Before exec: local_ns =", local_ns)
    exec("result = a + b", global_ns, local_ns)
    print("After exec('result = a + b', global_ns, local_ns):")
    print("  local_ns['result'] =", local_ns['result'])
    print("")

    # exec with only a globals dict.
    # In Py2 this was: exec "doubled = value * 2" in my_globals
    print("--- exec with globals dict only ---")
    my_globals = {"__builtins__": __builtins__, "value": 100}
    exec("doubled = value * 2", my_globals)
    print("After exec('doubled = value * 2', my_globals):")
    print("  my_globals['doubled'] =", my_globals['doubled'])
    print("")

    # exec multi-line code.
    # In Py2 this was: exec code in ns
    print("--- exec with multi-line code ---")
    code = """
items = [1, 2, 3, 4, 5]
total = 0
for item in items:
    total = total + item
"""
    multi_ns = {}
    exec(code, multi_ns)
    print("After exec(code, multi_ns):")
    print("  multi_ns['items'] =", multi_ns['items'])
    print("  multi_ns['total'] =", multi_ns['total'])
