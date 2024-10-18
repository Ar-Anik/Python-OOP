class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):

        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        if self.name in instance.__dict__:
            del instance.__dict__[self.name]


class Parent:
    attribute = Descriptor('attribute')

    def __init__(self, value):
        self.attribute = value


class Child(Parent):
    pass


p = Parent(10)
c = Child(20)

print("Parent Attribute : ", p.attribute)
print("Child Attribute : ", c.attribute)
