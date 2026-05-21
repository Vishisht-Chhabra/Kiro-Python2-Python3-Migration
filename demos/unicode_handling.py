"""Unicode Handling Demonstration - Python 2 vs Python 3.

Python 3 unifies the text model around two distinct string types:

  - ``str``   - text (Unicode code points)
  - ``bytes`` - immutable sequences of 8-bit bytes

Python 2 had a different and more confusing split:

    type("hello")    -> <type 'str'>      # bytes (8-bit string)
    type(u"hello")   -> <type 'unicode'>  # text  (Unicode string)
    basestring                            # common base of str and unicode

In Python 3:

    type("hello")    -> <class 'str'>     # text (what Py2 called unicode)
    type(b"hello")   -> <class 'bytes'>   # binary (what Py2 called str)
    unicode          -> removed; use str
    basestring       -> removed; use isinstance(x, (str, bytes))

The ``u"..."`` prefix is still legal in Python 3 (PEP 414) but is now just an
alias for a regular ``str`` literal, so both ``"hello"`` and ``u"hello"`` are
``str`` objects.
"""


def run():
    """Demonstrate the Python 3 str / bytes string model."""

    print("=== Python 3 Unicode Handling Demo ===")
    print("")

    # str (text) vs bytes (binary): the two Python 3 string types.
    # Python 2 form (different meaning):
    #     byte_string    = "hello"   # type 'str'      (bytes)
    #     unicode_string = u"hello"  # type 'unicode'  (text)
    print("--- str (text) vs bytes (binary) ---")
    text_string = "hello"
    byte_string = b"hello"
    print('text_string = "hello"')
    print('byte_string = b"hello"')
    print("type(text_string):", type(text_string))
    print("type(byte_string):", type(byte_string))
    print("type('hello') is str:", type("hello") is str)
    print("type(b'hello') is bytes:", type(b"hello") is bytes)
    print("")

    # In Python 3 the u"..." prefix is preserved for compatibility but
    # produces a regular str (PEP 414).
    print('--- Unicode literal prefix u"" (still allowed; produces str) ---')
    greeting = u"Bonjour"
    emoji_text = u"\u2603 Snowman"
    print('u"Bonjour" ->', greeting, "type:", type(greeting))
    print('u"\\u2603 Snowman" ->', emoji_text, "type:", type(emoji_text))
    print("type(u'hello') is str:", type(u"hello") is str)
    print("")

    # Encoding (str -> bytes) and decoding (bytes -> str)
    # In Python 3 encode() always returns bytes and decode() always returns str.
    print("--- Encoding and Decoding ---")
    original = "caf\u00e9"
    print('original = "caf\\u00e9" ->', original)
    print("type(original):", type(original))
    encoded = original.encode("utf-8")
    print("encoded = original.encode('utf-8') ->", repr(encoded))
    print("type(encoded):", type(encoded))
    print("isinstance(encoded, bytes):", isinstance(encoded, bytes))
    decoded = encoded.decode("utf-8")
    print("decoded = encoded.decode('utf-8') ->", decoded)
    print("type(decoded):", type(decoded))
    print("isinstance(decoded, str):", isinstance(decoded, str))
    print("")

    # Type-check summary. Python 2's `unicode` and `basestring` no longer
    # exist; the Python 3 replacement for `basestring` is the tuple
    # `(str, bytes)` passed to isinstance().
    # Python 2 forms (now NameError in Python 3):
    #     isinstance(u'hello', unicode)
    #     isinstance('hello',  basestring)
    print("--- Type Differences Summary ---")
    print("type('hello')   ->", type("hello"))
    print("type(b'hello')  ->", type(b"hello"))
    print("isinstance('hello', str):       ", isinstance("hello", str))
    print("isinstance(b'hello', bytes):    ", isinstance(b"hello", bytes))
    print("isinstance('hello', bytes):     ", isinstance("hello", bytes))
    print("isinstance(b'hello', str):      ", isinstance(b"hello", str))
    # basestring is gone in Python 3. The idiomatic replacement is to test
    # for either of the two string-like types explicitly.
    print(
        "isinstance('hello',  (str, bytes)):",
        isinstance("hello", (str, bytes)),
    )
    print(
        "isinstance(b'hello', (str, bytes)):",
        isinstance(b"hello", (str, bytes)),
    )
    print("(Use isinstance(x, (str, bytes)) where Python 2 used basestring)")
