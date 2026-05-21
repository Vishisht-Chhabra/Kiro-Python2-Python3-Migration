"""Unicode Handling Demonstration - Python 2 str vs unicode types."""


def run():
    """Demonstrate Python 2 str vs unicode type differences."""

    print "=== Python 2 Unicode Handling Demo ==="
    print ""

    # str vs unicode types
    print "--- str vs unicode types ---"
    byte_string = "hello"
    unicode_string = u"hello"
    print "byte_string = \"hello\""
    print "unicode_string = u\"hello\""
    print "type(byte_string):", type(byte_string)
    print "type(unicode_string):", type(unicode_string)
    print ""

    # u"" prefix for unicode literals
    print "--- Unicode literal prefix u\"\" ---"
    greeting = u"Bonjour"
    emoji_text = u"\u2603 Snowman"
    print "u\"Bonjour\" ->", greeting, "type:", type(greeting)
    print "u\"\\u2603 Snowman\" ->", emoji_text, "type:", type(emoji_text)
    print ""

    # Encoding and decoding
    print "--- Encoding and Decoding ---"
    original = u"caf\u00e9"
    print "original = u\"caf\\u00e9\" ->", original
    encoded = original.encode("utf-8")
    print "encoded = original.encode('utf-8') ->", repr(encoded)
    print "type(encoded):", type(encoded)
    decoded = encoded.decode("utf-8")
    print "decoded = encoded.decode('utf-8') ->", decoded
    print "type(decoded):", type(decoded)
    print ""

    # Type differences summary
    print "--- Type Differences Summary ---"
    print "type('hello') is", type("hello")
    print "type(u'hello') is", type(u"hello")
    print "isinstance('hello', str):", isinstance("hello", str)
    print "isinstance(u'hello', unicode):", isinstance(u"hello", unicode)
    print "isinstance(u'hello', basestring):", isinstance(u"hello", basestring)
    print "isinstance('hello', basestring):", isinstance("hello", basestring)
