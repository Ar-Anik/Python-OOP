"""
The singleton pattern is a design pattern that ensures a class has only one instance and provides a global point of access to that instance.
This pattern is useful when exactly one object is needed to coordinate actions across the system, such as a single configuration manager, logging service, or connection pool.

Key Characteristics of the Singleton Pattern:
    1. Single Instance: Only one instance of the class is created. Any subsequent requests for an instance will return the same object.
    2. Global Access Point: The single instance can be accessed globally, ensuring that there is a consistent point of access.
"""

class SingletnMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]

class SingletonBase(metaclass=SingletnMeta):
    pass

class A(SingletonBase):
    def __init__(self, value):
        self.value = value

class B(SingletonBase):
    def __init__(self, value):
        self.value = value


a1 = A(10)
a2 = A(20)
b1 = B(30)
b2 = B(40)

print(a1.value)
print(a2.value)
print(b1.value)
print(b2.value)

"""
The super().__call__(*args, **kwargs) line calls the __call__ method of the superclass (type), which performs the standard instance creation process:
    1. Allocates memory for the new instance.
    2. Initializes the instance by calling its __init__ method with the provided arguments (*args and **kwargs).
    3. Returns the newly created instance.

When you create an instance of A or B, the following steps occur:
    1. When you write a1 = A(10), Python needs to create an instance of A.
    2. Python looks up the metaclass of A, which is SingletonMeta, and calls its __call__ method.
    3. The __call__ method of SingletonMeta is invoked with cls set to A and args and kwargs set to (10,) and {}, respectively.

"""