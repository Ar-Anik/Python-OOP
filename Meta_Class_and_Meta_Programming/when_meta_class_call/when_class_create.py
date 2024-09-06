"""
1. The metaclass is used when the class itself is defined or created.
2. This happens when the Python interpreter encounters the class statement or uses the type() function to dynamically create a class.
3. The metaclass’s __new__ and __init__ methods can be overridden to customize the behavior of class creation.
4. When an object or class is created, Python first calls __new__ to create the object (allocate memory).
5. Once __new__ has created the object and returned it, Python automatically calls __init__ on the newly created object to initialize its attributes.
"""

class Meta(type):
    """
        cls: The class object itself (for example, MyClass).
        name: The name of the class (MyClass).
        bases: A tuple containing base classes (in this case, it's empty).
        dct: A dictionary containing the class attributes and methods, such as __init__.
    """
    def __new__(cls, name, bases, dct):
        print("Class Use : ", cls)
        print("Class Name : ", name)
        print("Class Dict : ", dct)

        # because it return new class object
        return super().__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print("Class Use : ", cls)
        print("Class Name : ", name)
        print("Class Dict : ", dct)

        # Adding a class attribute
        cls.class_attr = "This is a class Attribute"

        # Adding a class method
        @classmethod
        def class_method(cls):
            print(f"Class Method called in {cls.__name__}")

        cls.class_method = class_method

        # Initializing a normal method
        def instance_method(self):
            print(f"Instance method called with value : {self.value}")

        cls.instance_method = instance_method

        super().__init__(name, bases, dct)


class MyClass(metaclass=Meta):
    __author__ = "aubdur rob anik"

    def __init__(self, value):
        self.value = value


obj = MyClass(13)
print(obj.class_attr)
obj.class_method()
obj.instance_method()
