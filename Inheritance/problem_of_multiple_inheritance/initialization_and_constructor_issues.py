"""
3. Initialization and Constructor Issues
Constructors (__init__ methods) of multiple base classes can conflict or interact in unexpected ways, especially
if they expect different arguments or perform conflicting initialization tasks.
"""

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):
    def __init__(self, brand, model, num_wheels):
        super().__init__(brand, model)
        self.num_wheels = num_wheels


class Boat(Vehicle):
    def __init__(self, brand, model, max_speed):
        super().__init__(brand, model)
        self.max_speed = max_speed


class AmphibiousVehicle(Car, Boat):
    def __init__(self, brand, model, num_wheels, max_speed):
        # Which Superclass constructor should be called here?
        # Conflicting Initialization tasks may occur.
        super().__init__(brand, model, num_wheels)
        self.max_speed = max_speed

print(AmphibiousVehicle.__mro__)
bmp = AmphibiousVehicle("Soviet", "BMP-3", 12, 760)

"""
it show TypeError: __init__() missing 1 required positional argument: 'max_speed' From the MRO, we see that the __init__ method of Car will be 
called first. So, when create an instance of AmphibiousVehicle, both Car and Boat's __init__ methods will be called. The Car class's __init__ 
method will initialize brand, model, and num_wheels, and then the Boat class's __init__ method will not initialize max_speed. 
That why show error.
"""