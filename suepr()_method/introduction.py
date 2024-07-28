"""
super() method in Python is used to call methods and access attributes of a superclass (parent class) in a subclass(child class). It's particularly useful when working
with inheritance and want to invoke methods or access attributes defined in a parent class from within a subclass.
"""

class People:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def write(self):
        print("Name :: ", self.name)
        print("Age :: ", self.age)
        print("Phone :: ", self.phone)

class StudentBio(People):
    def __init__(self, name, id, age, phone, university):
        super().__init__(name, age, phone)
        self.id = id
        self.university = university

    def printAll(self):
        super().write()
        print("ID :: ", self.id)
        print("University :: ", self.university)

std = StudentBio("Aubdur Rob Anik", 73, 14, "01685946475", "UAP")
std.printAll()
