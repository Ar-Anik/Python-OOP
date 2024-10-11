class MyDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print(f"Accessing {self.name}")
        return instance.__dict__.get(self.name, '')

    def __set__(self, instance, value):
        print(f"Setting {self.name} to {value}")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        if self.name in instance.__dict__:
            print(f"Deleting {self.name}")
            del instance.__dict__[self.name]


class MyClass:
    attribute_1 = MyDescriptor("attribute_1")
    attribute_2 = MyDescriptor("attribute_2")

obj = MyClass()

obj.attribute_1 = 10
obj.attribute_2 = 20

print(obj.attribute_1)
print(obj.attribute_2)

obj.__dict__['attribute_1'] = 100
print(obj.attribute_1)
