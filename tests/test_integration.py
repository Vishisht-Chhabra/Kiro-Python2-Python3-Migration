"""Integration tests for the Python 2 demo web server.

Tests server startup, routing, and error handling using threading
and urllib2 to make HTTP requests.

Requirements: 1.1, 1.2, 1.3, 1.4, 1.5
"""

import sys
import os
import threading
import time
import urllib2
import BaseHTTPServer

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from registry import DemoRegistry
from runner import DemoRunner
from renderer import HtmlRenderer
from server import DemoRequestHandler
from demos import print_statement


def get_free_port():
    """Find a free port to use for testing."""
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))
    port = s.getsockname()[1]
    s.close()
    return port


def setup_server(port):
    """Set up and return a test server on the given port."""
    registry = DemoRegistry()
    runner = DemoRunner()
    renderer = HtmlRenderer()

    registry.register("print_statement", "Print Statement", print_statement)

    DemoRequestHandler.registry = registry
    DemoRequestHandler.runner = runner
    DemoRequestHandler.renderer = renderer

    server = BaseHTTPServer.HTTPServer(("", port), DemoRequestHandler)
    return server


def start_server_thread(server):
    """Start the server in a background thread."""
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()
    time.sleep(0.1)  # Give server time to start
    return thread


def test_server_starts_and_responds():
    """Test server starts and responds on configured port."""
    port = get_free_port()
    server = setup_server(port)
    start_server_thread(server)

    try:
        response = urllib2.urlopen("http://localhost:%d/" % port)
        assert response.getcode() == 200
    finally:
        server.shutdown()


def test_index_page_returns_200_with_demo_links():
    """Test GET / returns 200 with HTML containing demo links."""
    port = get_free_port()
    server = setup_server(port)
    start_server_thread(server)

    try:
        response = urllib2.urlopen("http://localhost:%d/" % port)
        assert response.getcode() == 200
        html = response.read()
        assert "/demo/print_statement" in html
        assert "Print Statement" in html
        assert "text/html" in response.info().get("Content-Type", "")
    finally:
        server.shutdown()


def test_demo_page_returns_200_with_source_and_output():
    """Test GET /demo/print_statement returns 200 with source and output."""
    port = get_free_port()
    server = setup_server(port)
    start_server_thread(server)

    try:
        response = urllib2.urlopen(
            "http://localhost:%d/demo/print_statement" % port
        )
        assert response.getcode() == 200
        html = response.read()
        # Should contain source code section
        assert "<pre><code>" in html
        # Should contain output section
        assert "Output" in html or "output" in html
        assert "def run():" in html
    finally:
        server.shutdown()


def test_static_css_returns_200():
    """Test GET /static/style.css returns 200 with CSS content."""
    port = get_free_port()
    server = setup_server(port)
    start_server_thread(server)

    try:
        response = urllib2.urlopen(
            "http://localhost:%d/static/style.css" % port
        )
        assert response.getcode() == 200
        content = response.read()
        assert "text/css" in response.info().get("Content-Type", "")
        # CSS file should have some styling content
        assert len(content) > 0
    finally:
        server.shutdown()


def test_nonexistent_path_returns_404():
    """Test GET /nonexistent returns 404 page."""
    port = get_free_port()
    server = setup_server(port)
    start_server_thread(server)

    try:
        urllib2.urlopen("http://localhost:%d/nonexistent" % port)
        assert False, "Expected HTTPError for 404"
    except urllib2.HTTPError as e:
        assert e.code == 404
        html = e.read()
        assert "404" in html or "Not Found" in html
    finally:
        server.shutdown()


def test_server_continues_after_demo_error():
    """Test server continues serving after a demo module error."""
    import types

    port = get_free_port()
    server = setup_server(port)

    # Register a broken demo module that raises an error
    broken_module = types.ModuleType("broken_demo")
    broken_module.__file__ = __file__

    def broken_run():
        raise RuntimeError("Intentional test error")

    broken_module.run = broken_run
    DemoRequestHandler.registry.register(
        "broken_demo", "Broken Demo", broken_module
    )

    start_server_thread(server)

    try:
        # Request the broken demo - should still return 200 with error info
        response = urllib2.urlopen(
            "http://localhost:%d/demo/broken_demo" % port
        )
        assert response.getcode() == 200
        html = response.read()
        assert "error" in html.lower() or "Error" in html

        # Server should still work after the error
        response = urllib2.urlopen("http://localhost:%d/" % port)
        assert response.getcode() == 200
    finally:
        server.shutdown()
