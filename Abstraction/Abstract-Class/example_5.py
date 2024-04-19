from abc import ABC, abstractmethod

class cls1(ABC):
    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass

class cls2(cls1):
    @abstractmethod
    def method3(self):
        pass

class cls3(cls2):
    def method1(self):
        print("This is method-1")

    def method2(self):
        print("This is method-2")

    def method3(self):
        print("This is method-3")

cls = cls3()
cls.method1()
cls.method2()
cls.method3()