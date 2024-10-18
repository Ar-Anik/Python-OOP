"""
In multilevel inheritance, the descriptor is passed down through multiple levels of inheritance.
"""

class Descriptor:
    def __get__(self, instance, owner):
        print(f"From Class {instance.__class__.__name__}")
        return "Descriptor in Grandparent."

class Grandparent:
    attr = Descriptor()

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

child = Child()
parent = Parent

print(child.attr)
print(parent.attr)
