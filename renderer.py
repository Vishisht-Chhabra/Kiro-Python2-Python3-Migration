"""HTML Renderer module.

Generates HTML pages for the demo application including the index page,
individual demo pages, and error pages. Uses html.escape() for HTML entity
escaping and links to an external stylesheet.
"""

import html


class HtmlRenderer:
    """Renders HTML pages for the demo application.

    Generates the index page with demo links, individual demo pages
    with source code and output, and a 404 error page.
    """

    def render_index(self, demos):
        """Render the index page.

        Args:
            demos: list of (name, title) tuples

        Returns:
            HTML string with clickable links for each demo.
        """
        links = ""
        for name, title in demos:
            escaped_title = html.escape(title, quote=True)
            links += '        <li><a href="/demo/%s">%s</a></li>\n' % (
                html.escape(name, quote=True), escaped_title
            )

        return """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Python 2 Feature Demos</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <h1>Python 2 Feature Demos</h1>
    <p>Select a demonstration to view its source code and output:</p>
    <ul>
%s    </ul>
</body>
</html>""" % links

    def render_demo(self, title, result):
        """Render a demo page.

        Args:
            title: display title
            result: DemoResult instance with source_code, output, and error fields

        Returns:
            HTML string showing source code and output (or error).
        """
        escaped_title = html.escape(title, quote=True)
        escaped_source = html.escape(result.source_code, quote=True)

        output_section = ""
        if result.error is not None:
            escaped_error = html.escape(result.error, quote=True)
            output_section = (
                '    <h2>Error</h2>\n'
                '    <div class="error-block">\n'
                '        <pre>%s</pre>\n'
                '    </div>' % escaped_error
            )
        else:
            escaped_output = html.escape(result.output, quote=True)
            output_section = (
                '    <h2>Output</h2>\n'
                '    <pre class="output">%s</pre>' % escaped_output
            )

        return """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>%s - Python 2 Feature Demos</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <h1>%s</h1>
    <p><a href="/">&larr; Back to index</a></p>
    <h2>Source Code</h2>
    <pre><code>%s</code></pre>
%s
</body>
</html>""" % (escaped_title, escaped_title, escaped_source, output_section)

    def render_404(self):
        """Render a 404 page.

        Returns:
            HTML string for a simple 404 Not Found page.
        """
        return """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>404 Not Found - Python 2 Feature Demos</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <h1>404 Not Found</h1>
    <p>The page you requested was not found.</p>
    <p><a href="/">&larr; Back to index</a></p>
</body>
</html>"""
