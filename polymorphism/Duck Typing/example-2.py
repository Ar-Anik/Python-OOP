class Dog:
    def speak(self):
        return "Woof"

    def eat(self):
        return "Meat"

    def move(self):
        return "Running"

class Cat:
    def speak(self):
        return "Meow"

    def eat(self):
        return "Fish"

    def move(self):
        return "Walking"

class Duck:
    def speak(self):
        return "Quack"

    def eat(self):
        return "Pondweed"

    def move(self):
        return "Swiming"

# def simulate_zoo(*animals):
#     for animal in animals:
#         for ani in animal:
#             if hasattr(ani, 'speak') and callable(ani.speak):
#                 print(ani.speak())
#
#             if hasattr(ani, 'eat') and callable(ani.eat):
#                 print(ani.eat())
#
#             if hasattr(ani, 'move') and callable(ani.move):
#                 print(ani.move())
#
#             print()

def simulate_zoo(*animals):
    for animal in animals:
        if hasattr(animal, 'speak') and callable(animal.speak):
            print(animal.speak())

        if hasattr(animal, 'eat') and callable(animal.eat):
            print(animal.eat())

        if hasattr(animal, 'move') and callable(animal.move):
            print(animal.move())

        print()

dog = Dog()
cat = Cat()
duck = Duck()

simulate_zoo(dog, cat, duck)