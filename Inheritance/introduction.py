# Inheritance is the capability of one class to derive or inherit the attributes,method and properties from another class

class Information:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def write(self):
        for key, value in self.__dict__.items():
            print(f"{key.capitalize()}: {value}")


class Person(Information):
    pass

class Student(Information):
    occupation = "Student"

    def write_class(self):
        for key, value in vars(self.__class__).items():
            print(f"{key.capitalize()}: {value}")

prsn = Person("Anik", 14, "01543267484")
prsn.write()

std = Student("Sourov", 15, "01643278342")
std.write()

# self.__dict__ attribute holds a dictionary of the instance's attributes, but it does not include class attributes.
std.write_class()
