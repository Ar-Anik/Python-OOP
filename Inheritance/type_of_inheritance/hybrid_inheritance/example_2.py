class Animal:
    def sound(self):
        print("This is an Animal")

class Mammal(Animal):
    pass

class Bird(Animal):
    def sound(self):
        print("This is a Bird")

class Bat(Mammal, Bird):
    pass

creature = Bat()
creature.sound()

# Check the method resolution order (MRO)
print(Bat.mro())