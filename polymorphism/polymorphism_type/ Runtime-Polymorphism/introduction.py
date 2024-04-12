# Run-time -----> Overriding

''' Runtime polymorphism is a fundamental concept in object-oriented programming (OOP) where the selection of a method to execute happens at runtime
 rather than at compile time. It enables a program to behave differently based on the actual type of object being operated upon. '''

''' Runtime polymorphism is a fundamental concept in object-oriented programming (OOP) where the selection of a method to execute happens at runtime
rather than at compile time. It enables a program to behave differently based on the actual type of object being operated upon. '''

# Python is dynamically typed and supports both inheritance and method overriding, which are essential for achieving runtime polymorphism : -
''' Inheritance: Runtime polymorphism relies on inheritance. You have a superclass (or base class) and one or more subclasses (or derived classes).
                 The subclass inherits properties and methods from the superclass '''

''' Method Overriding: Subclasses can provide their own implementation of a method that is already defined in the superclass. This is achieved by redefining the 
                       method in the subclass with the same signature (method name, parameters, and return type) as in the superclass.'''

''' Late Binding: The decision about which method to call is made at runtime based on the type of the object that invokes the method. 
                  This is also called dynamic binding or late binding. '''

class Animal:
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

# Creating instances of subclasses
dog = Dog()
cat = Cat()

# Calling the overridden method
dog.make_sound()
cat.make_sound()

'''
1. We define a superclass Animal with a method make_sound(), which prints a generic sound.

2. We define two subclasses, Dog and Cat, which override the make_sound() method with their specific implementations.

3. We create instances of Dog and Cat, and when we call the make_sound() method on these instances, 
   Python dynamically resolves the method to call based on the actual type of the object at runtime.
   
4. This dynamic method resolution is what constitutes runtime polymorphism. 
   The make_sound() method behaves differently depending on whether it's called on a Dog object or a Cat object, 
   allowing for flexible and polymorphic behavior.
'''

# This dynamic resolution of methods at runtime is a characteristic feature of late binding in Python :
'''
Late binding refers to the process where the decision about which method to call is made at runtime based on the type 
of the object that invokes the method.

In Python, method resolution is primarily dynamic, meaning the method to be called is determined at runtime. 
This allows for flexibility and polymorphism in object-oriented programming. When you call a method on an object in Python, 
the interpreter dynamically looks up the method based on the object's actual type at runtime and invokes the appropriate implementation.

In the above example, when dog.make_sound() is called, Python dynamically resolves the method to invoke based on the actual 
type of the dog object (which is of type Dog). Similarly, when cat.make_sound() is called, Python dynamically resolves the method 
based on the actual type of the cat object (which is of type Cat). 
This dynamic resolution of methods at runtime is a characteristic feature of late binding in Python.
'''