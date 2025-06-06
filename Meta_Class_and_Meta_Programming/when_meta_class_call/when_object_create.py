"""Bellow is a Special Case."""

"""
1. When an instance of the class is created, the metaclass controls how the class's __call__ method is invoked.
2. This stage is triggered when you create an object of a class using the class name, like MyClass().
3. If the metaclass defines the __call__ method (as in the Singleton pattern in your original code), it will be invoked during object creation.
4. The __call__ method is responsible for creating the instance by calling the __new__ and __init__ methods of the class.
"""

class Meta(type):
    def __call__(cls, *args, **kwargs):
        print(f"Creating Object of {cls.__name__}")

        print("Argument : ", args)
        print("KeyWord Argument : ", kwargs)

        # because __call__ method create and return an object
        return super().__call__(*args, **kwargs)

class MyClass(metaclass=Meta):
    def __init__(self, value):
        self.value = value

obj = MyClass(1400)
