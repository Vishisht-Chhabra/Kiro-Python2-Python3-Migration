"""Property test for demo page rendering.

Feature: python2-sample-app, Property 2: Demo page rendering includes source and output

Validates: Requirements 1.4, 1.5
"""

from hypothesis import given, settings
from hypothesis.strategies import text
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from renderer import HtmlRenderer
from runner import DemoResult


# Strategy: generate non-empty source code strings (printable ASCII)
source_strategy = text(
    alphabet="abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_=():.+-*/",
    min_size=1,
    max_size=100
)

# Strategy: generate non-empty output strings
output_strategy = text(
    alphabet="abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_=():.+-*/\n",
    min_size=1,
    max_size=100
)

# Strategy: generate non-empty error message strings
error_strategy = text(
    alphabet="abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_=():.+-*/\n",
    min_size=1,
    max_size=100
)

# Strategy: generate title strings
title_strategy = text(
    alphabet="abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
    min_size=1,
    max_size=50
)


@given(title=title_strategy, source=source_strategy, output=output_strategy)
@settings(max_examples=100, use_coverage=False)
def test_demo_page_success_contains_source_and_output(title, source, output):
    """Property 2 (success case): Demo page rendering includes source and output.

    For any DemoResult with non-empty source_code and output,
    the rendered demo page HTML contains both the source code text
    and the output text.
    """
    renderer = HtmlRenderer()
    result = DemoResult(source_code=source, output=output, error=None)
    html = renderer.render_demo(title, result)

    assert source in html, (
        "Expected source code '%s' not found in rendered HTML" % source
    )
    assert output in html, (
        "Expected output '%s' not found in rendered HTML" % output
    )


@given(title=title_strategy, source=source_strategy, error=error_strategy)
@settings(max_examples=100, use_coverage=False)
def test_demo_page_error_contains_error_message(title, source, error):
    """Property 2 (error case): Demo page rendering includes error message.

    For any DemoResult with a non-None error field,
    the rendered demo page HTML contains the error message text.
    """
    renderer = HtmlRenderer()
    result = DemoResult(source_code=source, output="", error=error)
    html = renderer.render_demo(title, result)

    assert error in html, (
        "Expected error message '%s' not found in rendered HTML" % error
    )
