'''
In Python, an abstract property is a property within a class that is declared but not implemented in that class.
Instead, it must be implemented by any subclass derived from the class containing the abstract property.

To create an abstract property, you typically use the @property decorator along with the @abstractmethod decorator from the abc module.
'''

'''
1. An abstract property is a property declared in an abstract base class without an implementation.

2. Concrete subclasses must provide an implementation for all abstract properties defined in their parent abstract base class.

3. Abstract properties help enforce a consistent interface across subclasses and serve as a form of documentation.
'''

'''
Abstract properties are commonly used to define a common interface or behavior that subclasses must follow. 
They help enforce a contract between classes and facilitate polymorphism and code reuse in object-oriented programming.
'''

from abc import ABC, abstractmethod

class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14159 * self.radius ** 2

rectangle = Rectangle(5, 4)
print("Area of Rectangle : ", rectangle.area)

circle = Circle(3)
print("Area of Circle : ", circle.area)

#### Both Are Same ####

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14159 * self.radius ** 2

rectangle = Rectangle(6, 7)
print("Area of Rectangle : ", rectangle.area)

circle = Circle(4)
print("Area of Circle : ", circle.area)


'''
if i declare as a property in a abstract class then also use property decorator in subclass
'''