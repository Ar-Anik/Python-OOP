class Parent1:
    def write(self):
        print("From Parent1")

class Parent2:
    def write(self):
        print("From Parent2")

class Child1(Parent1, Parent2):
    pass

class Child2(Parent2, Parent1):
    pass

obj1 = Child1()
obj1.write()

obj2 = Child2()
obj2.write()
