# https://www.geeksforgeeks.org/python-oops-aggregation-and-composition/
# https://www.codechef.com/learn/course/oops-concepts-in-python/CPOPPY04/problems/ADVPPY35

"""
Learning About Aggregation : 
    1. What is Aggregation ?
    2. Key Characteristics of Aggregation.
    3. Differentiate Aggregation from Composition
    4. Introduce Abstract Base Classes (ABCs) in Aggregation
    5. Explore Dynamic Aggregation
    6. Implement basic validation
    7. Type checking
    8. Key Design Patterns Using Aggregation : Factory Pattern, Observer Pattern.
"""

"""
---> Aggregation is a "has-a" relationship where one object is a container (whole) and contains references to other objects (parts). A Library has 
many Books, but a Book can exist without the Library.

---> Aggregation is a special form of association between classes where one class contains a reference to another class, representing a "has-a" 
relationship. Unlike composition, in aggregation, the contained object can exist independently of the container object.

"""

"""
Key Characteristics : 
    1. Weak Ownership: The contained object can exist separately from the container
    2. Independent Lifecycle: The contained object can be shared among multiple container objects.
    3. Loose Coupling: The objects are less tightly integrated compared to composition. Aggregation reduces dependencies, making the design more 
       modular and flexible.
    4. Unidirectional Association : Aggregation is a unidirectional association. i.e. a one-way relationship. For example, a department can have 
       students but vice versa is not possible and thus unidirectional in nature.
"""

class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay * 12) + (self.bonus * 2)


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.obj_salary = salary

    def total_salary(self):
        return self.obj_salary.annual_salary()

salary = Salary(20000, 10000)
emp = Employee("Anik", 14, salary)

print("Employee Total Salary : ", emp.total_salary())

