""" Adding a New Method at Runtime """

class Calculator:
    def add(self, a, b):
        return a + b

def multiply(self, a, b):
    return a * b

Calculator.multiply = multiply

klas = Calculator()

print(klas.add(4, 5))
print(klas.multiply(4, 5))
