"""
Unidirectional Association: In this type of association, only one class is aware of and interacts with the other.
The second class is completely unaware of the first.
"""

class Employer:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

    def myWage(self):
        return self.pay

    def payDifference(self, other_pay):
        return self.pay - other_pay

class Employee:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

anik = Employer("Anik", 23, 100000)
anika = Employee("Anika", 45, 80000)

print(f"Pay Difference : {anik.payDifference(anika.pay)}")


"""
The Above example is Unidirectional Association : 
    1. The Employer class interacts with the Employee class by using the pay attribute of an Employee instance.
    2. The Employee class has no knowledge of the Employer class. It does not interact with or reference the Employer class in any way.
"""

