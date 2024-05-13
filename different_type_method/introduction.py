# Instance Method
# It takes self as the first parameter, which refers to the instance on which the method is called.

# Class Method:
# A class method is a method that operates on the class itself
# It takes cls as the first parameter, which refers to the class itself
# Class methods are defined using the @classmethod decorator.

# Static Method
# A static method is a method that does not operate on either the class or its instances.
# It does not take self or cls as parameters.
# Static methods are defined using the @staticmethod decorator.

class Student:
    university = "University of Asia Pacific"
    def __init__(self, name, id, department):
        self.name = name
        self.id = id
        self.department = department

    # Instance Method
    def show(self):
        print("Name : ", self.name)
        print("ID : ", self.id)
        print("Department : ", self.department)
        print("University : ", self.university)

    # Class Method:
    @classmethod
    def from_class(cls):
        print('{}, Here No Convocation Held'.format(cls.university))
        print("Class Name : ", cls.__name__)

    # Static Method
    @staticmethod
    def staticMethod():
        print("Bro I am independent No Argument Need")

    def staticMethodWithArgument(wifeName):
        print((wifeName + '\n') * 5, sep='')

    def __str__(self):
        return f"Name -> {self.name}, ID -> {self.id}, Department -> {self.department}, University -> {self.university}"

class Derive(Student):
    pass

s = Student("Anik", 18101073, "CSE")

# s.from_class()
# Student.from_class()

Derive.from_class()
