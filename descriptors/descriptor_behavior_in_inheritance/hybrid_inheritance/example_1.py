"""
In hybrid inheritance, where a class inherits from multiple and multilevel hierarchies, descriptors follow the MRO.
"""

class DescriptorX:
    def __get__(self, instance, owner):
        return "Descriptor in X."

class DescriptorZ:
    def __get__(self, instance, owner):
        return "Descriptor in Z."

class X:
    attr = DescriptorX()

class Y(X):
    pass

class Z:
    attr = DescriptorZ()

class W(Y, Z):
    pass

w = W()
print(w.attr)

"""
the MRO for W is [W, Y, X, Z, object], so the descriptor from X is used.
"""
