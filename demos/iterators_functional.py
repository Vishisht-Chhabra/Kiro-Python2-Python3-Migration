"""Iterators and Functional Programming Demonstration - Python 2 iterator protocol and functional builtins."""


def run():
    """Demonstrate Python 2 iterator protocol and functional builtins."""

    print "=== Python 2 Iterators & Functional Programming Demo ==="
    print ""

    # .next() method on iterators
    print "--- .next() method on iterators ---"
    my_list = [10, 20, 30, 40]
    it = iter(my_list)
    print "Iterator from [10, 20, 30, 40]:"
    print "  it.next() =", it.next()
    print "  it.next() =", it.next()
    print "  it.next() =", it.next()
    print "  it.next() =", it.next()
    print ""

    # reduce() as a built-in (no import needed)
    print "--- reduce() as a built-in ---"
    numbers = [1, 2, 3, 4, 5]
    total = reduce(lambda a, b: a + b, numbers)
    print "reduce(lambda a, b: a + b, [1, 2, 3, 4, 5]) =", total
    product = reduce(lambda a, b: a * b, numbers)
    print "reduce(lambda a, b: a * b, [1, 2, 3, 4, 5]) =", product
    # reduce with initial value
    total_with_init = reduce(lambda a, b: a + b, numbers, 100)
    print "reduce(lambda a, b: a + b, [1, 2, 3, 4, 5], 100) =", total_with_init
    print ""

    # apply() function
    print "--- apply() function ---"
    def greet(name, greeting="Hello"):
        return "%s, %s!" % (greeting, name)

    result = apply(greet, ("World",))
    print "apply(greet, ('World',)) =", result
    result2 = apply(greet, ("Python",), {"greeting": "Welcome"})
    print "apply(greet, ('Python',), {'greeting': 'Welcome'}) =", result2

    def add_three(a, b, c):
        return a + b + c

    result3 = apply(add_three, (10, 20, 30))
    print "apply(add_three, (10, 20, 30)) =", result3
    print ""

    # map() and filter() returning lists
    print "--- map() and filter() return lists ---"
    nums = [1, 2, 3, 4, 5, 6]
    mapped = map(lambda x: x * x, nums)
    print "map(lambda x: x*x, [1,2,3,4,5,6]) =", mapped
    print "  type:", type(mapped)

    filtered = filter(lambda x: x % 2 == 0, nums)
    print "filter(lambda x: x%2==0, [1,2,3,4,5,6]) =", filtered
    print "  type:", type(filtered)

    # map with None (zip-like behavior)
    a = [1, 2, 3]
    b = [4, 5, 6]
    zipped = map(None, a, b)
    print "map(None, [1,2,3], [4,5,6]) =", zipped
    print ""

    # Backtick repr syntax
    print "--- Backtick repr syntax ---"
    num = 42
    print "repr of 42 using backticks: " + `num`
    my_list = [1, "hello", 3.14]
    print "repr of [1, 'hello', 3.14] using backticks: " + `my_list`
    d = {"key": "value"}
    print "repr of {'key': 'value'} using backticks: " + `d`
