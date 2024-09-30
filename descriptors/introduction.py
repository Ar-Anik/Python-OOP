"""
Learning Link : https://developer.ibm.com/tutorials/os-pythondescriptors/
"""

"""
Topic which must be learn : 
1. Descriptor Protocol:
    # __get__, __set__, and __delete__ methods
    # How these methods are invoked during attribute access

2.Descriptor Types:
    # Data descriptors vs. non-data descriptors
    # Their behavior and precedence in attribute lookup

3. Descriptor Use Cases:
    # Property implementation
    # Method binding
    # Lazy evaluation
    # Attribute validation

4. Descriptor Lifecycle:
    # When descriptors are created and how they're bound to classes

5. Descriptor Performance:
    # Overhead compared to regular attributes
    # Caching strategies for optimization

6. Common Patterns:
    # Descriptor factories
    # Descriptors with __slots__

7. Interaction with Other Python Features:
    # Descriptors in inheritance hierarchies
    # Descriptors with metaclasses
"""


"""
# Descriptors Definitions  :
 
-----> A Python descriptor is a way to customize the behavior of attribute access in objects (classes). It lets you define what happens when an attribute is
retrieved, set, or deleted on an object. This is done by defining special methods inside a class: __get__, __set__, and __delete__.


-----> Python descriptors are a way to create managed attributes. Among their many advantages, managed attributes are used to protect an attribute from changes 
or to automatically update the values of a dependant attribute.
"""

"""
More Simplified Descriptors : 

1. A Descriptor as a Controller for Attributes : A descriptor is like a "manager" for attributes. When you access, assign, or delete an attribute in instance 
of a class, instead of Python directly handling it, the descriptor takes control and defines exactly how the attribute should behave.

2. A Descriptor as a Rule Setter for Variables: Think of a descriptor as a set of rules for handling variables in a class. When a variable (attribute) is 
accessed or changed, the descriptor applies these rules (which you define in __get__, __set__, or __delete__ methods).

3. A Descriptor as a Custom Getter/Setter: A descriptor allows you to customize what happens when you "get" (retrieve) or "set" (assign) a value to a class 
attribute. It’s similar to getter and setter methods in object-oriented programming but more flexible and automatic.
"""

"""
Diffenence Between Normal Attribute and Descriptor Attribute : 
1. Normal Attribute: Accessing or changing it just gets or sets the value directly.
2. Descriptor Attribute: Accessing or changing it calls the descriptor's methods to control what happens.
"""

"""
Descriptor Protocol : 
-----> The descriptor protocol is a set of methods in Python that allow objects (descriptors) to customize the behavior of attribute access (getting, setting, 
or deleting). It defines how Python should interact with a descriptor when attributes of a class are accessed, assigned, or deleted.

-----> Python descriptor protocol is simply a way to specify what happens when an attribute is referenced on a python object. It allows a programmer to easily 
and efficiently manage attribute access.

# The descriptor protocol consists of three special methods:

1. __get__(self, instance, owner/type): This method is called when an attribute is accessed. It defines how to retrieve the value of the attribute.

Parameters:
    # self: The descriptor instance.
    # instance: The instance of the class (e.g., obj) that is calling the attribute, or None if it’s being accessed through the class.
    # owner/type: The class (e.g., MyClass) where the descriptor is defined.
Returns: The value that should be returned when the attribute is accessed.

2. __set__(self, instance, value): This method is called when an attribute is assigned a value. It defines how to handle setting the value of the attribute.

Parameters:
    # self: The descriptor instance.
    # instance: The instance of the class where the attribute is being set.
    # value: The value being assigned to the attribute.
Returns: Nothing

3. __delete__(self, instance): This method is called when an attribute is deleted. It defines how to handle the deletion of the attribute.

Parameters:
    # self: The descriptor instance.
    # instance: The instance of the class where the attribute is being deleted.
Returns: Nothing

"""

"""
##  How the Descriptor Protocol Works ?
 ---> When we access, assign, or delete an attribute that uses a descriptor, Python will call the descriptor protocol methods (__get__, __set__, or __delete__) 
 to handle that operation instead of doing it directly. The descriptor's methods are automatically invoked when working with attributes that are defined using 
 a descriptor object.
"""


class MyDescriptor:
    # part of the descriptor protocol to handle attribute access
    def __get__(self, instance, owner):
        print("Getting The Attribute.")
        return instance._value

    # part of the descriptor protocol to handle setting the attribute
    def __set__(self, instance, value):
        print(f"Setting The Attribute to {value}")
        instance._value = value

    # part of the descriptor protocol to handle deleting the attribute
    def __delete__(self, instance):
        print("Deleting The Attribute.")
        del instance._value

class MyClass:
    attribute = MyDescriptor()

# Usage Example
obj = MyClass()

# Setting the attribute by calls __set__
obj.attribute = 10

print("Dictionary Attribute of Object : ", obj.__dict__)

# Accessing the attribute by calls __get__
print(obj.attribute)

# Deleting the attribute by calls __delete__
del obj.attribute

"""
1. Why Use _value as a Protected Attribute?
Instance._value is used to store the actual value of the attribute that is being controlled by the descriptor. The reason for using _value (or a similarly named attribute) is:
    1. Encapsulation: The underscore (_) in Python is a convention that denotes a protected attribute. It implies that the attribute is meant for internal use and should not be accessed directly 
                      outside of the class.

    2. Avoid Name Collisions: If we directly used instance.attribute, we'd enter an infinite loop because accessing instance.attribute would trigger the descriptor again. So, we store the actual 
                             value in another attribute (_value) to avoid this recursion.
"""

"""
2. How Does Python Understand attribute = _value?
Python differentiates the attribute attribute (controlled by the descriptor) and the internal attribute _value (where the actual value is stored) by:
    1. The descriptor is controlling attribute, and when __get__, __set__, or __delete__ are called, these methods decide how to handle the attribute.
    2. The descriptor doesn’t directly store the value. Instead, it manages access to an internal attribute (_value in this case), which is stored in the instance.__dict__.
"""