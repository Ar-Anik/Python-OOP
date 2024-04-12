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

