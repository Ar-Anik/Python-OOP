# Relationship Like Linear

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def display_info(self):
        for key, value in self.__dict__.items():
            print(f"{key.capitalize()}: {value}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark Bark!")


my_dog = Dog("Buddy", "Golden Retriever")
my_dog.display_info()
my_dog.make_sound()
