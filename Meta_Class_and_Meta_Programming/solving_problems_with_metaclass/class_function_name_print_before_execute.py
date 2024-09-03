def debug(func):
    """decorator for debugging passed function"""
    def wrapper(*args, **kwargs):
        print("Fully Qualified Name of this method : ", func.__qualname__)
        return func(*args, **kwargs)

    return wrapper


def debugmethods(cls):
    """class decorator make use of debug decorator to debug class methods"""

    # check in class dictionary for any callable(method)
    # if exist, replace it with debugged version

    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, debug(val))

    print("Each Class Function : ", cls.__dict__)
    return cls

@debugmethods
class Calc:
    def add(self, x, y):
        return x+y
    def mul(self, x, y):
        return x*y
    def div(self, x, y):
        if y > 0:
            return x/y
        else:
            raise ValueError("Division By Zero")

mycal = Calc()
print(mycal.add(2, 3))
print(mycal.mul(5, 2))
print(mycal.div(12, 3))
