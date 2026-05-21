"""Property test for index page rendering.

Feature: python2-sample-app, Property 1: Index page lists all registered demos

Validates: Requirements 1.3
"""

from hypothesis import given, settings
from hypothesis.strategies import text, lists, tuples
import re
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from renderer import HtmlRenderer


# Strategy: generate URL-safe names (lowercase letters and underscores, non-empty)
name_strategy = text(
    alphabet="abcdefghijklmnopqrstuvwxyz_",
    min_size=1,
    max_size=20
)

# Strategy: generate non-empty title strings (printable ASCII, no HTML special chars)
title_strategy = text(
    alphabet="abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
    min_size=1,
    max_size=50
)

# Strategy: generate lists of (name, title) pairs
demo_list_strategy = lists(
    tuples(name_strategy, title_strategy),
    min_size=0,
    max_size=20
)


@given(demos=demo_list_strategy)
@settings(max_examples=100, use_coverage=False)
def test_index_page_contains_all_demo_links(demos):
    """Property 1: Index page lists all registered demos.

    For any set of demo (name, title) pairs, the rendered index page
    HTML contains a link with href /demo/<name> for each registered demo
    and contains the title text for each registered demo.
    """
    renderer = HtmlRenderer()
    html = renderer.render_index(demos)

    for name, title in demos:
        # Verify href /demo/<name> is present
        expected_href = '/demo/%s' % name
        assert expected_href in html, (
            "Expected href '%s' not found in rendered HTML" % expected_href
        )

        # Verify title text is present in the HTML
        assert title in html, (
            "Expected title '%s' not found in rendered HTML" % title
        )
