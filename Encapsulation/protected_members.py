class Base:
    def __init__(self, value=2):
        # Protected Member
        self._a = value

class Derived(Base):
    def __init__(self, value=2):
        Base.__init__(self, value)
        print("Calling Protected Member of Base Class : ", self._a)

        self._a = 2 * value
        print("Calling Modified Protected Member Outside Class : ", self._a)

obj1 = Base()

obj2 = Derived()

print("Accessing Protected Member of Base Class Object : ", obj1._a)

print("Accessing Protected Member of Derived Class Object : ", obj2._a)
