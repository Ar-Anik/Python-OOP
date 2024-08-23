# Operator overloading is a programming technique that allows custom classes to redefine the behavior of built-in operators
# (such as +, -, *, /, ==, !=, <, >, etc.) so that they work with objects of those classes.

# Operator overloading is a powerful feature in many programming languages that allows you to redefine the behavior of operators,
# such as +, -, *, /, and others, for user-defined types.

# Operator Overloading for a class, and overloading operator work only of that class object.

class Addplus:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if type(self.value) == str or type(other.value) == str:
            return str(self.value) + str(other.value)
        else:
            return self.value + other.value

a = Addplus(3)
b = Addplus('anik')
c = Addplus(5)
print(a+b)
print(a+c)

"""
1. When a + b is executed, Python first checks whether the Addplus class (the class of a) has an __add__ method defined.
2. If the __add__ method is defined in the Addplus class, Python will call a.__add__(b), using the logic you've provided in that method.
3. If the __add__ method is not defined in the Addplus class (or its parent classes, if any), Python will attempt to use the default behavior. The default __add__ method in Python is not 
   typically defined for custom objects unless explicitly provided, so if Addplus did not have an __add__ method, Python would raise a TypeError saying that the + operation is unsupported 
   for Addplus instances.
"""