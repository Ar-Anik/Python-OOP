"""
Method overriding in Python refers to the ability of a subclass to provide a specific implementation of a method that is already defined in its superclass.
When a method is overridden in a subclass, the subclass provides a new implementation of that method that replaces the implementation inherited from the superclass.
"""

class Parent:
    def write(self):
        print("Called From Parent.")

class Child(Parent):
    def write(self):
        print("Called From Child.")

c = Child()
c.write()

# if we call parent class method like
Parent.write(c)