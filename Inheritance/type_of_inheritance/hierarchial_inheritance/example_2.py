class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand : {self.brand}, Model: {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, seat_num):
        super().__init__(brand, model)
        self.seat_num = seat_num

    def display_info(self):
        super().display_info()
        print(f"Number of Seats : {self.seat_num}")


class Truck(Vehicle):
    def __init__(self, brand, model, cargo_capacity):
        super().__init__(brand, model)
        self.cargo_capacity = cargo_capacity

    def display_info(self):
        super().display_info()
        print(f"Cargo Capacity : {self.cargo_capacity}")


class ElectricCar(Car):
    def __init__(self, brand, model, seat_num, battery_range):
        super().__init__(brand, model, seat_num)
        self.battery_range = battery_range

    def display_info(self):
        super().display_info()
        print(f"Battery Range : {self.battery_range}")


class HybridCar(Car):
    def __init__(self, brand, model, seat_num, fuel_economy):
        super().__init__(brand, model, seat_num)
        self.fuel_economy = fuel_economy

    def display_info(self):
        super().display_info()
        print(f"Fuel Economy : {self.fuel_economy}")


tesla_car = ElectricCar("Tesla", "Model S", 4, 375)
tesla_car.display_info()

ford_truck = Truck("Ford", "F-150", 2)
ford_truck.display_info()

toyota_car = HybridCar("Toyota", "Prius", 5, 50)
toyota_car.display_info()
