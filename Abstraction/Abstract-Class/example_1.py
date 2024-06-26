from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        return f"This is a {self.__class__.__name__}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def __str__(self):
        try:
            return f"Circle Area : {self.area()}, Circle Perimeter : {self.perimeter()}"
        except Exception as e:
            return str(e)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

    def __str__(self):
        try:
            return f"Square Area : {self.area()}, Square Perimeter : {self.perimeter()}"
        except Exception as e:
            return str(e)

circle = Circle(5)
square = Square(4)

print(circle)
print(square)

print(circle.describe())
print(square.describe())
