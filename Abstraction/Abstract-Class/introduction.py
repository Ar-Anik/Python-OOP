"""
In Python, an abstract class is a class that cannot be instantiated on its own and is designed to be subclassed.
It may contain one or more abstract methods, which are methods declared but not implemented in the abstract class.
Subclasses of an abstract class must provide implementations for all the abstract methods declared in the parent abstract class.
"""

"""
A class derived from ABC Class which belongs to abc module, is known as abstract class in Python.
"""

"""
1. ABC Class is known as Meta Class which means a class that defines the behavior of other classes. So we can say, Meta Class ABC defines that 
the class which is derived from it becomes an abstract class.

2. Abstract class can have abstract method and concrete methods.

3. Abstract class needs to be extended and its method implemented.

4. Python Virtual Machine(PVM) can not create objects of an abstract class.
   (PVM : A program which provides programming environment. The role of PVM is to convert the byte code instructions 
   into machine code so the computer can execute those machine code instructions and display the output.)
"""

"""
Concrete Method : A concrete method is a method whose action is define in the abstract class itself.

Example: 
from abc import ABC, abstractmethod
class Father(ABC):
    @abstractmethod
    def display(self):       # Abstract Method / Method without Body
        pass
        
    def show(self):
        print("Concrete Method")    # Concrete Method / Method with Body

"""

"""
Abstract Class Rules:

1. PVM can not create objects of an abstract class.

2. It is not necessary to declare all methods abstract in a abstract class.

3. Abstract class can have abstract method and concrete methods.

4. If there is any abstract method in a class, that class must be abstract.

5. The abstract methods of an abstract class must be defined in its child class/subclass.

6. If you are inheriting any abstract class that have abstract method, you must either provide the implementation of the method or
   make this class abstract.
"""

"""
When use Abstract Class?
    We use abstract class when there are some common feature shared by all the objects as they are.
"""