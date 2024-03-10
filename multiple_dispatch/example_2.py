from multipledispatch import dispatch

@dispatch(int, int)
def evaluate(op1, op2):
    return op1 + op2

@dispatch(float, float)
def evaluate(op1, op2):
    return op1 + op2

@dispatch(int, float)
def evaluate(op1, op2):
    return op1 + op2

@dispatch(float, int)
def evaluate(op1, op2):
    return op1 + op2

@dispatch(int, int)
def evaluate(op1, op2):
    return op1 - op2

@dispatch(float, float)
def evaluate(op1, op2):
    return op1 - op2

@dispatch(int, float)
def evaluate(op1, op2):
    return op1 - op2

@dispatch(float, int)
def evaluate(op1, op2):
    return op1 - op2

@dispatch(int, int)
def evaluate(op1, op2):
    return op1 * op2

@dispatch(float, float)
def evaluate(op1, op2):
    return op1 * op2

@dispatch(int, float)
def evaluate(op1, op2):
    return op1 * op2

@dispatch(float, int)
def evaluate(op1, op2):
    return op1 * op2

@dispatch(int, int)
def evaluate(op1, op2):
    if op2 == 0:
        raise ZeroDivisionError("Division by zero")
    return op1 / op2

@dispatch(float, float)
def evaluate(op1, op2):
    if op2 == 0:
        raise ZeroDivisionError("Division by zero")
    return op1/op2

@dispatch(int, float)
def evaluate(op1, op2):
    if op2 == 0:
        raise ZeroDivisionError("Division by zero")
    return op1/op2

@dispatch(float, int)
def evaluate(op1, op2):
    if op2 == 0:
        raise ZeroDivisionError("Division by zero")
    return op1/op2

print(evaluate(5, 3))
print(evaluate(2.5, 4.0))
print(evaluate(5, 5.5))
print(evaluate(5.5, 6.5))
