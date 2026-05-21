"""Range and Xrange Demonstration - Python 2 range() vs xrange()."""


def run():
    """Demonstrate Python 2 range() and xrange() differences."""

    print "=== Python 2 Range and Xrange Demo ==="
    print ""

    # range() returns a list
    print "--- range() returns a list ---"
    r = range(5)
    print "range(5) =", r
    print "type(range(5)):", type(r)
    print "range(2, 8) =", range(2, 8)
    print "range(0, 10, 2) =", range(0, 10, 2)
    print ""

    # xrange() returns a lazy iterator
    print "--- xrange() returns a lazy iterator ---"
    xr = xrange(5)
    print "xrange(5) =", xr
    print "type(xrange(5)):", type(xr)
    print "xrange(2, 8) =", xrange(2, 8)
    print ""

    # Iteration results from both
    print "--- Iterating over both ---"
    print "Iterating range(5):",
    for i in range(5):
        print i,
    print ""

    print "Iterating xrange(5):",
    for i in xrange(5):
        print i,
    print ""
    print ""

    # Key difference: memory usage
    print "--- Key Difference ---"
    print "range(5) creates a list in memory:", range(5)
    print "xrange(5) generates values on demand:", xrange(5)
