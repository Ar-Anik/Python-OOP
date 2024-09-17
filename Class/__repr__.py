"""
The __repr__(self) method in Python is a special method used to define the "official" string representation of an object. It's primarily used for debugging and development purposes.
The goal of __repr__ is to provide a string that ideally can be used to recreate the object, or at least provide a useful and unambiguous description of the object.

Here’s why you might use __repr__:

1. For Debugging: When you print an object or inspect it in a debugger, Python will call __repr__ to give you a string representation of the object.
                  This helps developers quickly understand the state of the object.

2. Unambiguous Representation: The output of __repr__ should be as unambiguous as possible, often including the class name and important attributes of the object.
                               This helps differentiate between objects of the same or different classes.

3. Recreate the Object: Ideally, the string returned by __repr__ should be a valid Python expression that could be used to recreate the object. While this isn't
                        always achievable, it's a useful goal when possible.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

p = Person("Anik", 14)

print(p)
print(p.__repr__())
print(repr(p))

"""
Without the __repr__ method, the default output would look something like <Person object at 0x...>, which is not as informative.
"""

"""
Key differences between __repr__ and __str__:
__repr__ : __repr__ is meant for developers, giving an unambiguous representation of the object.

__str__ : __str__ is meant for users, giving a more readable and informal string (used when print() is called).

# If __str__ isn’t defined, Python falls back to __repr__.
"""
