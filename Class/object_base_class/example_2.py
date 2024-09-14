class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    # Overriding __eq__ to compare two points based on coordinates
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y

        return False

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(2, 3)

print(p1)

print(p1 == p2)
print(p1 == p3)
