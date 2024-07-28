# Factory/built-in Method to Create Instances
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @classmethod
    def from_string(cls, cls_string):
        make, model = cls_string.split('-')
        return cls(make, model)

car_str = "Toyota-XCorolla"
car = Car.from_string(car_str)

print(car.make)
print(car.model)