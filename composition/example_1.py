class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        print(f"Class Name : ", self.__class__.__name__)
        return (self.pay * 12) + self.bonus

class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.salary = Salary(pay, bonus)

    def employee_total_salary(self):
        print(f"Name of ")
        return self.salary.annual_salary()

emp = Employee("Ar Anik", 18, 15000, 7500)
print("Employee Annual Salary : ", emp.employee_total_salary())
