# Method use for initialization attributes by built-in function __init__ method which is also called constructor

class Student:
    def __init__(self, name, roll, semester):
        self.name = name
        self.roll = roll
        self.semester = semester

    def write(self):
        print("Name : ", self.name)
        print("Roll : ", self.roll)
        print("Semester : ", self.semester)

std = Student("Aubdur Rob Anik", "18101073", "1-1")
std.write()


# Method use for initialization by user defined function
class Person:
    def set_value(prsn, name, age):
        prsn.name = name
        prsn.age = age

    def write(prsn):
        print("Name : ", prsn.name)
        print("Age : ", prsn.age)

person = Person()
person.set_value("Aubdur Rob Anik", 14)
person.write()


# Initialization by constructor and user define function
class Vehical:
    def __init__(self, company, engine_no, chesis_no):
        self.company = company
        self.engine_no = engine_no
        self.chesis_no = chesis_no

    def set_value(vcl, model):
        vcl.model = model

    def write(self):
        print("Name : ", self.company)
        print("Engine No. : ", self.engine_no)
        print("Chesis No : ", self.chesis_no)
        print("Model : ", self.model)

car = Vehical("Mahindra", "223344", "654327")
car.set_value("XUV 3XO")
car .write()
