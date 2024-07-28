"""
Hybrid inheritance is a combination of all type inheritance Hybrid inheritance is a type of inheritance in  object-oriented programming where a class inherits from multiple base classes,
combining features of both single and multiple inheritance. This means that a subclass can inherit attributes and methods from more than one parent class, forming a complex inheritance hierarchy.
"""

class Base:
    def function(self):
        print("This is the Base class")

class DerivedA(Base):
    def function(self):
        print("This is DerivedA")

class DerivedB(Base):
    def function(self):
        print("This is DerivedB")

class Combined(DerivedA, DerivedB):
    pass

obj = Combined()
obj.function()

# Check the method resolution order (MRO)
print(Combined.mro())

