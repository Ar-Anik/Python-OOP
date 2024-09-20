"""
In the context of multiple inheritance, __slots__ can behave differently depending on how it's defined in the base classes.
"""

class A:
    __slots__ = ('a',)

    def __init__(self, a):
        self.a = a

class B:
    __slots__ =  ('b',)

    def __init__(self, b):
        self.b = b

class C(A, B):
    # __slots__ = ('c',)

    def __init__(self, a, b, c):
        A.__init__(self, a)
        B.__init__(self, b)
        self.c = c

obj = C(1, 2, 3)
print(obj.a, obj.b, obj.c)

"""
when execute code, class C(A, B) an error occur like `TypeError: multiple bases have instance lay-out conflict`

Error occurs because Python cannot handle multiple inheritance with __slots__ when the base classes (A and B) each define their own __slots__. This is a limitation of Python's 
internal memory layout management. 

----> Why This Error Occur ?
When a class uses __slots__, it changes how instance attributes are stored. Normally, Python objects have a __dict__ to store instance attributes, but __slots__ removes that 
flexibility to save memory. However, in cases of multiple inheritance, Python struggles to manage memory layouts when different base classes define their own __slots__.
"""
