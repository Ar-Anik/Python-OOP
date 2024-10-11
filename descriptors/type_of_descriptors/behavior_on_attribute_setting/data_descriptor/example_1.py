"""
If we set an instance attribute with the same name as the descriptor, the descriptor's behavior will take precedence.
"""

# Example of Data-Descriptor
class DataDescriptor:
    def __get__(self, instance, owner):
        print("Call Get Method.")
        return instance._value

    def __set__(self, instance, value):
        print("Call Set Method.")
        instance._value = value

class Example:
    attr = DataDescriptor()

obj = Example()

obj.attr = 100
print(obj.attr)

print("Before Instance Attribute Assign : ", obj.__dict__)

obj.__dict__['attr'] = 50
print(obj.attr)

print("After Instance Attribute Assign : ", obj.__dict__)
