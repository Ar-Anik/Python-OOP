# Multiple inheritance in Python refers to a situation where a class can inherit attributes and methods from more than one parent class. This means that a child class can inherit from multiple base classes.
class ClassA:
    def __init__(self):
        self.name1 = "A"

    def wrt1(self):
        print("\nThis is class ", self.name1)

class ClassB:
    def __init__(self):
        self.name2 = "B"

    def wrt2(self):
        print("This is Class ", self.name2)

class ClassC(ClassA, ClassB):
    def __init__(self):
        ClassA.__init__(self)
        ClassB.__init__(self)

    def write(self):
        ClassA.wrt1(self)
        ClassB.wrt2(self)

c = ClassC()
c.write()
