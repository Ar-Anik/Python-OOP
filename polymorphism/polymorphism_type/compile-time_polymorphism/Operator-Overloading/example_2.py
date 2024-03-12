# here implement vector dot product

class Vector:
    def __init__(self, *components):
        self.components = components

    def __add__(self, other):
        if isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimension for addition")
            return Vector(*[a + b for a, b in zip(self.components, other.components)])
        else:
            raise TypeError("Unsupported Operand Type For +: Vector and {}".format(type(other)))

    def __sub__(self, other):
        if isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimension for subtraction")
            return Vector(*[a - b for a, b in zip(self.components, other.components)])
        else:
            raise TypeError("Unsupported Operand Type For -: Vector and {}".format(type(other)))

    def __mul__(self, other):
        if isinstance(other, (int, float, complex)):
            return Vector(*[a * other for a in self.components])
        elif isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimension for multiplication")
            return sum(a * b for a, b in zip(self.components, other.components))
        else:
            raise TypeError("Unsupported Operand Type For *: Vector and {}".format(type(other)))

    def __truediv__(self, other):
        if isinstance(other, (int, float, complex)):
            if other == 0:
                raise ValueError("Division By Zero")
            return Vector(*[a / other for a in self.components])
        else:
            raise TypeError("Unsupported Operand Type For /: Vector and {}".format(type(other)))

    def __str__(self):
        return "(" + ", ".join(str(comp) for comp in self.components) + ")"

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print("Real Vector Addition:", v1 + v2)
print("Real Vector Subtraction:", v1 - v2)
print("Real Vector Multiplication:", v1 * 2)
print("Real Vector Division:", v1 / 2)

cv1 = Vector(1+2j, 2-3j, 3+4j)
cv2 = Vector(4-5j, 5+6j, 6-7j)

print("Complex Vector Addition:", cv1 + cv2)
print("Complex Vector Subtraction:", cv1 - cv2)
print("Complex Vector Multiplication:", cv1 * 2)
print("Complex Vector Division:", cv1 / 2)

