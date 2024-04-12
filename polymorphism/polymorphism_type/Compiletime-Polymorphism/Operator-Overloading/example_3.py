class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __pos__(self):
        xx = self.x
        yy = self.y
        if self.x < 0:
            xx = self.x * (-1)
        if self.y < 0:
            yy = self.y * (-1)

        return Point(xx, yy)

    def __invert__(self):
        return Point(self.y, self.x)

    # absolute value of a point is (x, y) means distance between (0, 0) and (x, y)
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

p1 = Point(2, -3)

print("Negation : ", -p1)
print("Position : ", +p1)
print("Inversion : ", ~p1)
print("Absolute value : ", abs(p1))