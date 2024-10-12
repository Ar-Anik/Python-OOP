"""
Unbound Method: A function that belongs to a class but is not yet associated with an instance of the class. It's just a regular function.

In older versions of Python (before Python 3), an unbound method was a method object that is not bound to a class or instance. However, in Python 3 and later,
unbound methods do not exist as a separate category; they are just functions defined in a class, not associated with an instance. You can still call these methods
using the class itself by explicitly passing an instance as the first argument.
"""

class UnboundMethodClass:
    def method_1(self):
        print(f"This Method is call from the object {self}.")

class MyClass:
    pass

func = UnboundMethodClass.method_1

obj = MyClass()
func(obj)
