"""
1. Instance Method
It takes self as the first parameter, which refers to the instance on which the method is called.

2. Class Method:
A class method is a method that operates on the class itself. It takes cls as the first parameter, which refers to the class itself.
Class methods are defined using the @classmethod decorator.

3. Static Method
A static method is a method that is bound to the class and not the instance of the class. It does not take self or cls as parameters.
Static methods are defined using the @staticmethod decorator.

Static methods: Do not have access to the instance (self) or the class (cls). They behave like plain functions but belong to the class's namespace.
They are used for utility functions that perform a task in isolation, without needing access to class or instance data.
"""

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

    @staticmethod
    def staticMethodWithArgument(wifeName):
        print((wifeName + '\n') * 5)

    def __str__(self):
        return f"Name -> {self.name}, ID -> {self.id}, Department -> {self.department}, University -> {self.university}"

s = Student("Anik", 18101073, "CSE")
print(s)

s.show()
Student.show(s)

s.from_class()
Student.from_class()

s.staticMethod()
Student.staticMethod()

s.staticMethodWithArgument("Only God Know.")
Student.staticMethodWithArgument("Angel Moyuri")

