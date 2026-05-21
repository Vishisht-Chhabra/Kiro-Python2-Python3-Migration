"""Property test for registry registration order.

Feature: python2-to-python3-migration, Property 1: Registry preserves
registration order. Validates Requirements 3.2, 3.3.
"""

import os
import sys
import types

from hypothesis import given, settings, strategies as st

# conftest.py also inserts the project root onto sys.path, but we add it here
# defensively so this module can be imported standalone (e.g. for static
# inspection or `python -m py_compile`).
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from registry import DemoRegistry


# Strategy: generate URL-safe demo names (lowercase letters, digits, underscore).
# Names must be pairwise distinct within a single registry, which we enforce
# via `unique_by` on the outer list strategy.
name_strategy = st.text(
    alphabet="abcdefghijklmnopqrstuvwxyz0123456789_",
    min_size=1,
    max_size=20,
)

# Strategy: generate non-empty title strings (printable ASCII).
title_strategy = st.text(
    alphabet=(
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789 _-."
    ),
    min_size=1,
    max_size=50,
)

# Strategy: generate a list of (name, title) pairs where the names are pairwise
# distinct. Module objects are minted per-registration inside the test body so
# each registered module is a unique sentinel comparable with `is`.
demo_pairs_strategy = st.lists(
    st.tuples(name_strategy, title_strategy),
    unique_by=lambda t: t[0],
    min_size=0,
    max_size=20,
)


@given(pairs=demo_pairs_strategy)
@settings(max_examples=100)
def test_registry_preserves_registration_order(pairs):
    """Property 1: Registry preserves registration order.

    Feature: python2-to-python3-migration, Property 1: Registry preserves
    registration order. Validates Requirements 3.2, 3.3.

    For any finite sequence of `(name, title, module)` registrations with
    pairwise-distinct names submitted to a fresh DemoRegistry:
      (a) `get_all()` returns the `(name, title)` pairs in registration order;
      (b) `get_module(name)` returns the exact module object that was
          registered for every registered name (compared with `is`);
      (c) `get_module(unregistered_name)` returns `None`.
    """
    registry = DemoRegistry()

    # Register each (name, title) with a fresh, unique ModuleType sentinel so
    # we can later verify identity (not just equality) of the returned module.
    registered_modules = {}
    for name, title in pairs:
        module = types.ModuleType(name)
        registered_modules[name] = module
        registry.register(name, title, module)

    # Assertion (a): get_all() returns (name, title) pairs in registration order.
    expected_pairs = [(name, title) for name, title in pairs]
    assert registry.get_all() == expected_pairs, (
        "Expected get_all() to return %r in registration order, got %r"
        % (expected_pairs, registry.get_all())
    )

    # Assertion (b): get_module(name) returns the exact module object registered.
    for name, _title in pairs:
        assert registry.get_module(name) is registered_modules[name], (
            "Expected get_module(%r) to return the registered module object"
            % name
        )

    # Assertion (c): get_module(unregistered_name) returns None.
    # Derive a name that is guaranteed not to be in the registered set by
    # appending a sentinel suffix to a name that cannot collide with any
    # value the strategy emits (the suffix '!' is outside the strategy's
    # alphabet, so no generated name can equal it).
    registered_names = {name for name, _ in pairs}
    unregistered_name = "unregistered!sentinel"
    assert unregistered_name not in registered_names
    assert registry.get_module(unregistered_name) is None, (
        "Expected get_module(%r) to return None for an unregistered name"
        % unregistered_name
    )
