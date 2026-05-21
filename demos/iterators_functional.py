"""Iterators and Functional Programming Demonstration - Python 2 vs Python 3.

Removed in Python 3:
    it.next()             -> next(it)
    reduce (built-in)     -> from functools import reduce
    apply(f, args, kw)    -> f(*args, **kw)
    map(...)              -> returns an iterator; wrap in list(...) for a list
    filter(...)           -> returns an iterator; wrap in list(...) for a list
    map(None, a, b)       -> list(itertools.zip_longest(a, b))
    `x`  (backtick repr)  -> repr(x)
"""

import itertools
from functools import reduce


def run():
    """Demonstrate Python 3 iterator protocol and functional builtins."""

    print("=== Python 3 Iterators & Functional Programming Demo ===")
    print("")

    # next(it) replaces the Python 2 it.next() method
    print("--- next(it) replaces Python 2's it.next() method ---")
    my_list = [10, 20, 30, 40]
    it = iter(my_list)
    print("Iterator from [10, 20, 30, 40]:")
    print("  next(it) =", next(it))
    print("  next(it) =", next(it))
    print("  next(it) =", next(it))
    print("  next(it) =", next(it))
    print("(Python 2 wrote it.next() for each of those calls.)")
    print("")

    # reduce() moved from built-ins into functools
    print("--- reduce() now lives in functools ---")
    numbers = [1, 2, 3, 4, 5]
    total = reduce(lambda a, b: a + b, numbers)
    print("reduce(lambda a, b: a + b, [1, 2, 3, 4, 5]) =", total)
    product = reduce(lambda a, b: a * b, numbers)
    print("reduce(lambda a, b: a * b, [1, 2, 3, 4, 5]) =", product)
    # reduce with initial value
    total_with_init = reduce(lambda a, b: a + b, numbers, 100)
    print("reduce(lambda a, b: a + b, [1, 2, 3, 4, 5], 100) =", total_with_init)
    print("(Python 2 had reduce as a built-in; in Python 3 import it from functools.)")
    print("")

    # apply() is gone; use *args / **kwargs unpacking
    print("--- apply() replaced by f(*args, **kwargs) unpacking ---")

    def greet(name, greeting="Hello"):
        return "%s, %s!" % (greeting, name)

    # apply(greet, ("World",))  ->  greet(*("World",))
    result = greet(*("World",))
    print("greet(*('World',)) =", result)
    # apply(greet, ("Python",), {"greeting": "Welcome"})
    #   ->  greet(*("Python",), **{"greeting": "Welcome"})
    result2 = greet(*("Python",), **{"greeting": "Welcome"})
    print("greet(*('Python',), **{'greeting': 'Welcome'}) =", result2)

    def add_three(a, b, c):
        return a + b + c

    # apply(add_three, (10, 20, 30))  ->  add_three(*(10, 20, 30))
    result3 = add_three(*(10, 20, 30))
    print("add_three(*(10, 20, 30)) =", result3)
    print("(Python 2 wrote apply(f, args[, kwargs]); Python 3 has no apply.)")
    print("")

    # map() and filter() return iterators in Python 3
    print("--- map() and filter() now return iterators ---")
    nums = [1, 2, 3, 4, 5, 6]

    mapped_iter = map(lambda x: x * x, nums)
    print("map(lambda x: x*x, [1,2,3,4,5,6]) ->", mapped_iter)
    print("  type:", type(mapped_iter))
    print("  list(map(...)) =", list(map(lambda x: x * x, nums)))

    filtered_iter = filter(lambda x: x % 2 == 0, nums)
    print("filter(lambda x: x%2==0, [1,2,3,4,5,6]) ->", filtered_iter)
    print("  type:", type(filtered_iter))
    print("  list(filter(...)) =", list(filter(lambda x: x % 2 == 0, nums)))
    print("(Python 2 returned a list directly; Python 3 returns a lazy iterator.)")
    print("")

    # map(None, a, b) -> itertools.zip_longest(a, b)
    print("--- map(None, a, b) replaced by itertools.zip_longest ---")
    a = [1, 2, 3]
    b = [4, 5, 6]
    zipped = list(itertools.zip_longest(a, b))
    print("list(itertools.zip_longest([1,2,3], [4,5,6])) =", zipped)
    uneven = list(itertools.zip_longest([1, 2, 3], ["x", "y"]))
    print("list(itertools.zip_longest([1,2,3], ['x','y'])) =", uneven)
    print("(Python 2 wrote map(None, a, b); Python 3 has no map(None, ...).)")
    print("")

    # repr(x) replaces backtick repr `x`
    print("--- repr(x) replaces backtick `x` repr syntax ---")
    num = 42
    print("repr of 42 (was `num` in Python 2): " + repr(num))
    items = [1, "hello", 3.14]
    print("repr of [1, 'hello', 3.14] (was `items`): " + repr(items))
    d = {"key": "value"}
    print("repr of {'key': 'value'} (was `d`): " + repr(d))
    print("(Backtick repr was a SyntaxError in Python 3; use repr(x).)")
