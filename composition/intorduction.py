"""
Learning about composition in Python object-oriented programming:

    1. Definition of composition
    2. Composition vs inheritance
    3. Implementing composition in Python
    4. Benefits of composition
    5. "Has-a" relationships
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

----> Composition is a key concept in Object-Oriented Programming (OOP) where one class contains another class as part of its attributes, which 
allows for building complex types by combining objects. It's a way to model "has-a" relationships between objects. This is different from 
inheritance, which models "is-a" relationships.

----> Composition is a design principle in object-oriented programming where a class is composed of one or more objects of other classes. Instead of 
inheriting properties and methods from a parent class, a class can contain instances of other classes as attributes. This allows for greater flexibility 
and modularity in code design, as it enables you to build complex objects by combining simpler ones. The main idea behind composition is "has-a" 
relationship, as opposed to inheritance's "is-a" relationship. For example, a Car "has-a" Engine, rather than a Car "is-a" Engine.
"""

class Engine:
    def start(self):
        return "Engine Started."

    def stop(self):
        return "Engine Stop."

class Car:
    def __init__(self):
        self.engine = Engine()      # Composition: Car has-a Engine.

    def start(self):
        return self.engine.start()

    def stop(self):
        return self.engine.stop()


my_car = Car()
print(my_car.start())
print(my_car.stop())

"""
# Delegation in composition ? (Delegation is nothing but overall composition concept)
----> delegation in composition is a design approach where an object hands off some of its responsibilities to another object. In other words, 
instead of handling all functionality within one class, one class delegates certain tasks or methods to another "helper" class.


----> When using composition with delegation, a class has an instance of another class (the "delegate") as one of its attributes and forwards 
certain method calls to this delegate object. This helps in organizing code, promoting reuse, and separating concerns, as the delegated class 
handles specific tasks, while the main class focuses on coordinating these tasks.

`In the above example  Instead of Car managing engine operations directly, it delegates the work to Engine by calling start() and stop() on 
self.engine. The Car class just provides a wrapper around these calls.`
"""

"""
Q : Different Between Inheritance and Composition ?

Inheritance:
    1. Represents an "is-a" relationship
    2. A derived class inherits properties and methods from a base class
    3. Creates a hierarchical structure of classes

Composition:
    1. Represents a "has-a" relationship
    2. One class contains an instance of another class as a member
    3. Creates a modular structure where objects are composed of other objects

Key differences:
    1. Inheritance creates tight coupling between classes, while composition allows for looser coupling
    2. Inheritance is about extending functionality, while composition is about combining functionalities
    3. With inheritance, subclasses depend on the implementation of their superclasses; with composition, classes depend only on the interfaces of their component objects
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
