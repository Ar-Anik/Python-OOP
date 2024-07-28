# Multilevel inheritance in Python refers to a scenario where a class inherits from another class, and then another class inherits from that derived class, creating a chain of inheritance.
# It create a hierarchy of classes where each class inherits attributes and methods from its parent class.

# Multilevel inheritance forms a linear chain of subclasses, whereas hierarchical inheritance involves multiple subclasses branching out from a single base class.

class Father:
    def fun1(self):
        print("\nThis is Father Class")

class Son(Father):
    def fun2(self):
        print("This is Son Class")

class Grandson(Son):
    def fun3(self):
        print("This is GrandSon Class")

a = Grandson()
a.fun1()
a.fun2()
a.fun3()
