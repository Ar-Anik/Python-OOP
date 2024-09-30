"""
Python follows a specific process to determine whether it should invoke the descriptor's __get__, __set__, or __delete__ methods when you interact with an attribute.
"""

"""
1. When Accessing an Attribute (__get__):
When you access an attribute (e.g., obj.attribute), Python checks if the attribute has a descriptor, and if so, it calls its __get__() method.

--> Here’s how it works:
Step 1: When we do obj.attribute, Python looks for the attribute in the instance's __dict__.
Step 2: If it doesn't find the attribute in the instance’s __dict__, it checks if the attribute is a descriptor by seeing if it has a __get__() method.
Step 3: If it finds that attribute is a descriptor, it calls the __get__() method on the descriptor.
"""

class DescriptorOne:
    def __get__(self, instance, owner):
        return "Value From __get__ Function."

class ClassOne:
    attribute = DescriptorOne()

obj = ClassOne()
print(obj.attribute)   # Internally calls __get__()

"""
when we do obj.attribute behind the scenes, Python does something like:

if hasattr(type(obj), 'attribute') and hasattr(type(obj).attribute, '__get__'):
    value = type(obj).attribute.__get__(obj, type(obj))

"""


"""
2. When Setting an Attribute (__set__):
When you assign a value to an attribute (e.g., obj.attribute = value), Python checks if the attribute has a descriptor, and if so, it calls its __set__() method.

---> Here’s the process:
    Step 1: When you do obj.attribute = value, Python first checks if attribute is a descriptor by seeing if it has a __set__() method.
    Step 2: If attribute has a __set__() method, Python calls __set__(self, obj, value) on the descriptor.
"""

class DescriptorTwo:
    def __set__(self, instance, value):
        print(f"Setting Attribute to {value}")

class ClassTwo:
    attribute = DescriptorTwo()

obj = ClassTwo()
obj.attribute = 10    # Internally calls __set__()

"""
when we do obj.attribute = 10, Behind the scenes Python does something like:

if hasattr(type(obj), 'attribute') and hasattr(type(obj).attribute, '__set__'):
    type(obj).attribute.__set__(obj, 10)

"""


"""
3. When Deleting an Attribute (__delete__):
When you delete an attribute (e.g., del obj.attribute), Python checks if the attribute has a descriptor, and if so, it calls its __delete__() method.

---> Here’s how it works:
    Step 1: When you do del obj.attribute, Python checks if attribute is a descriptor by seeing if it has a __delete__() method.
    Step 2: If it has a __delete__() method, Python calls __delete__(self, obj) on the descriptor.

"""

class DescriptorThree:
    def __delete__(self, instance):
        print("Attribute Deleted.")

class ClassThree:
    attribute = DescriptorThree()

obj = ClassThree()
del obj.attribute       # Internally calls __delete__().

"""
when we do `del obj.attribute`, Behind the scenes Python does something like:

if hasattr(type(obj), 'attribute') and hasattr(type(obj).attribute, '__delete__'):
    type(obj).attribute.__delete__(obj)

"""

"""
----> For data descriptors (those implementing both __get__ and __set__), Python always checks the class first for the descriptor. This is because data descriptors take precedence over instance variables.

----> For non-data descriptors (those only implementing __get__), Python checks the instance first, and if the attribute is not found there, it checks the class.
"""