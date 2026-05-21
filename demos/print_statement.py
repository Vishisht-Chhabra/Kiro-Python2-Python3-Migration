"""Print Statement Demonstration - Python 2 print syntax features."""

import sys
import StringIO


def run():
    """Demonstrate Python 2 print statement syntax."""

    print "=== Python 2 Print Statement Demo ==="
    print ""

    # Basic print statement (no parentheses needed)
    print "--- Basic print statement ---"
    print "Hello, World!"
    print ""

    # Print with multiple comma-separated values
    print "--- Multiple comma-separated values ---"
    print "Name:", "Alice", "Age:", 30
    print "Values:", 1, 2, 3, 4, 5
    print ""

    # Trailing comma suppresses newline
    print "--- Trailing comma (suppresses newline) ---"
    print "First part...",
    print "Second part on same line"
    print ""

    # >> redirect syntax for writing to stderr
    print "--- >> redirect syntax (writing to stderr via StringIO) ---"
    captured = StringIO.StringIO()
    print >> captured, "This was written using >> redirect syntax"
    print >> captured, "Multiple lines", "can be redirected"
    print "Captured from >> redirect:"
    print captured.getvalue()
    captured.close()
