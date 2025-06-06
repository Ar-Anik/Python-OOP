"""
The singleton pattern is a design pattern that ensures a class has only one instance and provides a global point of access to that instance.
This pattern is useful when exactly one object is needed to coordinate actions across the system, such as a single configuration manager, logging service, or connection pool.

Key Characteristics of the Singleton Pattern:
    1. Single Instance: Only one instance of the class is created. Any subsequent requests for an instance will return the same object.
    2. Global Access Point: The single instance can be accessed globally, ensuring that there is a consistent point of access.
"""


"""
When you create an instance of a class, like this:
    my_instance = MyClass()

1. Python internally invokes the __call__() method of the metaclass of MyClass (which is type by default).
2. The __call__() method is responsible for the creation of the instance by:
    # Calling __new__(): The __call__() method first calls the __new__() method of the class to create a new instance.
    # Calling __init__(): After the instance is created, the __call__() method then calls the __init__() method to initialize the instance.
"""

class SingletnMeta(type):
    _instances = {}
    print("This is print.")

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]

"""
1. SingletonBase is created using the SingletnMeta metaclass. The metaclass controls how the SingletonBase class itself (and any subclasses like A or B) is created.

2. The __call__ method defined in SingletnMeta is invoked whenever you try to create an instance of A or B. This method ensures that the singleton instance for each 
class is created only once and is reused for subsequent instantiations.
"""

"""
1. Defining SingletnMeta:
    # When the Python interpreter first encounters the definition of SingletnMeta, the code inside the metaclass body (such as the print("This is print.") statement) 
      is executed immediately during the definition of the metaclass itself.
    # This means "This is print." will be printed only once, at the time the metaclass SingletnMeta is defined.

2. Creating SingletonBase with the Metaclass:
    # When SingletonBase is defined as class SingletonBase(metaclass=SingletnMeta), the following happens:
        The __new__ method of the metaclass is called (if defined). This is where the actual creation of the SingletonBase class object happens.
        The __init__ method of the metaclass is called to initialize the SingletonBase class object.
        
    # Since SingletnMeta inherits from type, if you don't define __new__ or __init__ explicitly, the default behavior from type is used, which creates and initializes the class as usual.
        
    # At this stage, SingletonBase becomes a class that is governed by the SingletnMeta metaclass.
    
3. The __call__ method of SingletnMeta is NOT called at this point:
    # The __call__ method in SingletnMeta will not be executed during the creation of SingletonBase. It will only be executed later when you try to instantiate objects of the subclasses (A or B).
    # The __call__ method in SingletnMeta is responsible for intercepting object creation (A(10) or B(30)), and it will only be triggered during instance creation, not class definition.
"""

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