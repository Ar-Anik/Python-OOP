"""
1. In multiple inheritance, super() follows the Method Resolution Order(MRO), and it traverses the hierarchy based on the order of MRO.

2. super() can take two arguments: the type of the object whose MRO is used as a starting point for the search, and the object itself.
"""

class A:
    def method(self):
        print("A Method")

class B(A):
    def method(self):
        print("B Method")

class C(B):
    def method(self):
        print("C Method")

class D(C):
    def method(self):
        print("D Method")

class E(D):
    def method(self):
        print("E Method")
        super(B, self).method()

obj = E()
obj.method()

print(E.mro())

""" In this example, super(B, self).method() explicitly indicates that the search for the method should start from the class after B in the MRO. """
