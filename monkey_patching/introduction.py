# https://www.lambdatest.com/blog/monkey-patching-in-python/

"""
Monkey patching in Python is a technique where we dynamically modify or extend the behavior of classes or modules at runtime.
It's commonly used to change or add functionality in a class or module without altering its original source code Like Decorator.

--> Monkey patching is done by directly assigning a new function or attribute to a class or instance at runtime.
--> Monkey Patching Techniques : Attribute Overriding, Method Overriding.
"""

class Greeter:
    def greet(self):
        return "Hello Bangladesh"

greeter = Greeter()
print(greeter.greet())

def new_greet(self):
    return "Hi i am Aubdur Rob Anik"

Greeter.greet = new_greet    # Patching the method

print(greeter.greet())
