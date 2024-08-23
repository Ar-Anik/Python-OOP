"""
Operator : Operator is a symbol or function. (+, -, AND, OR etc)
Operand : Value or Variable.
"""

# Polymorphism, in object-oriented programming, refers to the ability of a single interface to represent data or actions in various forms.

"""
In object-oriented programming (OOP), overloading refers to the ability to define multiple methods or functions with the same name but
with different parameters or different types of parameters within the same class or scope. This allows the same method name to be used
for different purposes depending on the context in which it's called.

For example, you might have a calculateArea method in a class that can calculate the area of different shapes. You could overload this method
to accept different types of parameters, such as calculateArea(int radius) for a circle or calculateArea(int length, int width) for a rectangle.

There are two Type of overloading :
    1. Operator Overloading.
    2. Method Overloading.
"""

"""
Two Type of Polymorphism :
    1. Compile-time Polymorphism (Static Polymorphism)
    2. Runtime Polymorphism (Dynamic Polymorphism)
"""

# Suppose we want add two value for this there are several steps Python needs to do.
# Operation Like :
a = 7
b = 6
c = a + b

"""
Step are :
    1. Check the types of both operands
    2. Check whether they both support the + operation
    3. Extract the function that performs the + operation (due to operatoroverloading objects can have a custom definition for addition)
    4. Extract the actual values of the objects
    5. Perform the + operation
    6. Construct a new integer object for the result
"""