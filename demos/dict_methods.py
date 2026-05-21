"""Dictionary Methods Demonstration - Python 2 dict methods returning lists."""


def run():
    """Demonstrate Python 2 dictionary methods."""

    print "=== Python 2 Dictionary Methods Demo ==="
    print ""

    sample = {"name": "Alice", "age": 30, "city": "Paris"}
    print "sample =", sample
    print ""

    # dict.keys(), dict.values(), dict.items() return lists
    print "--- dict.keys(), values(), items() return lists ---"
    keys = sample.keys()
    print "sample.keys() =", keys
    print "type(sample.keys()):", type(keys)
    print ""

    values = sample.values()
    print "sample.values() =", values
    print "type(sample.values()):", type(values)
    print ""

    items = sample.items()
    print "sample.items() =", items
    print "type(sample.items()):", type(items)
    print ""

    # dict.has_key() method
    print "--- dict.has_key() method ---"
    print "sample.has_key('name'):", sample.has_key("name")
    print "sample.has_key('email'):", sample.has_key("email")
    print ""

    # dict.iterkeys(), itervalues(), iteritems() return iterators
    print "--- dict.iterkeys(), itervalues(), iteritems() ---"
    print "sample.iterkeys() =", sample.iterkeys()
    print "type(sample.iterkeys()):", type(sample.iterkeys())
    print "list(sample.iterkeys()) =", list(sample.iterkeys())
    print ""

    print "sample.itervalues() =", sample.itervalues()
    print "type(sample.itervalues()):", type(sample.itervalues())
    print "list(sample.itervalues()) =", list(sample.itervalues())
    print ""

    print "sample.iteritems() =", sample.iteritems()
    print "type(sample.iteritems()):", type(sample.iteritems())
    print "list(sample.iteritems()) =", list(sample.iteritems())
