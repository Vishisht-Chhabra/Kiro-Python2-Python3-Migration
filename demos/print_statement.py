"""Print Statement Demonstration - Python 2 vs Python 3.

Python 3 makes print a function. Python 2 used these statement forms:

    print "Hello"
    print "Name:", "Alice", "Age:", 30   # comma-separated values
    print "First part...",               # trailing comma suppresses newline
    print >> sys.stderr, "msg"           # redirect to a stream

Python 3 replaces all of them with print() function calls, and adds the
``sep=``, ``end=``, and ``file=`` keyword arguments for fine-grained control.
"""

import io
import sys


def run():
    """Demonstrate the Python 3 print() function."""

    print("=== Python 3 print() Function Demo ===")
    print("")

    # Basic print() call (parentheses required in Python 3)
    # Python 2 form (now SyntaxError):
    #     print "Hello, World!"
    print("--- Basic print() call ---")
    print("Hello, World!")
    print("")

    # Multiple comma-separated values are passed as positional arguments.
    # Python 2 form:
    #     print "Name:", "Alice", "Age:", 30
    print("--- Multiple positional arguments ---")
    print("Name:", "Alice", "Age:", 30)
    print("Values:", 1, 2, 3, 4, 5)
    print("")

    # The sep= keyword controls what is placed between values
    # (default is a single space).
    print("--- sep= keyword argument ---")
    print("default sep:", "a", "b", "c")
    print("a", "b", "c", sep="-")
    print("2024", "01", "15", sep="/")
    print("")

    # The end= keyword controls what terminates the line
    # (default is "\n"). This replaces Python 2's trailing-comma form.
    # Python 2 form:
    #     print "First part...",
    #     print "Second part on same line"
    print("--- end= keyword argument ---")
    print("First part...", end=" ")
    print("Second part on same line")
    print("no newline at all", end="")
    print(" -> joined together")
    print("")

    # The file= keyword redirects output to any text-mode file-like object.
    # This replaces Python 2's `print >> stream, value` syntax.
    # Python 2 form:
    #     captured = StringIO.StringIO()
    #     print >> captured, "This was written using >> redirect syntax"
    print("--- file= keyword argument (capture via io.StringIO) ---")
    captured = io.StringIO()
    print("This was written using file= keyword", file=captured)
    print("Multiple lines", "can be redirected", file=captured)
    print("Captured from file= redirect:")
    print(captured.getvalue())
    captured.close()

    # file=sys.stderr is the direct Python 3 equivalent of `print >> sys.stderr, ...`.
    # We only mention it here rather than calling it so the captured demo output
    # stays on stdout.
    print("--- file=sys.stderr replaces `print >> sys.stderr, ...` ---")
    print("Equivalent to Py2:  print >> sys.stderr, 'oops'")
    print("Python 3 form:     print('oops', file=sys.stderr)")
    # Demonstrate it once for real, redirected back to stdout would defeat the
    # purpose; we send a single short line so the behavior is observable but
    # does not pollute the captured-output rendering.
    print("(written to stderr below)", file=sys.stderr)
