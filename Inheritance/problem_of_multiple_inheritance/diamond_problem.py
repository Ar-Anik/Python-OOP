"""
1. Diamond Problem
Diamond problem, also known as the Deadly Diamond of Death, is a classic issue that arises in languages that support multiple inheritance.
It occurs when a subclass inherits from two classes that have a common ancestor.
"""


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print("Class Name : ", self.__class__.__name__)
        print(f"Make : {self.make}, Model: {self.model}")


class Car(Vehicle):
    def drive(self):
        print("Driving Car....")


class Truck(Vehicle):
    def load_cargo(self):
        print("Loading Cargo....")


class HybridCar(Car, Truck):  # Diamond Problem arises here
    pass


print(HybridCar.__mro__)

hybrid_car = HybridCar("Toyota", "Prius")
hybrid_car.display_info()  # Which 'display_info' method should be called?
hybrid_car.drive()
hybrid_car.load_cargo()

"""
Python resolves this by following a specific Method Resolution Order (MRO) using the C3 linearization algorithm, 
which determines the order in which methods are searched for and executed. However, if there's no clear resolution, 
Python will raise a TypeError indicating that the method resolution is ambiguous.
"""