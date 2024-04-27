class Base:
    def __init__(self, value):
        self.a = value
        self.__c = "Protected Variable"

class Derived(Base):
    def __init__(self, value):
        super().__init__(value)
        print("Calling Private Member of Base Class : ", self.__c)

obj1 = Base(2)
print(obj1.a)

# It raise AttributeError: 'Base' object has no attribute '__c'
# print(obj1.__c)

# It raise AttributeError: 'Derived' object has no attribute '_Derived__c'
# obj2 = Derived(3)
