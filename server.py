"""HTTP Server module.

Provides the request handler and server setup for the Python 2 demo
application. Routes requests to the appropriate handler based on URL path.
"""

import os
from http.server import BaseHTTPRequestHandler


class DemoRequestHandler(BaseHTTPRequestHandler):
    """Request handler for the Python 2 demo application.

    Routes GET requests to the index page, individual demo pages,
    or static files. Uses class-level attributes for shared dependencies.

    Class Attributes:
        registry: DemoRegistry instance for looking up demos.
        runner: DemoRunner instance for executing demo modules.
        renderer: HtmlRenderer instance for generating HTML pages.
    """

    registry = None
    runner = None
    renderer = None

    def do_GET(self):
        """Route GET requests based on URL path.

        Routes:
            /                  -> index page with all demo links
            /demo/<name>       -> demo page for the named demo
            /static/style.css  -> static CSS stylesheet
            anything else      -> 404 page
        """
        path = self.path

        if path == "/":
            self._serve_index()
        elif path.startswith("/demo/"):
            name = path[len("/demo/"):]
            self._serve_demo(name)
        elif path == "/static/style.css":
            self._serve_static_css()
        else:
            self._serve_404()

    def _serve_index(self):
        """Serve the index page listing all registered demos."""
        demos = self.registry.get_all()
        html = self.renderer.render_index(demos)
        self._send_html(200, html)

    def _serve_demo(self, name):
        """Serve a demo page for the given demo name.

        Looks up the demo module in the registry, executes it via the
        runner, and renders the result. Returns 404 if the demo is not found.

        Args:
            name: URL-safe demo name to look up.
        """
        module = self.registry.get_module(name)
        if module is None:
            self._serve_404()
            return

        # Get the title for this demo
        title = name
        for demo_name, demo_title in self.registry.get_all():
            if demo_name == name:
                title = demo_title
                break

        result = self.runner.execute(module)
        html = self.renderer.render_demo(title, result)
        self._send_html(200, html)

    def _serve_static_css(self):
        """Serve the static CSS stylesheet."""
        css_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "static",
            "style.css"
        )
        try:
            with open(css_path, "r") as f:
                css_content = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "text/css")
            self.end_headers()
            self.wfile.write(css_content.encode("utf-8"))
        except IOError:
            self._serve_404()

    def _serve_404(self):
        """Serve a 404 Not Found page."""
        html = self.renderer.render_404()
        self._send_html(404, html)

    def _send_html(self, status_code, html):
        """Send an HTML response with the given status code.

        Args:
            status_code: HTTP status code (e.g., 200, 404).
            html: HTML content string to send.
        """
        self.send_response(status_code)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def log_message(self, format, *args):
        """Log HTTP requests to stderr (default BaseHTTPRequestHandler behavior)."""
        super().log_message(format, *args)
