class Descriptor:
    def __get__(self, instance, owner):
        print(f"Call Get From {instance.__class__.__name__}")
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        print(f"Call Set From {instance.__class__.__name__}")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class BaseClass:
    attr = Descriptor()

class DerivedClass(BaseClass):
    attr = Descriptor()

class FinalClass(DerivedClass):
    attr = Descriptor()

obj = FinalClass()

obj.attr = 10

print(obj.attr)
