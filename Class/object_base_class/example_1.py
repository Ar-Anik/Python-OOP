class CustomClass:
    def __init__(self, x):
        self.x = x

obj = CustomClass(5)

print(obj.__str__())
print(obj.__repr__())
print(obj.__eq__(obj))   # __eq__() is used to compare objects for equality.
