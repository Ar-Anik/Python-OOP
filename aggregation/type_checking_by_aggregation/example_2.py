from typing import List

# Employee class representing an individual employee
class Employee:
    def __init__(self, emp_id: int, name: str, position: str):
        self.emp_id = emp_id
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.name} (ID: {self.emp_id}) - {self.position}"


class Department:
    def __init__(self, dept_id: int, dept_name: str):
        self.dept_id = dept_id
        self.dept_name = dept_name
        self.employees: List[Employee] = []

    def add_employee(self, employee):
        if not isinstance(employee, Employee):
            raise TypeError("Only objects of type 'Employee' can be added to the department.")
        self.employees.append(employee)
        print(f"Employee {employee} added to department {self.dept_name}.")

    def list_employees(self):
        print(f"Employees in {self.dept_name} Department:")
        if not self.employees:
            print("No employees in this department.")
        else:
            for emp in self.employees:
                print(f" - {emp}")

    def get_employee_count(self):
        return len(self.employees)


try:
    anik = Employee(1, "Anik", "Software Engineer")
    sourov = Employee(2, "Sourob", "Data Analyst")
    shawon = Employee(3, "shawon", "Project Manager")

    it_department = Department(101, "IT")

    it_department.add_employee(anik)
    it_department.add_employee(sourov)

    it_department.add_employee(shawon)

    it_department.list_employees()

    print(f"Total Employees: {it_department.get_employee_count()}")

    it_department.add_employee("Random String")  # This will raise a TypeError

except TypeError as e:
    print(e)
