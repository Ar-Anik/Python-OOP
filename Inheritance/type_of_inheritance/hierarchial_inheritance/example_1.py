"""
Hierarchical inheritance involves a structure where multiple subclasses inherit from a single base class, but additional subclasses can also inherit from those subclasses,
forming a hierarchy. (Sub-Class Have Sub-Class)

The inheritance structure resembles a tree, with the base class at the root and multiple subclasses branching out from it.
"""

class Parent:
    def func1(self):
        print("This is Parent Class")

class Child1(Parent):
    def func2(self):
        print("This is Child1 Class")

class Child2(Parent):
    def func3(self):
        print("This is Child2 Class")


c1 = Child1()
c1.func1()
c1.func2()

c2 = Child2()
c2.func1()
c2.func3()
