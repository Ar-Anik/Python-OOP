# Static Method Example : Utility Function
class MathOperations:
    @staticmethod
    def add(x, y):
        return x+y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y != 0:
            return x/y
        else:
            return "Can't divide by zero"

print(MathOperations.add(5, 3))
print(MathOperations.subtract(5, 3))
print(MathOperations.multiply(5, 3))
print(MathOperations.divide(10, 3))
print(MathOperations.divide(10, 0))
