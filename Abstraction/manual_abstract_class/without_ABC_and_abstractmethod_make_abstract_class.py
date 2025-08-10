"""
> Create a base class that acts like an abstract class by raising NotImplementedError in methods that subclasses
are expected to override.
"""

class Shape:
    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement calculate_area method")

    def calculate_perimeter(self):
        raise NotImplementedError("Subclasses must implement calculate_perimeter method")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(4, 5)
print(rectangle.calculate_area())

shape = Shape()
shape.calculate_area()

"""
> Without using ABC and @abstractmethod, Python will not prevent instantiation of the base class.

> When we define a method in a base class that raises NotImplementedError, it's just a normal method that 
raises an error if called. It doesn't force subclasses to implement it. Therefore, our code works until 
we call the missing method.

> we rely on runtime errors, not compile-time enforcement. This approach works, but it’s less clean, safe 
and self-documenting.
"""

"""
Q : When Is This Useful?
> When we want to avoid dependencies on abc.
> For simpler codebases or dynamic situations where we handle enforcement manually.
> When we want maximum flexibility at the cost of strict rules.
"""

