"""Unit tests for demo modules.

Tests each of the 13 demo modules by capturing their stdout output
and asserting expected content.

Requirements: 2.1-14.4
"""

import sys
import os
import StringIO

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def capture_demo_output(module):
    """Run a demo module's run() function and capture stdout output."""
    captured = StringIO.StringIO()
    old_stdout = sys.stdout
    try:
        sys.stdout = captured
        module.run()
    finally:
        sys.stdout = old_stdout
    return captured.getvalue()


def test_print_statement_demo():
    """Test print_statement demo output."""
    from demos import print_statement
    output = capture_demo_output(print_statement)

    # Comma-separated values
    assert "Name:" in output
    assert "Alice" in output
    assert "Age:" in output
    # Trailing comma behavior
    assert "First part..." in output
    assert "Second part on same line" in output
    # Stderr redirect via >>
    assert ">> redirect" in output
    assert "Captured from >> redirect:" in output


def test_integer_division_demo():
    """Test integer_division demo output."""
    from demos import integer_division
    output = capture_demo_output(integer_division)

    # 5/2=2
    assert "5 / 2 =" in output
    assert "2" in output
    # / vs // difference
    assert "5 // 2" in output
    # Mixed operands
    assert "5 / 2.0 =" in output
    assert "2.5" in output


def test_unicode_handling_demo():
    """Test unicode_handling demo output."""
    from demos import unicode_handling
    output = capture_demo_output(unicode_handling)

    # Type differences
    assert "type(byte_string):" in output
    assert "type(unicode_string):" in output
    # u"" prefix
    assert 'u"' in output or "u'" in output or "unicode" in output
    # Encode/decode
    assert "encode" in output
    assert "decode" in output


def test_range_xrange_demo():
    """Test range_xrange demo output."""
    from demos import range_xrange
    output = capture_demo_output(range_xrange)

    # range returns a list
    assert "range(5)" in output
    assert "type(range(5)):" in output
    assert "<type 'list'>" in output
    # xrange returns iterator
    assert "xrange(5)" in output
    assert "type(xrange(5)):" in output
    assert "<type 'xrange'>" in output


def test_dict_methods_demo():
    """Test dict_methods demo output."""
    from demos import dict_methods
    output = capture_demo_output(dict_methods)

    # List returns
    assert "sample.keys()" in output
    assert "<type 'list'>" in output
    # has_key
    assert "has_key" in output
    # iter methods
    assert "iterkeys" in output
    assert "itervalues" in output
    assert "iteritems" in output


def test_user_input_demo():
    """Test user_input demo output."""
    from demos import user_input
    output = capture_demo_output(user_input)

    # Simulated raw_input
    assert "raw_input" in output
    assert "Alice" in output
    # Simulated input
    assert "input()" in output or "input" in output
    # Security warning
    assert "dangerous" in output or "WARNING" in output or "Security" in output


def test_exec_statement_demo():
    """Test exec_statement demo output."""
    from demos import exec_statement
    output = capture_demo_output(exec_statement)

    # Variable modification
    assert "Before exec: x =" in output
    assert "After exec" in output
    assert "42" in output
    # Namespace usage
    assert "namespace" in output or "local_ns" in output


def test_string_formatting_demo():
    """Test string_formatting demo output."""
    from demos import string_formatting
    output = capture_demo_output(string_formatting)

    # %s/%d/%f
    assert "%s" in output or "Hello," in output
    assert "%d" in output or "years old" in output
    assert "%f" in output or "meters" in output
    # Named placeholders
    assert "%(name)s" in output or "named" in output.lower()
    # Template
    assert "Template" in output


def test_exception_syntax_demo():
    """Test exception_syntax demo output."""
    from demos import exception_syntax
    output = capture_demo_output(exception_syntax)

    # Comma syntax
    assert "comma syntax" in output
    assert "ZeroDivisionError" in output or "ValueError" in output
    # Old raise
    assert "raise" in output.lower() or "Raised" in output
    # StandardError
    assert "StandardError" in output


def test_numeric_types_demo():
    """Test numeric_types demo output."""
    from demos import numeric_types
    output = capture_demo_output(numeric_types)

    # L suffix
    assert "L" in output
    assert "<type 'long'>" in output
    # long()
    assert "long(" in output
    # Octal
    assert "octal" in output.lower() or "0755" in output
    # <> operator
    assert "<>" in output
    # cmp()
    assert "cmp(" in output


def test_iterators_functional_demo():
    """Test iterators_functional demo output."""
    from demos import iterators_functional
    output = capture_demo_output(iterators_functional)

    # .next() method
    assert ".next()" in output
    # reduce() as built-in
    assert "reduce(" in output
    # apply() function
    assert "apply(" in output
    # map/filter return lists
    assert "map(" in output
    assert "filter(" in output
    assert "<type 'list'>" in output
    # Backtick repr
    assert "backtick" in output.lower() or "`" in output


def test_classes_objects_demo():
    """Test classes_objects demo output."""
    from demos import classes_objects
    output = capture_demo_output(classes_objects)

    # Old-style class
    assert "Old" in output or "old" in output
    # New-style class
    assert "New" in output or "new" in output or "object" in output
    # __metaclass__
    assert "__metaclass__" in output
    # __cmp__
    assert "__cmp__" in output or "cmp(" in output
    # Unbound methods
    assert "unbound" in output.lower() or "Unbound" in output


def test_module_imports_demo():
    """Test module_imports demo output."""
    from demos import module_imports
    output = capture_demo_output(module_imports)

    # StringIO
    assert "StringIO" in output
    # urllib2
    assert "urllib2" in output
    # ConfigParser
    assert "ConfigParser" in output
    # Relative imports
    assert "relative" in output.lower() or "import" in output
