class ValueDescriptor:
    def __init__(self):
        self._value = ''

    def __get__(self, instance, owner):
        print(f"Get Function Call From {instance.__class__.__name__}")
        return self._value

    def __set__(self, instance, value):
        print(f"Set Function Call From {instance.__class__.__name__}")
        self._value = value

    def __delete__(self, instance):
        print(f"Delete Function Call From {instance.__class__.__name__}")
        try:
            del self._value
        except AttributeError:
            print("Value Not Exist.")


class BaseClass:
    value = ValueDescriptor()

class AnotherBaseClass:
    def display(self):
        print("Another base class method.")

class DerivedClass(BaseClass, AnotherBaseClass):
    def show(self):
        print("Derived class method.")

class FurtherDerivedClass(DerivedClass):
    def show_more(self):
        print("Further derived class method.")


obj = FurtherDerivedClass()

obj.value = 42
print(obj.value)

obj.show()
obj.display()
obj.show_more()
