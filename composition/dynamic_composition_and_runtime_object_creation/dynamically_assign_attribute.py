"""
Q : What means "Bind"?
--> Binding a function to an object means associating it with a specific instance, so it becomes a method of that instance.

Q : Difference between function and method ?
    1. Functions are standalone and don’t have access to an instance (no self by default).
    2. Methods are functions bound to an object, which automatically pass self as the first argument when called.

Q : Why use types.MethodType ?
--> When we use types.MethodType, we’re converting a standalone function into a method bound to a specific instance of a class. This binding enables the function to
access the instance’s attributes via self, just like any other method defined directly in the class.
"""

import types

class Car:
    def __init__(self, model):
        self.model = model

def add_feature(obj, name, value):
    if callable(value):
        value = types.MethodType(value, obj)
    setattr(obj, name, value)


def display_info(self):
    for key, value in self.__dict__.items():
        print(f'{key} : {value}')

def my_func(self):
    print("This is my function.")

def func():
    print("This is function.")

my_car = Car("Tesla Model S")
add_feature(my_car, "color", "Red")
add_feature(my_car, "battery", "100 kwh")
add_feature(my_car, 'display_info', display_info)

my_car.display_info()

setattr(my_car, 'func', func)
my_car.func()

# Todo: It show a error, TypeError: my_func() missing 1 required positional argument: 'self'
setattr(my_car, 'my_func', my_func)
my_car.my_func()
