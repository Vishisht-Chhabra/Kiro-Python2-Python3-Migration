"""User Input Demonstration - Python 2 vs Python 3.

Python 2 had two reading builtins; Python 3 has one. Mapping table:

    Python 2                       Python 3
    --------------------------     ----------------------------------
    raw_input(prompt)  -> str        input(prompt)            -> str
    input(prompt)      -> eval()     eval(input(prompt))      -> any
                                     (DANGEROUS: evaluates
                                      arbitrary user expressions)

In Python 2, raw_input() returned the entered line verbatim as a str,
while input() was equivalent to eval(raw_input(prompt)) - it parsed and
evaluated whatever the user typed. Python 3 renamed raw_input() to
input() and removed the eval-based input() entirely. To recreate the
old eval-based behavior in Python 3, wrap input() with eval(...).
"""

import sys
import io


def run():
    """Demonstrate Python 3 input() (and the eval(input()) replacement for Py2 input())."""

    print("=== Python 3 User Input Demo ===")
    print("")

    # Python 3 input() returns a str - it replaces Python 2 raw_input()
    print("--- input() reads a line from stdin and returns it as str ---")
    print("Python 2 had raw_input(prompt); Python 3 renamed it to input(prompt).")
    print("Example: name = input('Enter your name: ')")
    print("")

    # Simulate by replacing stdin with an io.StringIO holding canned input
    old_stdin = sys.stdin
    sys.stdin = io.StringIO("Alice\n")
    try:
        name = input("Enter your name: ")
    finally:
        sys.stdin = old_stdin
    print("Simulated input: 'Alice'")
    print("Result: name =", repr(name))
    print("type(name):", type(name))
    print("(input() in Python 3 returns a str, just like Python 2 raw_input() did.)")
    print("")

    # Python 2 input() evaluated expressions; Py3 equivalent is eval(input())
    print("--- eval(input()) is the Python 3 equivalent of Python 2 input() ---")
    print("Python 2 input(prompt) was equivalent to eval(raw_input(prompt)).")
    print("Python 3 removed that behavior. To get it back, wrap input() with eval().")
    print("Example: value = eval(input('Enter expression: '))")
    print("")

    old_stdin = sys.stdin
    sys.stdin = io.StringIO("2 + 3\n")
    try:
        result = eval(input("Enter expression: "))
    finally:
        sys.stdin = old_stdin
    print("Simulated input: '2 + 3'")
    print("Result: value =", result)
    print("type(value):", type(result))
    print("(eval(input()) parsed and evaluated '2 + 3' and returned the integer 5)")
    print("")

    # Security warning - this is the whole reason Py3 dropped the eval-based input()
    print("--- Security Implications ---")
    print("WARNING: eval(input(...)) is dangerous!")
    print("It calls eval() on whatever the user types, which can execute arbitrary code.")
    print("Never use eval(input(...)) on untrusted input. Examples of dangerous input:")
    print("  __import__('os').system('rm -rf /')")
    print("  open('/etc/passwd').read()")
    print("Use input() (which returns a plain str) and parse it explicitly with")
    print("int(), float(), ast.literal_eval(), or a real parser instead.")
