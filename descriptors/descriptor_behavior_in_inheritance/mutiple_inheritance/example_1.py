"""
In multiple inheritance, the method resolution order (MRO) comes into play. The descriptor follows the MRO to decide which class’s descriptor is used.
"""

class DescriptorA:
    def __get__(self, instance, owner):
        return "Descriptor in A"

class DescriptorB:
    def __get__(self, instance, owner):
        return "Descriptor in B"

class A:
    attr = DescriptorA()

class B:
    attr = DescriptorB()

class C(A, B):
    pass

print("C class MRO : ", C.__mro__)
c = C()

print(c.attr)

"""
Here, class C inherits from both A and B, but since A is before B in the MRO, the descriptor from A is used.
"""
