class Vehicle:
    def __init__(self, fuel_level):
        self._fuel_level = fuel_level

    def _refuel(self, amount):
        self._fuel_level += amount
        print(f"Refueled {amount} Units. Current Fuel Level: {self._fuel_level}")

class Car(Vehicle):
    def __init__(self, fuel_level, fuel_type):
        super().__init__(fuel_level)
        self._fuel_type = fuel_type

    def refuel(self):
        if self._fuel_type == "Gasoline":
            self._refuel(50)    # Refill with 50 Units for gasoline cars
        elif self._fuel_type == "Electric":
            self._refuel(20)    # Refill with 20 Units for electric cars
        else:
            print("Unknown Fuel Type. Refueling not Supported.")

toyota = Car(20, "Gasoline")
nexon = Car(50, "Electric")

toyota.refuel()
nexon.refuel()
