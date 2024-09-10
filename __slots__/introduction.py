"""
In Python Object-Oriented Programming (OOP), __slots__ is used to restrict the creation of instance attributes.
Normally, Python objects are stored in a dictionary (__dict__), which allows dynamic creation of attributes.
However, this can consume more memory because of the overhead of maintaining a dictionary for each object.

By defining __slots__, you tell Python to only allow a fixed set of attributes, which saves memory by preventing
the creation of __dict__ and uses a more memory-efficient internal structure.

Key Benefits of __slots__:
1. Memory Optimization: By avoiding the creation of a __dict__ for each instance.
2. Speed of Attribute Access: Since the attributes are stored in a more static manner, access to these attributes can be slightly
   faster compared to using the dynamic __dict__.
3. Restricting Attributes: Prevents dynamic attribute creation, which can catch some errors where attributes are misspelled.
"""

"""
In Python, by default, instances of classes store their attributes in a dynamic dictionary called __dict__. 
This allows new attributes to be added to instances at runtime but comes with overhead in memory and attribute 
access speed due to the use of a dictionary.

When you define __slots__ in a class, you are explicitly telling Python which attributes the object will have, 
and Python no longer needs to allocate a __dict__ for each instance. Instead, it uses a more memory-efficient 
internal structure (like a tuple or array) to store the defined attributes.
"""

# without __slots__
class Information:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Information('Anik', 14)
person.location = 'Bangladesh'

def write(self):
    for key, value in person.__dict__.items():
        print(f"{key} : {value}")
person.write = write

print(person.__dict__)


# with __slots__
# __slots__ is defined as a class-level variable, and it contains a list of attribute names that are allowed.
class WithSlots:
    __slots__ = ('name', 'age')     # Only these attributes are allowed

    # we can also write this way __slots__
    # __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = WithSlots("Aubdur Rob Anik", 18)
obj.location = "Bangldesh"      # This will raise an AttributeError, as 'location' is not allowed
