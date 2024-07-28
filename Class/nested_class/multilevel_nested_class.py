class Company:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    class Department:
        def __init__(self, name):
            self.name = name
            self.teams = []

        def add_team(self, team):
            self.teams.append(team)

        class Team:
            def __init__(self, name):
                self.name = name
                self.employees = []

            def add_employee(self, employee):
                self.employees.append(employee)

            class Employee:
                def __init__(self, name, position, id):
                    self.name = name
                    self.position = position
                    self.id = id

    def print_hierarchy(self):
        print(f"Company : {self.name}")
        for department in self.departments:
            print(f"- Department: {department.name}")
            for team in department.teams:
                print(f"  - Team: {team.name}")
                for employee in team.employees:
                    print(f"    - Employee: {employee.name}, Position: {employee.position}, ID : {employee.id}")


my_company = Company("XYZ-Company" )

hr_department = my_company.Department("HR")
engineering_department = my_company.Department("Engineering")

my_company.add_department(hr_department)
my_company.add_department(engineering_department)

hr_recruitment_team = hr_department.Team("Recruitment")
engineering_dev_team = engineering_department.Team("Development")

hr_department.add_team(hr_recruitment_team)
engineering_department.add_team(engineering_dev_team)

hr_recruitment_team.add_employee(hr_department.Team.Employee("Alice", "HR Manager", "1001"))
hr_recruitment_team.add_employee(hr_recruitment_team.Employee("Bob", "HR Assistant", "1002"))
engineering_dev_team.add_employee(engineering_dev_team.Employee("Charlie", "Software Engineer", "1003"))
engineering_dev_team.add_employee(engineering_dev_team.Employee("David", "Hardware Engineer", "1004"))

my_company.print_hierarchy()

print(my_company.Department.Team.Employee.__mro__)
