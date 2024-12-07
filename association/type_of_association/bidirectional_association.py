"""
Bidirectional Association: In a bidirectional association, both classes are aware of each other and can interact mutually.
"""

class Employer:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay
        self.employees = []      # List of Reference to Employee

    def assign_employee(self, employee):
        self.employees.append(employee)
        employee.employer = self

class Employee:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay
        self.employer = None

anik = Employer("Anik", 23, 100000)

anika = Employee("Anika", 45, 80000)
sourov = Employee("Sourov", 30, 90000)
oni = Employee("Oni", 27, 85000)

anik.assign_employee(anika)
anik.assign_employee(sourov)
anik.assign_employee(oni)

print(f"Employer: {anik.name}")
print("Employees:")
for emp in anik.employees:
    print(f"- {emp.name}, Age: {emp.age}, Pay: {emp.pay}")

# Each employee can reference their employer
print(f"\n{anika.name}'s Employer: {anika.employer.name}")
print(f"{sourov.name}'s Employer: {sourov.employer.name}")
print(f"{oni.name}'s Employer: {oni.employer.name}")


"""
Bidirectional Association occurs when both classes are aware of and can reference each other. In this case:
    1. The Employer class maintains a reference to its employees through the employees list.
    2. Each Employee maintains a reference to its employer through the employer attribute.
"""
