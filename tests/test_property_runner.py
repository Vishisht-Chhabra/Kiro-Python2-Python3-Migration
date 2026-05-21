"""Property test for the demo Runner.

Feature: python2-to-python3-migration, Property 2: Runner captures stdout,
signals errors, and always restores sys.stdout. Validates Requirements 3.4,
3.5, 3.6, 3.7.
"""

import os
import sys
import types

from hypothesis import given, settings, strategies as st

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from runner import DemoRunner, DemoResult


# Strategy: generate output strings that may include HTML metacharacters,
# whitespace, and a few control-adjacent characters so the capture path is
# exercised across a varied alphabet. The strategy avoids characters that
# print() cannot emit on stdout (e.g. raw NULs in some environments) by
# restricting to printable ASCII plus space and tab.
output_text_strategy = st.text(
    alphabet=(
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789"
        " \t<>&\"'/():.,_-+=*"
    ),
    min_size=1,
    max_size=200,
)

# Strategy: select an exception class to raise. Each class has a distinct
# class name so the "error contains class name" assertion is exercised across
# multiple types.
exception_class_strategy = st.sampled_from(
    [ValueError, TypeError, RuntimeError, KeyError, ZeroDivisionError]
)


def _make_module_that_prints(text_to_print):
    """Build a synthetic module whose run() writes text_to_print to stdout."""
    module = types.ModuleType("synthetic_print_module")

    def run(_text=text_to_print):
        # Use sys.stdout.write so we have full control over the emitted bytes
        # (no extra newline appended by print()).
        sys.stdout.write(_text)

    module.run = run
    return module


def _make_module_that_raises(exc_class):
    """Build a synthetic module whose run() raises an instance of exc_class."""
    module = types.ModuleType("synthetic_raise_module")

    def run(_exc_class=exc_class):
        raise _exc_class("boom")

    module.run = run
    return module


@given(text_to_print=output_text_strategy)
@settings(max_examples=100)
def test_runner_normal_return_captures_output_and_restores_stdout(text_to_print):
    """Property 2 (normal-return branch): Runner captures stdout and restores it.

    Feature: python2-to-python3-migration, Property 2: Runner captures stdout,
    signals errors, and always restores sys.stdout. Validates Requirements 3.4,
    3.5, 3.6, 3.7.

    For any synthetic module whose run() prints a string T to sys.stdout and
    returns normally, after DemoRunner.execute(module) returns:
      (a) sys.stdout has been restored to the value it held immediately before
          the call;
      (b) DemoResult.error is None;
      (c) DemoResult.output contains T.
    """
    module = _make_module_that_prints(text_to_print)

    snapshot_stdout = sys.stdout
    result = DemoRunner().execute(module)

    # (a) sys.stdout is restored to the pre-call value.
    assert sys.stdout is snapshot_stdout, (
        "sys.stdout was not restored after DemoRunner.execute on normal return"
    )

    # (b) error is None on normal return.
    assert result.error is None, (
        "Expected DemoResult.error to be None on normal return, got %r"
        % (result.error,)
    )

    # (c) output contains the printed text T.
    assert text_to_print in result.output, (
        "Expected printed text %r to appear in DemoResult.output %r"
        % (text_to_print, result.output)
    )


@given(exc_class=exception_class_strategy)
@settings(max_examples=100)
def test_runner_raising_run_signals_error_and_restores_stdout(exc_class):
    """Property 2 (raise branch): Runner signals errors and restores stdout.

    Feature: python2-to-python3-migration, Property 2: Runner captures stdout,
    signals errors, and always restores sys.stdout. Validates Requirements 3.4,
    3.5, 3.6, 3.7.

    For any synthetic module whose run() raises an exception E, after
    DemoRunner.execute(module) returns:
      (a) sys.stdout has been restored to the value it held immediately before
          the call (this clause must hold whether or not run() raises);
      (b) DemoResult.error is a non-empty string;
      (c) DemoResult.error contains the exception's class name.
    """
    module = _make_module_that_raises(exc_class)

    snapshot_stdout = sys.stdout
    result = DemoRunner().execute(module)

    # (a) sys.stdout is restored even when run() raised.
    assert sys.stdout is snapshot_stdout, (
        "sys.stdout was not restored after DemoRunner.execute when run() raised"
    )

    # (b) error is a non-empty string.
    assert isinstance(result.error, str), (
        "Expected DemoResult.error to be a str when run() raised, got %r"
        % (type(result.error),)
    )
    assert len(result.error) > 0, (
        "Expected DemoResult.error to be non-empty when run() raised"
    )

    # (c) error contains the exception's class name.
    assert exc_class.__name__ in result.error, (
        "Expected exception class name %r in DemoResult.error %r"
        % (exc_class.__name__, result.error)
    )
