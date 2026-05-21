"""Dictionary Methods Demonstration - Python 2 vs Python 3.

Python 2 dict methods removed in Python 3:
    d.has_key(k)     -> use `k in d`
    d.iterkeys()     -> use `iter(d)` or just iterate d
    d.itervalues()   -> use `iter(d.values())`
    d.iteritems()    -> use `iter(d.items())`

Python 3 dict methods that changed:
    d.keys()         -> returns a dict_keys view (not a list); list(d.keys()) materializes
    d.values()       -> returns a dict_values view; list(d.values()) materializes
    d.items()        -> returns a dict_items view; list(d.items()) materializes
"""


def run():
    """Demonstrate Python 3 dictionary methods (view objects + `in`)."""

    print("=== Python 3 Dictionary Methods Demo ===")
    print("")

    sample = {"name": "Alice", "age": 30, "city": "Paris"}
    print("sample =", sample)
    print("")

    # dict.keys(), dict.values(), dict.items() return view objects in Python 3
    print("--- dict.keys(), values(), items() return view objects ---")
    keys = sample.keys()
    print("sample.keys() =", keys)
    print("type(sample.keys()):", type(keys))
    print("list(sample.keys()) =", list(keys))
    print("")

    values = sample.values()
    print("sample.values() =", values)
    print("type(sample.values()):", type(values))
    print("list(sample.values()) =", list(values))
    print("")

    items = sample.items()
    print("sample.items() =", items)
    print("type(sample.items()):", type(items))
    print("list(sample.items()) =", list(items))
    print("")

    # Membership testing replaces dict.has_key()
    print("--- `in` operator replaces dict.has_key() ---")
    print("'name' in sample:", "name" in sample)
    print("'email' in sample:", "email" in sample)
    print("")

    # Removed Python 2 iterator methods: iterkeys, itervalues, iteritems
    print("--- Removed in Python 3: iterkeys / itervalues / iteritems ---")
    print("Iterating sample directly (replaces iterkeys()):")
    for key in sample:
        print("  key:", key)
    print("")

    print("Iterating sample.values() (replaces itervalues()):")
    for value in sample.values():
        print("  value:", value)
    print("")

    print("Iterating sample.items() (replaces iteritems()):")
    for key, value in sample.items():
        print("  %s -> %r" % (key, value))
