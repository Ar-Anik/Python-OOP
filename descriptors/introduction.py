"""
Learning Link : https://developer.ibm.com/tutorials/os-pythondescriptors/
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
"""

