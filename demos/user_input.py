"""User Input Demonstration - Python 2 raw_input() and input()."""

import sys
import StringIO


def run():
    """Demonstrate Python 2 raw_input() and input() behavior."""

    print "=== Python 2 User Input Demo ==="
    print ""

    # Simulate raw_input() behavior
    print "--- raw_input() behavior ---"
    print "raw_input() reads a line from stdin and returns it as a string."
    print "Example: name = raw_input('Enter your name: ')"
    print ""

    # Simulate by replacing stdin
    old_stdin = sys.stdin
    sys.stdin = StringIO.StringIO("Alice\n")
    name = raw_input("Enter your name: ")
    sys.stdin = old_stdin
    print "Simulated input: 'Alice'"
    print "Result: name =", repr(name)
    print "type(name):", type(name)
    print ""

    # Simulate input() evaluating expressions
    print "--- input() evaluates expressions ---"
    print "Python 2 input() is equivalent to eval(raw_input())"
    print "Example: value = input('Enter expression: ')"
    print ""

    # Safe simulation using eval to show the behavior
    old_stdin = sys.stdin
    sys.stdin = StringIO.StringIO("2 + 3\n")
    result = input("Enter expression: ")
    sys.stdin = old_stdin
    print "Simulated input: '2 + 3'"
    print "Result: value =", result
    print "type(value):", type(result)
    print "(input() evaluated '2 + 3' and returned integer 5)"
    print ""

    # Security implications
    print "--- Security Implications ---"
    print "WARNING: Python 2 input() is dangerous!"
    print "It calls eval() on user input, which can execute arbitrary code."
    print "Example of dangerous input: __import__('os').system('rm -rf /')"
