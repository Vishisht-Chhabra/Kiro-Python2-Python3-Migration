# Python 2 Feature Demos

A small Python 2.7 web application that demonstrates Python 2 language features in the browser. Each demo shows the source code of a Python 2 idiom alongside its captured runtime output, so you can see both the syntax and the behavior.

## What's inside

13 demo modules, each focused on one Python 2 feature category:

| Demo | Python 2 feature |
|------|------------------|
| Print Statement | `print "x"`, comma-separated values, trailing comma, `>>` redirect |
| Integer Division | Classic division: `5 / 2 == 2`, `/` vs `//`, mixed int/float operands |
| Unicode Handling | `str` vs `unicode`, `u""` literals, encode/decode |
| Range and Xrange | `range()` returns a list, `xrange()` returns a lazy iterator |
| Dictionary Methods | `keys()` / `values()` / `items()` return lists, `has_key()`, `iter*()` |
| User Input | `raw_input()` for strings, `input()` evaluates expressions |
| Exec Statement | `exec` as a statement, with explicit globals / locals |
| String Formatting | `%`-style formatting, named placeholders, `string.Template` |
| Exception Syntax | `except E, e:`, `raise E, "msg"`, three-arg `raise`, `StandardError` |
| Numeric Types | `L` suffix, `long()`, octal `0755`, `<>` operator, `cmp()` |
| Iterators / Functional | `.next()`, `reduce`, `apply`, `map` / `filter` lists, backtick repr |
| Classes and Objects | Old-style and new-style classes, `__metaclass__`, `__cmp__`, unbound methods |
| Module Imports | `StringIO`, `urllib2`, `ConfigParser`, implicit relative imports |

## Architecture

```
Browser ──HTTP──▶ BaseHTTPServer ──▶ Registry ──▶ Demo module
                                  └─▶ Runner   (captures stdout)
                                  └─▶ Renderer (HTML output)
```

- `main.py` — entry point, registers all demos and starts the server
- `server.py` — `BaseHTTPServer` request handler with routes for `/`, `/demo/<name>`, `/static/style.css`
- `registry.py` — maps URL-safe names to demo modules
- `runner.py` — executes a demo's `run()` function, redirects stdout to `StringIO`, captures errors
- `renderer.py` — generates the HTML pages (uses `cgi.escape` for entity safety)
- `demos/` — the 13 demo modules, each exposing a `run()` function
- `static/style.css` — page styling
- `tests/` — unit, property-based (hypothesis), and integration tests

Zero runtime dependencies beyond the Python 2.7 stdlib.

## Requirements

- Either Docker (recommended on modern macOS / Linux), or
- Python 2.7 installed natively
- For tests: `pytest` and `hypothesis==3.56.0` (installed automatically via the Docker test command below)

---

## Quick start

All commands below assume your terminal is **inside the `Kiro-Python2/` directory**:

```bash
cd Kiro-Python2
```

### Start the application

#### Using Docker (recommended)

```bash
docker run --rm --name python2-demo-app \
  -v "$(pwd):/app" -w /app \
  -p 8080:8080 python:2.7-slim python -u main.py
```

Then open **http://localhost:8080/** in your browser.

Press `Ctrl+C` to stop the server.

**If port 8080 is already in use**, map a different host port (left side is your host, right side is the container):

```bash
docker run --rm --name python2-demo-app \
  -v "$(pwd):/app" -w /app \
  -p 8090:8080 python:2.7-slim python -u main.py
```

Then open **http://localhost:8090/**.

**To run in the background** (detached mode):

```bash
docker run -d --name python2-demo-app \
  -v "$(pwd):/app" -w /app \
  -p 8080:8080 python:2.7-slim python -u main.py

docker logs -f python2-demo-app   # follow logs
docker rm -f python2-demo-app     # stop and remove the container
```

#### Using native Python 2.7

If Python 2.7 is installed locally:

```bash
python main.py            # default port 8080
python main.py 9000       # custom port
```

Then open **http://localhost:8080/** (or your custom port). Press `Ctrl+C` to stop.

### Run the tests

The test suite has **22 tests** across three categories:

- 13 unit tests — verify each demo's captured output
- 2 property-based tests (hypothesis) — verify index and demo page rendering invariants
- 6 integration tests — start the server in a thread and exercise the HTTP routes

#### Using Docker

```bash
docker run --rm -v "$(pwd):/app" -w /app python:2.7-slim \
  sh -c "pip install pytest 'hypothesis==3.56.0' && python -m pytest tests/ -v"
```

#### Using native Python 2.7

```bash
pip install pytest 'hypothesis==3.56.0'
python -m pytest tests/ -v
```

> Hypothesis 3.56.0 is pinned because newer 3.x releases are incompatible with the `typing` shim that pip installs alongside them on Python 2.7.

Expected output (last line):

```
========================== 22 passed in 3.58 seconds ===========================
```

To run a single test file or a single test:

```bash
python -m pytest tests/test_demos.py -v
python -m pytest tests/test_demos.py::test_print_statement_demo -v
```

---

## Project layout

```
Kiro-Python2/
├── README.md                     # This file
├── main.py                       # Entry point
├── server.py                     # HTTP request handler
├── registry.py                   # Demo registry
├── runner.py                     # Executes demos, captures stdout
├── renderer.py                   # HTML page generation
├── static/
│   └── style.css
├── demos/
│   ├── __init__.py
│   ├── print_statement.py
│   ├── integer_division.py
│   ├── unicode_handling.py
│   ├── range_xrange.py
│   ├── dict_methods.py
│   ├── user_input.py
│   ├── exec_statement.py
│   ├── string_formatting.py
│   ├── exception_syntax.py
│   ├── numeric_types.py
│   ├── iterators_functional.py
│   ├── classes_objects.py
│   └── module_imports.py
└── tests/
    ├── __init__.py
    ├── conftest.py
    ├── test_demos.py             # 13 unit tests
    ├── test_property_index.py    # Property 1 (hypothesis)
    ├── test_property_demo.py     # Property 2 (hypothesis)
    └── test_integration.py       # 6 integration tests
```

## Adding a new demo

1. Create `demos/your_feature.py` with a `run()` function that prints to stdout.
2. Register it in `main.py`:
   ```python
   from demos import your_feature
   registry.register("your_feature", "Your Feature Title", your_feature)
   ```
3. Restart the server and visit `/demo/your_feature`.

## Notes

- All code in `demos/` uses Python 2.7 syntax. The application requires Python 2.7 to run.
- The runner captures `stdout` only. If a demo writes to `stderr` directly, that output won't appear on the page (the print statement demo redirects stderr to a `StringIO` buffer to make it visible).
- Errors raised inside a demo's `run()` are caught and rendered as an error block on the page; the server keeps serving.

## Troubleshooting

**`Bind for 0.0.0.0:8080 failed: port is already allocated`**
Another process is using port 8080. Either stop it, or map a different host port (e.g. `-p 8090:8080`) and visit that port instead.

**`Cannot connect to the Docker daemon`**
Docker isn't running. On macOS with colima: `colima start`. On macOS with Docker Desktop: open the Docker Desktop app.

**`docker: Error response from daemon: Conflict. The container name "/python2-demo-app" is already in use`**
A previous container with that name is still around. Remove it: `docker rm -f python2-demo-app` and re-run.
