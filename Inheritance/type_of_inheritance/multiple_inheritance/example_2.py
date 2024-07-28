class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name : {self.name}, Age: {self.age}")


class Employee:
    def __init__(self, employee_id, department):
        self.employee_id = employee_id
        self.department = department

    def display_employee_info(self):
        print(f"Employee ID : {self.employee_id}, Department: {self.department}")


class FullTimeEmployee(Person, Employee):
    def __init__(self, name, age, employee_id, department, salary):
        # way-1
        # super().__init__(name, age)
        # Employee.__init__(self, employee_id, department)

        # way-2
        # super(Person, self).__init__(employee_id, department) does not mean that the parent class of Person is Employee. The super() function is used to refer to the next class in the Method Resolution Order (MRO).
        # When using super(Person, self), you're effectively asking Python to find the next class in the MRO after Person, and then call its __init__ method.
        # mro of FullTimeEmployee Class : (<class '__main__.FullTimeEmployee'>, <class '__main__.Person'>, <class '__main__.Employee'>, <class 'object'>)
        super().__init__(name, age)
        super(Person, self).__init__(employee_id, department)

        # way-3
        # Person.__init__(self, name, age)
        # Employee.__init__(self, employee_id, department)

        self.salary = salary

    def display_info(self):
        super().display_info()
        self.display_employee_info()
        print(f"Salary : {self.salary}")


class PartTimeEmployee(Person, Employee):
    def __init__(self, name, age, employee_id, department, hourly_rate, hours_worked):
        super().__init__(name, age)
        Employee.__init__(self, employee_id, department)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def display_info(self):
        super().display_info()
        self.display_employee_info()
        print(f"Hourly Rate : {self.hourly_rate}, Hours Worked: {self.hours_worked}")


# print(FullTimeEmployee.__mro__)
# print(PartTimeEmployee.__mro__)

full_time_employee = FullTimeEmployee("Alice", 30, "FT001", "Finance", 5000)
full_time_employee.display_info()

part_time_employee = PartTimeEmployee("Bob", 25, "PT001", "HR", 20, 25)
part_time_employee.display_info()

