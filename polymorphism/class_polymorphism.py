class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Paddle")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly")

car_1 = Car("Tata", "F-19")
boat_1 = Boat("Ibiza", "Touring-20")
plane_1 = Plane("Boeing", "747")

for x in (car_1, boat_1, plane_1):
    x.move()