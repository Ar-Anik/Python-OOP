'''
In Python, @property is a built-in decorator that allows you to define methods that can be accessed as attributes rather than as method calls.
It provides a way to encapsulate instance variables with accessor methods, known as getter and setter methods, to control access to the instance
variables and add additional behavior if needed.

Using @property, you can make an instance attribute act like a read-only attribute, a write-only attribute, or a read-write attribute, depending
on how you implement the getter, setter, and deleter methods.
'''

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    # The @radius.setter decorator is used to define a setter method for the radius property created using the @property decorator.
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius Can't Be Negative")
        self._radius = value

circle = Circle(5)

print(circle.radius)

circle.radius = 78
circle.radius = -1

print(circle.radius)

'''
Advantages of Property:

1. Encapsulation: Provides a way to encapsulate data by controlling the access to instance variables.

2. Validation: Allows you to add validation logic when setting values to ensure they meet certain criteria.

3. Readability: Makes the code more readable and provides a cleaner way to work with attributes.

'''

'''
Overall :

The @property decorator is a powerful tool in Python that allows you to implement getter, setter, and deleter methods for controlling 
access to instance variables, enhancing the encapsulation of your classes, and providing a more intuitive interface for working with objects.

'''

