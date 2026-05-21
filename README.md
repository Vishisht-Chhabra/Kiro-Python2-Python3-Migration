# Python 2 → Python 3 Feature Demos

A Python 3 web application that demonstrates Python 3 idioms alongside their Python 2 predecessors. Each demo shows the source code of a Python 3 pattern alongside its captured runtime output, and each demo's docstring preserves the original Python 2 syntax for comparison.

## What's inside

13 demo modules, each focused on one Python 2 feature category and its Python 3 equivalent:

| Demo | Python 2 feature | Python 3 equivalent |
|------|------------------|---------------------|
| Print Statement | `print "x"`, comma-separated values, trailing comma, `>>` redirect | `print()` function with `sep`, `end`, `file` kwargs |
| Integer Division | Classic division: `5 / 2 == 2`, `/` vs `//`, mixed int/float operands | True division: `5 / 2 == 2.5`, `//` for floor |
| Unicode Handling | `str` vs `unicode`, `u""` literals, encode/decode | `str` (text) vs `bytes`, unified string model |
| Range and Xrange | `range()` returns a list, `xrange()` returns a lazy iterator | `range()` is lazy (subsumes `xrange`) |
| Dictionary Methods | `keys()` / `values()` / `items()` return lists, `has_key()`, `iter*()` | View objects, `k in d` replaces `has_key()` |
| User Input | `raw_input()` for strings, `input()` evaluates expressions | `input()` returns str, `eval(input())` for eval |
| Exec Statement | `exec` as a statement, with explicit globals / locals | `exec()` function call |
| String Formatting | `%`-style formatting, named placeholders, `string.Template` | `str.format()`, f-strings, plus legacy `%` |
| Exception Syntax | `except E, e:`, `raise E, "msg"`, three-arg `raise`, `StandardError` | `except E as e:`, `raise E("msg")`, `.with_traceback()` |
| Numeric Types | `L` suffix, `long()`, octal `0755`, `<>` operator, `cmp()` | Unified `int`, `0o755` octal, `!=`, `(a>b)-(a<b)` |
| Iterators / Functional | `.next()`, `reduce`, `apply`, `map` / `filter` lists, backtick repr | `next()`, `functools.reduce`, `*args`, lazy iterators |
| Classes and Objects | Old-style and new-style classes, `__metaclass__`, `__cmp__`, unbound methods | All new-style, `metaclass=`, rich comparisons |
| Module Imports | `StringIO`, `urllib2`, `ConfigParser`, implicit relative imports | `io`, `urllib.request`, `configparser`, explicit relative |

## Architecture

```
Browser ──HTTP──▶ http.server ──▶ Registry ──▶ Demo module
                               └─▶ Runner   (captures stdout)
                               └─▶ Renderer (HTML output)
```

- `main.py` — entry point, registers all demos and starts the server
- `server.py` — `http.server` request handler with routes for `/`, `/demo/<name>`, `/static/style.css`
- `registry.py` — maps URL-safe names to demo modules
- `runner.py` — executes a demo's `run()` function, redirects stdout to `io.StringIO`, captures errors
- `renderer.py` — generates the HTML pages (uses `html.escape` for entity safety)
- `demos/` — the 13 demo modules, each exposing a `run()` function
- `static/style.css` — page styling
- `tests/` — unit, property-based (hypothesis), and integration tests

Zero runtime dependencies beyond the Python 3.9+ stdlib.

## Requirements

- Either Docker (recommended on modern macOS / Linux), or
- Python 3.9 or newer installed natively
- For tests: install dependencies via `pip install -r requirements.txt`

---

## Quick start

All commands below assume your terminal is **inside the project directory**:

```bash
cd Kiro-Python2-Python3-Migrate
```

### Start the application

#### Using Docker (recommended)

```bash
docker run --rm --name python3-demo-app \
  -v "$(pwd):/app" -w /app \
  -p 8080:8080 python:3.11-slim python -u main.py
```

Then open **http://localhost:8080/** in your browser.

Press `Ctrl+C` to stop the server.

**If port 8080 is already in use**, map a different host port (left side is your host, right side is the container):

```bash
docker run --rm --name python3-demo-app \
  -v "$(pwd):/app" -w /app \
  -p 8090:8080 python:3.11-slim python -u main.py
```

Then open **http://localhost:8090/**.

**To run in the background** (detached mode):

```bash
docker run -d --name python3-demo-app \
  -v "$(pwd):/app" -w /app \
  -p 8080:8080 python:3.11-slim python -u main.py

docker logs -f python3-demo-app   # follow logs
docker rm -f python3-demo-app     # stop and remove the container
```

#### Using native Python 3

If Python 3.9+ is installed locally:

```bash
python main.py            # default port 8080
python main.py 9000       # custom port
```

Then open **http://localhost:8080/** (or your custom port). Press `Ctrl+C` to stop.

### Run the tests

The test suite has **24 tests** across three categories:

- 13 unit tests — verify each demo's captured output
- 5 property-based tests (hypothesis) — verify registry ordering, runner capture/restore, and page rendering invariants
- 6 integration tests — start the server in a thread and exercise the HTTP routes

#### Using Docker

```bash
docker run --rm -v "$(pwd):/app" -w /app python:3.11-slim \
  sh -c "pip install -r requirements.txt && python -m pytest tests/ -v"
```

#### Using native Python 3

```bash
pip install -r requirements.txt
python -m pytest tests/ -v
```

Expected output (last line):

```
========================== 24 passed ===========================
```

To run a single test file or a single test:

```bash
python -m pytest tests/test_demos.py -v
python -m pytest tests/test_demos.py::test_print_statement_demo -v
```

---

## Project layout

```
Kiro-Python2-Python3-Migrate/
├── README.md                     # This file
├── main.py                       # Entry point
├── server.py                     # HTTP request handler
├── registry.py                   # Demo registry
├── runner.py                     # Executes demos, captures stdout
├── renderer.py                   # HTML page generation
├── requirements.txt              # Test dependencies (pytest, hypothesis)
├── run_python3.sh                # Docker helper script
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
    ├── test_property_registry.py # Property 1 (hypothesis)
    ├── test_property_runner.py   # Property 2 (hypothesis)
    ├── test_property_index.py    # Property 3 (hypothesis)
    ├── test_property_demo.py     # Properties 4 & 5 (hypothesis)
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

- All code in `demos/` uses Python 3 syntax; each demo's docstring shows the original Python 2 form for comparison.
- The minimum supported interpreter is Python 3.9+.
- The runner captures `stdout` only. If a demo writes to `stderr` directly, that output won't appear on the page (the print statement demo redirects stderr to an `io.StringIO` buffer to make it visible).
- Errors raised inside a demo's `run()` are caught and rendered as an error block on the page; the server keeps serving.

## Troubleshooting

**`Bind for 0.0.0.0:8080 failed: port is already allocated`**
Another process is using port 8080. Either stop it, or map a different host port (e.g. `-p 8090:8080`) and visit that port instead.

**`Cannot connect to the Docker daemon`**
Docker isn't running. On macOS with colima: `colima start`. On macOS with Docker Desktop: open the Docker Desktop app.

**`docker: Error response from daemon: Conflict. The container name "/python3-demo-app" is already in use`**
A previous container with that name is still around. Remove it: `docker rm -f python3-demo-app` and re-run.
