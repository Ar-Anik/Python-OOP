"""
If the child class defines a new descriptor or method with the same name as one in the parent class. the child class’s version will be used.
"""

class Descriptor:
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class Parent:
    value = Descriptor('parent_value')

    def __init__(self, value):
        self.value = value

class Child(Parent):
    value = Descriptor('child_value')

    def __init__(self, value):
        super().__init__(value)

p = Parent(10)
c = Child(20)

print("Parent Value : ", p.value)
print("Child Value : ", c.value)

c.value = 50
print("Parent Value : ", p.value)
print("Child Value : ", c.value)

print("Parent Dictionary : ", p.__dict__)
print("Child Dictionary : ", c.__dict__)
