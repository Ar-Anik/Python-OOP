class A:
    __slots__ = ()

class B:
    __slots__ = ()

class C(A, B):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


cls = C(1, 2, 3)
print(cls.a, cls.b, cls.c)

print(hasattr(cls, '__dict__'))
print(hasattr(cls, '__slots__'))
