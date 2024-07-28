class Parent1:
    def write(self):
        print("It Parent1 Function")

class Parent2:
    def write(self):
        print("It Parent2 Function")

class Child(Parent1, Parent2):
    def write(self):
        print("It Child Function")

obj = Child()
obj.write()

# if we call parent1 and parent2 class method like
Parent1.write(obj)
Parent2.write(obj)
