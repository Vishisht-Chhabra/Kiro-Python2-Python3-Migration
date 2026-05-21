"""Numeric Types Demonstration - Python 2 vs Python 3.

Python 3 unifies arbitrary-precision integers under a single ``int`` type and
removes several Python 2 numeric-syntax constructs. The Python 2 forms shown
below are kept here as text for side-by-side comparison; the demo body uses
their Python 3 replacements.

Removed in Python 3:
    42L                   -> 42                  (int is arbitrary precision)
    long(x)               -> int(x)
    0755                  -> 0o755               (explicit octal prefix)
    a <> b                -> a != b
    cmp(a, b)             -> (a > b) - (a < b)   or functools.cmp_to_key
"""

from functools import cmp_to_key


def run():
    """Demonstrate Python 3 numeric types alongside removed Python 2 forms."""

    print("=== Python 3 Numeric Types Demo ===")
    print("")

    # L suffix for long integers (removed in Python 3)
    print("--- L suffix removed: int is arbitrary precision ---")
    # Python 2: big_num = 123456789012345678901234567890L
    big_num = 123456789012345678901234567890
    print("123456789012345678901234567890 =", big_num)
    print("Type:", type(big_num))
    # Python 2: small_long = 42L
    small_long = 42
    print("42 =", small_long)
    print("Type of 42:", type(small_long))
    print("(Python 2 wrote these as 42L / ...L; Python 3 has no L suffix)")
    print("")

    # long() built-in function (removed in Python 3; use int())
    print("--- long() removed: use int() ---")
    a = int(100)
    print("int(100) =", a, "type:", type(a))
    b = int("999")
    print("int('999') =", b, "type:", type(b))
    c = int(3.14)
    print("int(3.14) =", c, "type:", type(c))
    print("int(0xFF) =", int(0xFF), "type:", type(int(0xFF)))
    print("(Python 2 long(x) is now simply int(x))")
    print("")

    # Octal literal: leading zero removed; use 0o prefix
    print("--- Octal literals require the 0o prefix ---")
    # Python 2: octal_val = 0755
    octal_val = 0o755
    print("0o755 (octal) =", octal_val, "(decimal)")
    print("0o644 (octal) =", 0o644, "(decimal)")
    print("0o10  (octal) =", 0o10, "(decimal)")
    print("0o777 (octal) =", 0o777, "(decimal)")
    print("(Python 2 wrote these as 0755 / 0644 / 010 / 0777)")
    print("")

    # <> inequality operator (removed in Python 3; use !=)
    print("--- <> removed: use != ---")
    print("5 != 3:", 5 != 3)
    print("5 != 5:", 5 != 5)
    print("'hello' != 'world':", "hello" != "world")
    print("'same' != 'same':", "same" != "same")
    print("(Python 2 also accepted 5 <> 3; Python 3 only accepts !=)")
    print("")

    # cmp() built-in (removed in Python 3; use (a > b) - (a < b))
    print("--- cmp() removed: use (a > b) - (a < b) ---")

    def cmp(a, b):
        """Python 3 replacement for the removed Python 2 cmp() built-in."""
        return (a > b) - (a < b)

    print("cmp(1, 2) =", cmp(1, 2), " (first < second => -1)")
    print("cmp(2, 2) =", cmp(2, 2), " (equal => 0)")
    print("cmp(3, 2) =", cmp(3, 2), " (first > second => 1)")
    print("cmp('apple', 'banana') =", cmp("apple", "banana"))
    print("cmp('zebra', 'apple') =", cmp("zebra", "apple"))
    print("cmp([1,2,3], [1,2,4]) =", cmp([1, 2, 3], [1, 2, 4]))
    print("")

    # functools.cmp_to_key for sort use cases that previously passed cmp=...
    print("--- functools.cmp_to_key for sort use cases ---")
    words = ["banana", "apple", "cherry"]
    # Python 2: sorted(words, cmp=lambda a, b: cmp(len(a), len(b)))
    by_length = sorted(words, key=cmp_to_key(lambda a, b: cmp(len(a), len(b))))
    print("sorted by length:", by_length)
