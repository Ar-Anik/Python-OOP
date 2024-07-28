class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        print(f"Name : {self.name}, ID: {self.employee_id}, Salary: {self.salary} ")


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department
        self.subordinates = []

    def add_subordinate(self, employee):
        if isinstance(employee, Employee):
            self.subordinates.append(employee)
            print(f"{employee.name} added as a subordinate to {self.name}")
        else:
            print(f"Invalid Employee Type. Could not add Subordinate.")

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")
        if self.subordinates:
            print("Subordinates : ")
            for subordinates in self.subordinates:
                subordinates.display_info()


class Executive(Manager):
    def __init__(self, name, employee_id, salary, department, stock_options):
        super().__init__(name, employee_id, salary, department)
        self.stock_options = stock_options

    def display_info(self):
        super().display_info()
        print(f"Stock Options : {self.stock_options}")


class Intern(Employee):
    def __init__(self, name, employee_id, salary, supervisor):
        super().__init__(name, employee_id, salary)
        self.supervisor = supervisor

    def display_info(self):
        super().display_info()
        print(f"Supervisor : {self.supervisor}")


ceo = Executive("John Doe", "CEOOO1", 1000000, "Executive", 100)
ceo.display_info()

cto = Manager("Jane Smith", "CT0001", 300000, "Engineering")
engineer1 = Employee("Anik", "ENG290", 10000)
intern1 = Intern("Alice Johnson", "INT001", 5000, "Anik")

cto.add_subordinate(engineer1)
cto.add_subordinate(intern1)

cto.display_info()
