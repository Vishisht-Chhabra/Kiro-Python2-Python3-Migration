"""Property tests for demo page rendering.

Feature: python2-to-python3-migration

Property 4: Demo page (success) contains escaped source and output.
    Validates Requirements 3.10, 3.12.
Property 5: Demo page (error) contains the escaped error message.
    Validates Requirements 3.11, 3.12.
"""

from hypothesis import given, settings
from hypothesis.strategies import text
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from html import escape

from renderer import HtmlRenderer
from runner import DemoResult


# Strategy: generate non-empty source code strings.
# The alphabet includes the HTML metacharacters `<`, `>`, `&`, `"` so the
# renderer's escaping guarantee (Property 4) is exercised end-to-end.
source_strategy = text(
    alphabet=(
        "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789_=():.+-*/"
        "<>&\""
    ),
    min_size=1,
    max_size=100,
)

# Strategy: generate non-empty output strings.
# Includes HTML metacharacters for the same reason as source_strategy.
output_strategy = text(
    alphabet=(
        "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789_=():.+-*/\n"
        "<>&\""
    ),
    min_size=1,
    max_size=100,
)

# Strategy: generate non-empty error message strings.
# Includes HTML metacharacters for the Property 5 escaping check.
error_strategy = text(
    alphabet=(
        "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789_=():.+-*/\n"
        "<>&\""
    ),
    min_size=1,
    max_size=100,
)

# Strategy: generate title strings.
# Includes HTML metacharacters so escaped titles are exercised in the rendered
# page as well.
title_strategy = text(
    alphabet=(
        "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789"
        "<>&\""
    ),
    min_size=1,
    max_size=50,
)


@given(title=title_strategy, source=source_strategy, output=output_strategy)
@settings(max_examples=100)
def test_demo_page_success_contains_source_and_output(title, source, output):
    """Feature: python2-to-python3-migration, Property 4: Demo page (success) contains escaped source and output. Validates Requirements 3.10, 3.12.

    For any DemoResult with non-empty source_code and output, the rendered demo
    page HTML contains both the source code text and the output text in their
    HTML-escaped form.
    """
    renderer = HtmlRenderer()
    result = DemoResult(source_code=source, output=output, error=None)
    html = renderer.render_demo(title, result)

    escaped_source = escape(source, quote=True)
    escaped_output = escape(output, quote=True)

    assert escaped_source in html, (
        "Expected escaped source code %r not found in rendered HTML" % source
    )
    assert escaped_output in html, (
        "Expected escaped output %r not found in rendered HTML" % output
    )


@given(title=title_strategy, source=source_strategy, error=error_strategy)
@settings(max_examples=100)
def test_demo_page_error_contains_error_message(title, source, error):
    """Feature: python2-to-python3-migration, Property 5: Demo page (error) contains the escaped error message. Validates Requirements 3.11, 3.12.

    For any DemoResult with a non-None error field, the rendered demo page HTML
    contains the error message text in its HTML-escaped form.
    """
    renderer = HtmlRenderer()
    result = DemoResult(source_code=source, output="", error=error)
    html = renderer.render_demo(title, result)

    escaped_error = escape(error, quote=True)

    assert escaped_error in html, (
        "Expected escaped error message %r not found in rendered HTML" % error
    )
