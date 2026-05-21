"""Range and Xrange Demonstration - Python 2 vs Python 3.

Python 2 had two related builtins:

    range(5)         -> [0, 1, 2, 3, 4]   # eagerly built list
    xrange(5)        -> xrange(5)         # lazy iterator, memory-efficient

In Python 3, ``xrange`` was removed and ``range`` was reworked to be a lazy,
memory-efficient ``range`` object that subsumes the behavior of Python 2's
``xrange``. When a list is actually needed, callers materialize it explicitly
with ``list(range(...))``:

    range(5)         -> range(0, 5)       # lazy range object (subsumes xrange)
    list(range(5))   -> [0, 1, 2, 3, 4]   # materialize when needed
    xrange           -> removed (NameError in Python 3)

This demo exercises the Python 3 ``range`` object and shows the materialized
list form so the educational comparison with Python 2 stays intact.
"""


def run():
    """Demonstrate the Python 3 range object (xrange has been removed)."""

    print("=== Python 3 range Demo (xrange has been removed) ===")
    print("")

    # In Python 3, range(...) returns a lazy range object, not a list.
    # Python 2 form (eager list):
    #     r = range(5)        # -> [0, 1, 2, 3, 4]
    print("--- range(5) returns a lazy range object ---")
    r = range(5)
    print("range(5) =", r)
    print("type(range(5)):", type(r))
    print("range(2, 8) =", range(2, 8))
    print("range(0, 10, 2) =", range(0, 10, 2))
    print("")

    # To get the Python 2 list-style result, materialize with list(...).
    print("--- Materializing a range object with list(...) ---")
    print("list(range(5)) =", list(range(5)))
    print("list(range(2, 8)) =", list(range(2, 8)))
    print("list(range(0, 10, 2)) =", list(range(0, 10, 2)))
    assert list(range(5)) == [0, 1, 2, 3, 4]
    print("assert list(range(5)) == [0, 1, 2, 3, 4]  -> passed")
    print("")

    # xrange no longer exists in Python 3.
    # Python 2 form:
    #     xr = xrange(5)
    #     for i in xrange(5): ...
    print("--- xrange has been removed in Python 3 ---")
    print("Python 2: xrange(5) -> xrange(5)         (lazy iterator)")
    print("Python 3: xrange    -> NameError (use range instead)")
    print("")

    # Iteration: in Python 3, range is itself iterable and lazy.
    # The Python 2 trailing-comma form `print i,` becomes
    # `print(i, end=' ')` to suppress the newline.
    print("--- Iterating over a range object ---")
    print("Iterating range(5):", end=" ")
    for i in range(5):
        print(i, end=" ")
    print("")
    print("")

    # Memory / laziness note: range(N) does not allocate N integers up-front;
    # values are produced on demand, just like Python 2's xrange did.
    print("--- Key difference vs Python 2 ---")
    print("Python 2: range(N)  built a full list of N ints in memory.")
    print("Python 2: xrange(N) produced ints lazily (memory-efficient).")
    print("Python 3: range(N)  is lazy by default; it subsumes xrange.")
    print("Python 3: list(range(N)) when you actually need a list.")
