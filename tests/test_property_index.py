"""Property test for index page rendering.

Feature: python2-to-python3-migration, Property 3: Index page contains a link
and title for every registered demo. Validates Requirements 3.9, 3.12.
"""

import html as html_module
import os
import sys

from hypothesis import given, settings
from hypothesis.strategies import lists, text, tuples

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from renderer import HtmlRenderer


# Strategy: generate URL-safe names (alphanumeric plus underscore, non-empty).
name_strategy = text(
    alphabet=(
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789"
        "_"
    ),
    min_size=1,
    max_size=20,
)

# Strategy: generate non-empty title strings drawn from text that includes the
# HTML metacharacters `<`, `>`, `&`, `"` so the escaping guarantee from
# Property 3 is exercised end-to-end.
title_strategy = text(
    alphabet=(
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789"
        " "
        "<>&\""
    ),
    min_size=1,
    max_size=50,
)

# Strategy: generate lists of (name, title) pairs.
demo_list_strategy = lists(
    tuples(name_strategy, title_strategy),
    min_size=0,
    max_size=20,
)


@given(demos=demo_list_strategy)
@settings(max_examples=100)
def test_index_page_contains_all_demo_links(demos):
    """Property 3: Index page contains a link and title for every registered demo.

    Feature: python2-to-python3-migration, Property 3: Index page contains a
    link and title for every registered demo. Validates Requirements 3.9, 3.12.

    For any list of demo (name, title) pairs, the rendered index page HTML
    contains `/demo/<escaped_name>` for each registered demo and contains the
    escaped form of each title, so HTML metacharacters in the inputs do not
    survive unescaped in the output.
    """
    renderer = HtmlRenderer()
    rendered = renderer.render_index(demos)

    for name, title in demos:
        escaped_name = html_module.escape(name, quote=True)
        expected_href = "/demo/%s" % escaped_name
        assert expected_href in rendered, (
            "Expected href '%s' not found in rendered HTML" % expected_href
        )

        escaped_title = html_module.escape(title, quote=True)
        assert escaped_title in rendered, (
            "Expected escaped title '%s' not found in rendered HTML"
            % escaped_title
        )
