from multipledispatch import dispatch

class Animal:
    def __init__(self, name):
        self.name = name

class Herbivore(Animal):
    def __str__(self):
        return f"{self.name} the Herbivore"

class Carnivore(Animal):
    def __str__(self):
        return f"{self.name} the Carnivore"

class Omnivore(Animal):
    def __str__(self):
        return f"{self.name} the Omnivore"

class Food:
    def __init__(self, name):
        self.name = name

class Grass(Food):
    def __init__(self):
        super().__init__("Grass")

    def __str__(self):
        return self.name

class Meat(Food):
    def __init__(self):
        super().__init__("Meat")

    def __str__(self):
        return self.name

class Fruit(Food):
    def __init__(self):
        super().__init__("Fruit")

    def __str__(self):
        return self.name

@dispatch(Herbivore, Grass)
def feed(animal, food):
    print(f"Feeding {animal} some {food}.")

@dispatch(Carnivore, Meat)
def feed(animal, food):
    print(f"Feeding {animal} some {food}.")

@dispatch(Omnivore, Food)
def feed(animal, food):
    print(f"Feeding {animal} some {food}.")

lion = Carnivore("Leo")
giraffe = Herbivore("Gerry")
human = Omnivore("Alice")

grass = Grass()
meat = Meat()
fruit = Fruit()

feed(lion, meat)
feed(giraffe, grass)
feed(human, fruit)
feed(human, meat)
