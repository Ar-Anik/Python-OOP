"""
Learning about composition in Python object-oriented programming:

    1. Definition of composition
    2. Composition vs inheritance
    3. Implementing composition in Python
    4. Benefits of composition
    5. "part-of" relationships
    6. Aggregation vs composition
    7. Delegation in composition
    8. Dependency injection
    9. Design patterns using composition

    10. Composition with abstract base classes
    11. Dynamic composition and runtime object creation
    12. Composition in design patterns (e.g., Strategy, Decorator, Composite)
    13. Metaclasses and composition
    14. Composition with descriptors and properties
    15. Mixin classes as a form of composition
    16. Composition in concurrent and parallel programming
    17. Memory management considerations in complex compositions
    18. Testing strategies for composed objects
    19. Performance optimization in deeply nested compositions
"""

"""
Q : What is Composition?

----> Composition is a key concept in Object-Oriented Programming (OOP) where one class contains another class as part of its attributes, creating a 
"part-of" relationship between them. It's a way to model "part-of" relationships between objects. This is different from inheritance, which models 
"is-a" relationships.

----> Composition is a design principle in object-oriented programming where a class is composed of one or more objects of other classes. Rather than 
inheriting properties and methods from a parent class, a class can contain instances of other classes as attributes, creating a "part-of" relationship 
where the components are essential parts of the main object. This enables flexibility and modularity in code design, allowing complex objects to be 
built by combining simpler ones. For example, a Car is composed of an Engine, meaning that an engine is "part of" a car, rather than a Car "is-a" Engine.
"""

class Engine:
    def start(self):
        return "Engine Started."

    def stop(self):
        return "Engine Stop."

class Car:
    def __init__(self):
        self.engine = Engine()      # Composition: Engine is "part of" a Car.

    def start(self):
        return self.engine.start()

    def stop(self):
        return self.engine.stop()


my_car = Car()
print(my_car.start())
print(my_car.stop())

"""
# Delegation in composition ? (Delegation is nothing but overall composition concept)
----> Delegation in composition is a design approach where an object hands off some of its responsibilities to another object. Instead of managing 
all functionalities within one class, a class delegates certain tasks or methods to another "helper" class (known as the delegate). This approach is 
a key aspect of composition, where the main class does not perform all tasks directly but instead relies on another class to handle specific parts.


----> When using composition with delegation, a class contains an instance of another class (the "delegate") as one of its attributes and forwards 
certain method calls to this delegate object. This setup helps organize code, promote reuse, and separate concerns, as the delegated class handles 
specific functionality while the main class focuses on coordinating overall behavior.

`In the above example, instead of Car managing engine operations directly, it delegates the work to the Engine class by calling start() and stop() 
on self.engine. Here, the Car class does not contain the implementation for starting or stopping the engine itself. Instead, it provides a wrapper 
around these calls, relying on the Engine class to perform the actual operations.
"""

"""
Q : Different Between Inheritance and Composition ?

Inheritance:
    1. Represents an "is-a" relationship (e.g., a Dog is a Animal).
    2. A derived class inherits properties and methods from a base class, gaining its functionality and characteristics.
    3. Creates a hierarchical structure of classes, where subclasses are strongly linked to their superclasses.
    4. Useful when there is a need to extend or modify the behavior of an existing class in a clear hierarchy.

Composition:
    1. Represents a "part-of" relationship (a form of containment), where a class contains one or more instances of other classes as attributes. 
       It often describes a "has-a" relationship (e.g., a Car has an Engine).
    2. A class is composed of other classes, where it can include or remove specific components at runtime, allowing for flexibility and modularity.
    3. Creates a modular structure by building complex objects from simpler ones, promoting separation of concerns.
    4. Ideal when objects need to work together but do not need a hierarchical relationship.

Key differences:
    1. Coupling: Inheritance creates tight coupling between classes (subclasses depend on the superclass), while composition encourages looser 
       coupling (objects can be changed independently).
    2. Purpose: Inheritance is about extending functionality in a defined hierarchy, while composition is about combining functionalities in a 
       flexible manner.
    3. Dependency: With inheritance, subclasses depend on the specific implementation of their superclasses. In composition, classes rely only 
       on the interfaces (or exposed methods) of their component objects, making it easier to swap components without breaking functionality.
"""

"""
====> Benefits of Composition:

a) Flexibility:
    1. Easier to change behavior at runtime by swapping component objects.
    2. Allows for more dynamic structures.

b) Loose coupling:
    1. Classes are less dependent on each other's internal workings.
    2. Changes to one class are less likely to affect others.

c) Improved encapsulation:
    1. Internal details of component objects remain hidden.
    2. Reduces the risk of breaking encapsulation that can occur with inheritance.

d) Easier testing:
    1. Components can be tested in isolation.
    2. Easier to mock or stub dependencies.

e) Avoids the "fragile base class" problem:
    1. Changes to a base class in inheritance can unexpectedly affect subclasses.
    2. Composition minimizes this risk.

f) Favors design by interface:
    1. Encourages programming to interfaces rather than implementations.
    2. Promotes more modular and adaptable code.

g) Multiple sources of behavior:
    1. A class can easily combine behaviors from multiple other classes.
    2. Avoids limitations of single inheritance in some languages.

h) Clearer hierarchies:
    1. Prevents deep and complex inheritance hierarchies that can be hard to understand and maintain.
"""
