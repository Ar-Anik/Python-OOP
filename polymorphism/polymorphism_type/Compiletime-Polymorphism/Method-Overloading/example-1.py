# It violet Single Responsibility Principle (SRP)

def operate(a, b, operator):
    if operator == '+':
        return a + b

    elif operator == '-':
        return a - b

    elif operator == '*':
        return a * b

    elif operator == '/':
        try:
            return a / b
        except ZeroDivisionError:
           return f"Division By Zero is not Allowed"

print(operate(5, 3, '+'))
print(operate(8, 2, '-'))
print(operate(4, 0, '/'))
