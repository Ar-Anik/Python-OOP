"""
# Base Class with MultiBases Metaclass:
    1. When you define class Base(metaclass=MultiBases):, the Base class itself is created using the MultiBases metaclass.
    2. This means that any time a new subclass of Base is created, the metaclass MultiBases will be used to govern its creation process.

# How MultiBases Affects Subclasses (Class A, B, C):
    * Class A and B Creation:
        1. When class A(Base): is defined, Python sees that Base has a metaclass (MultiBases).
        2. The MultiBases.__new__ method is called to create the class A.
        3. Since A only inherits from one base class (Base), MultiBases.__new__ does not raise an error and allows the class A to be created.
        4. The same process happens for class B(Base).

    * Class C Creation:
        1. When you define class C(A, B):, Python again sees that A and B both inherit from Base, and therefore, their metaclass is MultiBases.
        2. Since C tries to inherit from both A and B, MultiBases.__new__ is called to create the class C.
        3. Inside MultiBases.__new__, the number of base classes is checked. Here, C has two base classes (A and B), so the length of bases is 2.
        4. Because of the logic in MultiBases.__new__, a TypeError is raised with the message "Inherited multiple base classes!!!", and the class C
           is not created.

# Propagation of Metaclass Behavior:
    1. The MultiBases metaclass affects all subclasses of Base because Python uses the metaclass of the base class when creating subclasses.
    2. In this case, since Base has MultiBases as its metaclass, any subclass of Base will also be governed by MultiBases.
    3. Therefore, the metaclass’s logic is applied not only when Base is created but also when any subclass of Base is created, ensuring that
       the metaclass rules are enforced consistently across the inheritance chain.

# Why Metaclass Behavior Propagates:
    1. When you create a class, Python checks if the class itself or any of its base classes have a metaclass.
    2. If a base class has a metaclass, Python uses that metaclass to create the new subclass.
    3. This is why MultiBases affects not just Base, but also A, B, and C.
"""

class MultiBases(type):
    def __new__(cls, clsname, bases, clsdict):
        if len(bases) > 1:
            raise TypeError("Inherited Multiple Base Classess!!!")

        return super().__new__(cls, clsname, bases, clsdict)

class Base(metaclass=MultiBases):
    pass

class A(Base):
    pass

class B(Base):
    pass

class C(A, B):
    pass
