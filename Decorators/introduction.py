"""
Decorators are a way to modify the behavior of a function or a class without changing its source code. In the context of OOP, 
decorators can be used to add functionality to class methods or perform validation checks before executing a method.
"""

"""
A decorator in programming is a design pattern that allows behavior to be added to individual objects dynamically, 
without affecting the behavior of other objects from the same class. In Python, decorators are a powerful feature that 
allows you to modify or extend the behavior of functions or methods without changing their source code directly.

In Python, decorators are implemented using the @decorator_function syntax or using the @decorator_class syntax. 
They are typically used to modify the behavior of functions or methods by wrapping them with additional functionality.
"""

"""
Decorators are extensively used in frameworks like Flask and Django for tasks such as URL routing, authentication, and request handling.
"""

# Decarator Use Manually
def my_decorator(func):
    def wrapper():
        print("Do something Before function is Call.")
        func()
        print("Do something after function is Call.")

    return wrapper

def test():
    print("Hello World")

test = my_decorator(test)
print("After Decorate Manually Function Name : ", test.__name__)

test()

"""
test = my_decorator(test) equivalent to @my_decorator
"""

# Dacorator Use by syntax
def my_decorator1(method):
    def cover():
        print("You can do something before call function.")
        method()
        print("You can do something after call function.")

    return cover

@my_decorator1
def test1():
    print("Function with decorator.")

print("After Decorator Use function name : ", test1.__name__)

test1()
