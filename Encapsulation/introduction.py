# https://www.geeksforgeeks.org/encapsulation-in-python/

"""
Encapsulation in Python refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit,
typically known as a class. It allows you to control the visibility of the internal state of an object and restrict access to certain parts of the code.

Encapsulation helps in achieving data hiding and abstraction. Data hiding means that the internal state of an object is not directly
accessible from outside the class, while abstraction means that the implementation details are hidden, and only the essential features
of an object are exposed.

In Python, encapsulation can be achieved using access modifiers such as:

1. Public: Variables and methods that are accessible from outside the class without any restrictions.

2. Protected: Variables and methods that are intended to be used within the class and its subclasses. Conventionally,
              these are prefixed with a single underscore (_), but the access is not restricted by the language itself.

3. Private: Variables and methods that are intended to be used only within the class where they are defined.
            Conventionally, these are prefixed with a double underscore (__), and their names are mangled to include
            the class name to prevent accidental access from outside the class.

"""

"""
What is mangling?

In Python, when you define a variable or method within a class with double underscores as a prefix (e.g., __variable or __method()), 
Python internally performs name mangling on these identifiers. Name mangling is a technique used to make the name of the variable or method 
unique within the class to prevent accidental access or overriding from outside the class.

When Python encounters a double underscore prefix, it automatically modifies the name of the variable or method by adding the class name 
as a prefix and underscores. This modification ensures that the variable or method becomes unique to the class where it's defined.

For example, if you define a variable __private_var within a class named MyClass, Python will mangle the name to something like _MyClass__private_var. 
Similarly, a method named __private_method() will be mangled to _MyClass__private_method().

This name mangling mechanism effectively makes it difficult for external code to access or override these variables and methods unintentionally. 
However, it's worth noting that this mechanism does not make the variables or methods completely private, as they can still be accessed from outside 
the class using the mangled name, although it's discouraged and not considered good practice.

"""

# Example of Name Mangling
class Myclass:
    def __init__(self):
        self.__private_var = 10

    def __private_method(self):
        print("This is a Private Method")

obj = Myclass()

"""
It arise AttributeError: type object 'MyClass' has no attribute '__private_var'
print(obj.__private_var)
"""

"""
It arise AttributeError: type object 'MyClass' has no attribute '__private_method'
obj.__private_method()
"""

# Accessing the private variable using the mangled name
print(obj._Myclass__private_var)

# Calling the private method using the mangled name
obj._Myclass__private_method()

