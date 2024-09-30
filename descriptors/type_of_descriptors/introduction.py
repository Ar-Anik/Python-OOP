"""
In Python, there are two types of descriptors are data descriptors and non-data descriptors.
"""

"""
Data Descriptors : A data descriptor implements both __get__ and __set__ methods. It can control the attribute's access and modification.
"""

class DataDescriptor:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value

class DataExample:
    attr = DataDescriptor(42)

obj = DataExample()
print(obj.attr)
obj.attr = 10
print(obj.attr)


"""
Non-Data Descriptors :  A non-data descriptor implements only the __get__ method and does not have a __set__ method. It can control the attribute access but not its modification.
"""

class NonDataDescriptor:
    def __get__(self, instance, owner):
        return "Hello, World!"

class NonDataExample:
    attr = NonDataDescriptor()

obj = NonDataExample()
print(obj.attr)
obj.attr = 100
print(obj.attr)


"""
Differences Between Descriptor Types :
1. Access Control:
    # Data Descriptors: Can manage both getting and setting of values, making them versatile for mutable attributes.
    # Non-Data Descriptors: Allow only getting values, making them suitable for read-only attributes.
    
2. Functionality:
    # Data Descriptors: Used when we need to encapsulate logic for both accessing and modifying attribute values.
    # Non-Data Descriptors: Ideal for properties that should be computed or fetched but not modified directly.

3. Behavior on Attribute Setting:
    # Data Descriptors: If an instance has an attribute with the same name, the descriptor will override the instance attribute when accessing or modifying the value. This is because 
      Python always checks the class first for data descriptors, and data descriptors take precedence over instance variables.
    # Non-Data Descriptors: If an instance has an attribute with the same name, the instance attribute will override the descriptor. Python checks the instance for the attribute first, 
      and if the attribute is not found there, it checks the class for a descriptor.
"""
