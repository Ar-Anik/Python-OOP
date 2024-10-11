"""
If an instance has an attribute with the same name, the descriptor will override the instance attribute when accessing or modifying the value. This is because
Python always checks the class first for data descriptors, and data descriptors take precedence over instance variables.
"""

class DataDescriptor:
    def __get__(self, instance, owner):
        print("Accessing Through DataDescriptor.")
        return instance.__dict__.get('attr', "No Value set in instance.")

    def __set__(self, instance, value):
        print("Setting Through DataDescriptor.")
        instance.__dict__['attr'] = value

class Example:
    attr = DataDescriptor()

obj = Example()

# Set and Get Attribute Value through the descriptor.
obj.attr = 42
print(obj.attr)

# Manually setting instance attribute
obj.__dict__['attr'] = 100
print(obj.attr)

"""
In this example, even though obj.__dict__['attr'] = 100 directly sets the instance attribute, accessing obj.attr will still go through the data descriptor's __get__ method.
"""