"""
In single inheritance, only one subclass inherits from one parent class. There is a one-to-one relationship between the parent class and the subclass.
Multiple subclasses inheriting from the same parent class would be an example of hierarchical inheritance, not single inheritance.

Single Inheritance: Involves one subclass inheriting from one parent class. It is a one-to-one relationship between the parent class and the subclass.

Hierarchical Inheritance: Involves multiple subclasses inheriting from the same parent class. It is a one-to-many relationship between the parent class and multiple subclasses.
"""

class Employee:
    def __init__(self, name, age, employee_id):
        self.name = name
        self.age = age
        self.employee_id = employee_id

    def display_info(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Employee ID : {self.employee_id}")


class FullTimeEmployee(Employee):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age, employee_id)
        self.salary = salary

    def calculate_salary(self):
        return self.salary * 12

    def display_info(self):
        super().display_info()
        print(f"Type : Full-Time Employee")
        print(f"Annual Salary : ${self.calculate_salary():,.2f}")


class PartTimeEmployee(Employee):
    def __init__(self, name, age, employee_id, hourly_rate, hours_worked):
        super().__init__(name, age, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    def display_info(self):
        super().display_info()
        print(f"Type : Part-Time Employee")
        print(f"Monthly Salary : ${self.calculate_salary():,.2f}")


class ContractEmployee(Employee):
    def __init__(self, name, age, employee_id, contract_duration, hourly_rate):
        super().__init__(name, age, employee_id)
        self.contract_duration = contract_duration
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        # 40: This represents the number of hours worked per week.
        # 4: This represents the number of weeks in a month.
        return self.hourly_rate * 40 * 4 * self.contract_duration

    def display_info(self):
        super().display_info()
        print(f"Type : Contract Employee")
        print(f"Total Contract Salary : ${self.calculate_salary():,.2f}")


full_time_emp = FullTimeEmployee("Alice", 30, "FT001", 50000)
part_time_emp = PartTimeEmployee("Bob", 25, "PT001", 30, 120)
contract_emp = ContractEmployee("Charlie", 35, "CT001", 6, 50)

print("Full Time Employee Information : ")
full_time_emp.display_info()

print("\nPart Time Employee Information : ")
part_time_emp.display_info()

print("\nContract Employee Information : ")
contract_emp.display_info()