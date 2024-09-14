"""
In Python, <class 'object'> is the base class for all classes, meaning that all classes are derived from this class either directly or indirectly.
Even if you define a class without explicitly specifying a base class, it implicitly inherits from object. This is part of Python's design to ensure
that every object shares a common set of behaviors, such as methods for comparison, attribute access, and memory management.

Why is it needed?
1. Common behavior: By having all classes inherit from object, Python provides a consistent interface and functionality across all objects.
                    It ensures that basic methods like __str__(), __repr__(), __eq__(), and __hash__() are available to all objects.

2. Memory management: Python's object class is involved in memory allocation and garbage collection.

3. Inheritance hierarchy: It enables the inheritance mechanism, where classes can extend and override behavior, making it easier to
                          implement polymorphism and other object-oriented principles.
"""

# Basic inheritance from object : Though it's not strictly necessary because Python 3 does this implicitly.

class MyClass(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def display(self):
        return f"Name: {self.name}, Value: {self.value}"

my_object = MyClass("Item", 10)

print(my_object.display())
