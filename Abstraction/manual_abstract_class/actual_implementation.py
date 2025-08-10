class Shape:
    def __init__(self):
        if type(self) is Shape:
            raise TypeError("Cannot instantiate abstract class Shape directly")

        required_method = ['calculate_area', 'calculate_perimeter']
        for method in required_method:
            subclass_method = getattr(self.__class__, method, None)
            base_method = getattr(Shape, method, None)
            if subclass_method is base_method:
                raise NotImplementedError(f"Subclasses must implement {method}() method.")

    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement calculate_area method")

    def calculate_perimeter(self):
        raise NotImplementedError("Subclasses must implement calculate_perimeter method")


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def calculate_area(self):
        return 3.14 * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
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
