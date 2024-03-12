# Complex Number
# to add two complex number a+bi and c+di, add their real parts and imaginary parts separately, (a+bi)+(c+di)=(a+c)+(b+d)i
# to subtract one complex number from another, distribute the negative sign and then apply addition, (a+bi)−(c+di)=(a−c)+(b−d)i
# to multiply two cmplex number a+bi and c+di, use the distributive property and the fact that i^2 = -1, (a+bi)×(c+di)=(ac−bd)+(ad+bc)i
# divide two complex numbers a+bi and c+di, (a + bi) / (c + di) = (ac + bd) / (c^2 + d^2) + (bc - ad) / (c^2 + d^2)i

# a = self.real, b = self.imaginary, c = other.real, d = other.imaginary

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        return ComplexNumber((self.real * other.real - self.imaginary * other.imaginary), (self.real * other.imaginary + self.imaginary * other.real))

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imaginary ** 2
        real_part = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imag_part = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return ComplexNumber(real_part, imag_part)

    def __str__(self):
        return f"{format(self.real, '.2f')} + {format(self.imaginary, '.2f')}i"

c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(1, 4)

print("Sum:", c1 + c2)
print("Difference:", c1 - c2)
print("Product:", c1 * c2)
print("Division:", c1 / c2)

