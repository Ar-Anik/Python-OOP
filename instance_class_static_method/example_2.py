# Keeping Track of Instances Created
class Dog:
    num_dogs = 0

    def __init__(self, name):
        self.name = name
        Dog.num_dogs += 1

    @classmethod
    def total_dogs(cls):
        return cls.num_dogs

dog1 = Dog("Anik Das")
dog2 = Dog("Anisul Islam Oni")

print(Dog.total_dogs())
