# Below Vehical class is not abstract class

from abc import ABC, abstractmethod

class Vehical:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehical):
    def stop(self):
        return f"{self.name} stops smoothly"

class Motorcycle(Vehical):
    def start(self):
        return f"{self.name} roars to life"


car = Car("Toyota")
motorcycle = Motorcycle("Harley Davidson")

print(car.start())
print(car.stop())

print(motorcycle.start())
print(motorcycle.stop())


'''
In Python, using the abc module with abstract base classes (ABCs) is not mandatory for defining abstract methods.

The @abstractmethod decorator can still be used without explicitly inheriting from ABC. 
However, this approach does not enforce the implementation of abstract methods in subclasses at runtime, which is the primary purpose of ABCs.

So, in your example, while the @abstractmethod decorator is used without inheriting from ABC, the code still technically works. 
However, it's not enforcing the abstraction as strictly as when using ABCs.

'''