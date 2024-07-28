# A Class is like an object constructor
# A Class is a user-defined blueprint for creating object

class Student:
    name = "Aubdur Rob Anik"       # attribute
    roll = "18101073"              # attribute

    def write(self):               # method
        print("self : ", type(self).__name__)
        print("Name : ", self.name)
        print("roll : ", self.roll)

# When an object of a Class is created, the Class is said to be instantiated
std = Student()
std.write()
