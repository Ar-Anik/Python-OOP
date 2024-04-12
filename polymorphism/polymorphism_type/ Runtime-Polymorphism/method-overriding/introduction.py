''' Method overriding in Python refers to the ability of a subclass to provide a specific implementation of a method that is already defined
in its superclass. This allows the subclass to change the behavior of the method while keeping the method name and signature the same as
the superclass. '''

class Animal:
   def make_sound(self):
       print("Generic Animal Sound")

class Dog(Animal):
   def make_sound(self):
       print("Woof")
       super().make_sound()

class Cat(Animal):
   def make_sound(self):
       print("Meow")

dog = Dog()
cat = Cat()

dog.make_sound()
cat.make_sound()
