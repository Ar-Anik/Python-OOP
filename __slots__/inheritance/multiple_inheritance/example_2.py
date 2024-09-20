class A:
    __slots__ = ()

class B:
    __slots__ = ()

class C(A, B):
    __slots__ = ('a', 'b', 'c')

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

c = C(1, 2, 3)
print(c.a, c.b, c.c)
