"""
2. Complexity Increases
Multiple inheritance can lead to complex class hierarchies, making code harder to understand and maintain.
"""

class Animal:
    def make_sound(self):
        print("Generic Animal Sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Bird(Animal):
    def make_sound(self):
        print("Chirp")

class DogBird(Dog, Bird):
    pass

obj = DogBird()
obj.make_sound()          # Which sound will be produced? Complexity increases.
