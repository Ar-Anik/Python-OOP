"""
-> The __call__ method in Python is a special (dunder) method that allows an object to be called like a
function. It can be used in regular classes and metaclasses, but the behavior and use-cases differ
slightly depending on where it's used.

-> In a regular class : implementing __call__ means instances of the class become callable objects, we can
do instance() as if it were a function.

class MyClass:
    def __call__(self, *args, **kwargs):
        pass

-> This is commonly used for:
    * Implementing function-like objects.
    * Building decorators.
    * Creating APIs with a natural syntax.
"""

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

double = Multiplier(2)
print(double(10))
