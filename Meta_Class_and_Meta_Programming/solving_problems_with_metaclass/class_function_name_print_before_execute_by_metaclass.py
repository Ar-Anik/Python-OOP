def Debug(func):
    """decorator for debugging passed function"""

    def wrapper(*args, **kwargs):
        print("Fully Qualified Name of Class Method : ", func.__qualname__)
        return func(*args, **kwargs)

    return wrapper

# def Debugmethods(cls):
#     """class decorator make use of debug decorator to debug class methods"""
#
#     for key, val in vars(cls).items():
#         if callable(val):
#             setattr(cls, key, Debug(val))
#
#     return cls
#
# class DebugMeta(type):
#     """metaclass which feed created class object to debugmethod to get debug functionality enabled objects"""
#
#     def __new__(cls, clsname, bases, clsdict):
#         obj = super().__new__(cls, clsname, bases, clsdict)
#         obj = Debugmethods(obj)
#         return obj

class DebugMeta(type):
    """Metaclass which applies the debug decorator to all callable methods in the class."""

    def __new__(cls, clsname, bases, clsdict):
        new_clsdict = {}

        for key, val in clsdict.items():
            if callable(val):
                new_clsdict[key] = Debug(val)
            else:
                new_clsdict[key] = val

        obj = super().__new__(cls, clsname, bases, new_clsdict)

        return obj


class Base(metaclass=DebugMeta):
    pass

class Calc(Base):
    def add(self, x, y):
        return x + y

class Calc_Multi(Calc):
    def mul(self, x, y):
        return x * y

mycal = Calc_Multi()
print(mycal.add(5, 6))
print(mycal.mul(5, 6))
