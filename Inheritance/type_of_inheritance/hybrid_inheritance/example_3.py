class BaseClass:
    def method(self):
        print("This is Base Class")

class SubClassA(BaseClass):
    def method(self):
        print("This is SubClass A")

class SubClassB(BaseClass):
    def method(self):
        print("This is SubClass B")

class CombinedClass(SubClassA, SubClassB):
    def method(self):
        print("This is Combined Class")


instance = CombinedClass()
instance.method()

SubClassB.method(instance)
SubClassA.method(instance)
BaseClass.method(instance)
