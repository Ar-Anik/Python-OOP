"""
if a child class overrides the descriptor, its own behavior takes precedence. Otherwise, the parent’s descriptor is inherited.
"""

class DescriptorParent:
    def __get__(self, instance, owner):
        return 'Descriptor in Parent.'

class DescriptorChild:
    def __get__(self, instance, owner):
        return 'Descriptor in Child.'

class Parent:
    attr = DescriptorParent()

class ChildOne(Parent):
    pass

class ChildTwo(Parent):
    attr = DescriptorChild()

c1 = ChildOne()
c2 = ChildTwo()

print(c1.attr)
print(c2.attr)
