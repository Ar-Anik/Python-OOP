class Descriptor:
    def __get__(self, instance, owner):
        print(f"Getting Value from {self.__class__.__name__}")
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        print(f"Setting Value in {self.__class__.__name__}")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

class DescriptorA(Descriptor):
    def __get__(self, instance, owner):
        return super().__get__(instance, owner)

    def __set__(self, instance, value):
        super().__set__(instance, value)

class DescriptorB(Descriptor):
    def __get__(self, instance, owner):
        super().__get__(instance, owner)

    def __set__(self, instance, value):
        super().__set__(instance, value)


class BaseA:
    attr = DescriptorA()

class BaseB:
    attr = DescriptorB()

class BaseC(BaseA, BaseB):
    pass

print("BaseC class MRO : ", BaseC.__mro__)
obj = BaseC()

obj.attr = 100

print(obj.attr)
