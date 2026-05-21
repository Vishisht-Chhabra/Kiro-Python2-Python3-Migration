"""Numeric Types Demonstration - Python 2 numeric types and literals."""


def run():
    """Demonstrate Python 2 numeric types and literals."""

    print "=== Python 2 Numeric Types Demo ==="
    print ""

    # L suffix for long integers
    print "--- L suffix for long integers ---"
    big_num = 123456789012345678901234567890L
    print "123456789012345678901234567890L =", big_num
    print "Type:", type(big_num)
    small_long = 42L
    print "42L =", small_long
    print "Type of 42L:", type(small_long)
    print ""

    # long() built-in function
    print "--- long() built-in function ---"
    a = long(100)
    print "long(100) =", a, "type:", type(a)
    b = long("999")
    print "long('999') =", b, "type:", type(b)
    c = long(3.14)
    print "long(3.14) =", c, "type:", type(c)
    print "long(0xFF) =", long(0xFF), "type:", type(long(0xFF))
    print ""

    # Octal literal with leading zero
    print "--- Octal literal with leading zero ---"
    octal_val = 0755
    print "0755 (octal) =", octal_val, "(decimal)"
    print "0644 (octal) =", 0644, "(decimal)"
    print "010 (octal) =", 010, "(decimal)"
    print "0777 (octal) =", 0777, "(decimal)"
    print ""

    # <> inequality operator
    print "--- <> inequality operator ---"
    print "5 <> 3:", 5 <> 3
    print "5 <> 5:", 5 <> 5
    print "'hello' <> 'world':", "hello" <> "world"
    print "'same' <> 'same':", "same" <> "same"
    print "Note: <> is equivalent to != in Python 2"
    print ""

    # cmp() built-in function
    print "--- cmp() built-in function ---"
    print "cmp(1, 2) =", cmp(1, 2), " (first < second => -1)"
    print "cmp(2, 2) =", cmp(2, 2), " (equal => 0)"
    print "cmp(3, 2) =", cmp(3, 2), " (first > second => 1)"
    print "cmp('apple', 'banana') =", cmp("apple", "banana")
    print "cmp('zebra', 'apple') =", cmp("zebra", "apple")
    print "cmp([1,2,3], [1,2,4]) =", cmp([1, 2, 3], [1, 2, 4])
