"""Integer Division Demonstration - Python 2 vs Python 3.

In Python 2, ``/`` performed *classic* division: when both operands were
integers the result was an integer (truncated toward negative infinity for
positive operands). In Python 3, ``/`` is *true* division and always returns
a float, while ``//`` is the explicit *floor* division operator.

    Python 2 (classic division):
        5 / 2   == 2          # int / int -> int (truncated)
        7 / 3   == 2
        10 / 4  == 2
        5 // 2  == 2          # // and / behave the same for ints in Py2

    Python 3 (true division):
        5 / 2   == 2.5        # always float division
        7 / 3   == 2.3333333333333335
        10 / 4  == 2.5
        5 // 2  == 2          # explicit floor division
"""


def run():
    """Demonstrate Python 3 true division and floor division."""

    # Python 2 (classic division):
    #   5 / 2  == 2          # int / int -> int (truncated)
    #   7 / 3  == 2
    # Python 3 (true division):
    #   5 / 2  == 2.5        # always float division
    #   5 // 2 == 2          # explicit floor division

    print("=== Python 3 Integer Division Demo ===")
    print("")

    # True division: / always returns a float in Python 3
    print("--- True Division (/ always returns a float) ---")
    print("5 / 2 =", 5 / 2)
    print("7 / 3 =", 7 / 3)
    print("10 / 4 =", 10 / 4)
    print("(In Python 3, / always performs true division and returns a float)")
    print("")

    # Floor division operator // truncates toward negative infinity
    print("--- Floor Division // vs True Division / ---")
    print("5 / 2  =", 5 / 2)
    print("5 // 2 =", 5 // 2)
    print("7 / 3  =", 7 / 3)
    print("7 // 3 =", 7 // 3)
    print("(Use // when you want the Python 2-style integer result)")
    print("")

    # Mixed integer and float operands: same in both Python 2 and Python 3
    print("--- Mixed Integer and Float Operands ---")
    print("5 / 2.0 =", 5 / 2.0)
    print("5.0 / 2 =", 5.0 / 2)
    print("7 / 3.0 =", 7 / 3.0)
    print("10.0 / 4 =", 10.0 / 4)
    print("(When one operand is a float, the result is a float - same as Py2)")
