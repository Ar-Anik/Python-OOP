class SoundDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get("sound", None)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Sound must be a string.")
        instance.__dict__["sound"] = value


class Animal:
    sound = SoundDescriptor()

class Dog(Animal):
    def bark(self):
        return f"Dog barks: {self.sound}"

class Cat(Animal):
    def meow(self):
        return f"Cat meows: {self.sound}"

dog = Dog()
cat = Cat()

dog.sound = "Woof"
cat.sound = "Meow"

print(dog.bark())
print(cat.meow())
