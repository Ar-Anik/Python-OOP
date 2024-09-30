from multipledispatch import dispatch

@dispatch(int, int)
def calculate(x, y):
    return x + y

@dispatch(float, float)
def calculate(x, y):
    return x * y

@dispatch(str, str)
def calculate(x, y):
    return x + " " + y

print(calculate(2, 2))
print(calculate(2.5, 4.0))
print(calculate("Hello", "World"))
