"""Integer Division Demonstration - Python 2 classic division behavior."""


def run():
    """Demonstrate Python 2 classic integer division."""

    print "=== Python 2 Integer Division Demo ==="
    print ""

    # Classic division: integer / integer = integer (truncated)
    print "--- Classic Division (integer / integer) ---"
    print "5 / 2 =", 5 / 2
    print "7 / 3 =", 7 / 3
    print "10 / 4 =", 10 / 4
    print "(In Python 2, dividing two integers truncates the result)"
    print ""

    # Floor division operator // (same as / for integers in Python 2)
    print "--- Floor Division // vs Classic / ---"
    print "5 / 2  =", 5 / 2
    print "5 // 2 =", 5 // 2
    print "7 / 3  =", 7 / 3
    print "7 // 3 =", 7 // 3
    print "(With integer operands, / and // give the same result in Python 2)"
    print ""

    # Mixed integer and float operands
    print "--- Mixed Integer and Float Operands ---"
    print "5 / 2.0 =", 5 / 2.0
    print "5.0 / 2 =", 5.0 / 2
    print "7 / 3.0 =", 7 / 3.0
    print "10.0 / 4 =", 10.0 / 4
    print "(When one operand is a float, result is a float)"
