"""
A metaclass is a class whose instances are classes. In other words, while a class defines the behavior and structure of its instances (objects),
a metaclass defines the behavior and structure of its classes. Metaclasses are often used to customize class creation and behavior in Python.

Metaclasses are commonly used for:
1. Enforcing class-level constraints or policies.
2. Automatically adding or modifying methods or attributes of classes.
3. Implementing singleton patterns or other design patterns.
4. Implementing data validation or serialization logic.

In Python, a metaclass is a class whose instances are classes. Essentially, a metaclass defines the behavior and structure of other classes.
"""

class MyMeta(type):
    def __new__(cls, name, bases, dct):
        # Add a new attribute to the class being created
        dct['author_name'] = "Aubdur Rob Anik"

        # Create the class using the super metaclass (type)
        return super().__new__(cls, name, bases, dct)

class TestMeta(metaclass=MyMeta):
    pass

print(TestMeta.author_name)

# type class
"""
The type class in Python is a built-in metaclass for creating classes dynamically. We can access it directly in Python without any additional imports.

Here, MyMeta is being defined as a subclass of type, making it a metaclass. When you define a class like this, you're essentially saying that instances of 
MyMeta will be classes themselves, and they will have control over the creation and behavior of other classes.
"""

# Step By Step
"""
1. Class Definition Parsing: Python starts parsing the class definition TestMeta.

2. Collecting Class Attributes and Methods: Python collects all the attributes and methods defined in the class body and stores them in a dictionary (let's call it dct). In this case, dct is empty since there are no attributes or methods defined.

3. Metaclass Invocation:
    1. Python detects the metaclass=MyMeta argument in the class definition.
    2. Instead of using the default metaclass (type), Python uses MyMeta to create the class TestMeta.

4. Calling MyMeta.__new__:
    # The __new__ method of MyMeta is called with the following arguments:
        1. cls: The metaclass itself, which is MyMeta.
        2. name: The name of the class being created, which is 'TestMeta'.
        3. bases: A tuple containing the base classes of the new class, which is empty in this case (()).
        4. dct: The dictionary containing the class attributes and methods (in this case, it is {'__module__': '__main__', '__qualname__': 'TestMeta'}).
            
5. MyMeta.new Execution:
    1. cls is MyMeta.
    2. name is 'TestMeta'.
    3. bases is (), since TestMeta does not inherit from any other class.
    4. dct starts with {'__module__': '__main__', '__qualname__': 'TestMeta'}.
    
6. Modification in MyMeta.new:
    1. The __new__ method of MyMeta adds author_name to dct.
    2. Now, dct becomes {'__module__': '__main__', '__qualname__': 'TestMeta', 'author_name': 'Aubdur Rob Anik'}.
    
7. Class Creation:
    1. super().__new__(cls, name, bases, dct) is called, which is type.__new__ in this case.
    2. This creates the class TestMeta with the modified dct.

8. TestMeta Class:
    1. The class TestMeta is now created with author_name as one of its attributes.

9. Using the Class:
    1. When you access TestMeta.author_name, you get Aubdur Rob Anik.

"""
