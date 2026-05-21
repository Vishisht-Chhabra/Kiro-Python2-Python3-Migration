"""Classes and Objects Demonstration - Python 2 class syntax."""


def run():
    """Demonstrate Python 2 class syntax features."""

    print "=== Python 2 Classes & Objects Demo ==="
    print ""

    # Old-style class (without inheriting from object)
    print "--- Old-style class (no object inheritance) ---"

    class OldStyleAnimal:
        """An old-style class - does not inherit from object."""
        def __init__(self, name, sound):
            self.name = name
            self.sound = sound

        def speak(self):
            return "%s says %s" % (self.name, self.sound)

    cat = OldStyleAnimal("Cat", "Meow")
    print "OldStyleAnimal class (no 'object' parent):"
    print "  cat.speak() =", cat.speak()
    print "  type(cat) =", type(cat)
    print "  type(OldStyleAnimal) =", type(OldStyleAnimal)
    print ""

    # New-style class (inheriting from object)
    print "--- New-style class (inherits from object) ---"

    class NewStyleAnimal(object):
        """A new-style class - explicitly inherits from object."""
        def __init__(self, name, sound):
            self.name = name
            self.sound = sound

        def speak(self):
            return "%s says %s" % (self.name, self.sound)

    dog = NewStyleAnimal("Dog", "Woof")
    print "NewStyleAnimal(object) class:"
    print "  dog.speak() =", dog.speak()
    print "  type(dog) =", type(dog)
    print "  type(NewStyleAnimal) =", type(NewStyleAnimal)
    print ""

    # __metaclass__ class attribute syntax
    print "--- __metaclass__ class attribute syntax ---"

    class MyMeta(type):
        def __new__(mcs, name, bases, attrs):
            attrs['meta_created'] = True
            return super(MyMeta, mcs).__new__(mcs, name, bases, attrs)

    class MyClass:
        __metaclass__ = MyMeta
        value = 42

    print "class MyClass with __metaclass__ = MyMeta:"
    print "  MyClass.meta_created =", MyClass.meta_created
    print "  MyClass.value =", MyClass.value
    print "  type(MyClass) =", type(MyClass)
    print ""

    # __cmp__ method for custom comparison
    print "--- __cmp__ method for custom comparison ---"

    class Temperature(object):
        def __init__(self, degrees):
            self.degrees = degrees

        def __cmp__(self, other):
            return cmp(self.degrees, other.degrees)

        def __repr__(self):
            return "Temperature(%d)" % self.degrees

    hot = Temperature(100)
    warm = Temperature(75)
    cold = Temperature(32)

    print "Temperature objects with __cmp__:"
    print "  cmp(hot, cold) =", cmp(hot, cold)
    print "  cmp(cold, hot) =", cmp(cold, hot)
    print "  cmp(warm, warm) =", cmp(warm, warm)
    print "  sorted([hot, cold, warm]) =", sorted([hot, cold, warm])
    print ""

    # Unbound methods via class reference
    print "--- Unbound methods via class reference ---"

    class Greeter(object):
        def hello(self, name):
            return "Hello, %s!" % name

    # Accessing method through class gives an unbound method
    unbound = Greeter.hello
    print "Greeter.hello =", unbound
    print "  type:", type(unbound)

    # Must pass instance explicitly to call unbound method
    g = Greeter()
    result = Greeter.hello(g, "World")
    print "  Greeter.hello(g, 'World') =", result
