class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.employee_id}, Salary: {self.salary}")


class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def write_code(self):
        print(f"{self.name} is writting code in {self.programming_language}")


class TeamLead(Developer):
    def __init__(self, name, employee_id, salary, programming_language, team_size):
        super().__init__(name, employee_id, salary, programming_language)
        self.team_size = team_size

    def conduct_meeting(self):
        print(f"{self.name} is conducting a meeting with the team")


class ProjectManager(TeamLead):
    def __init__(self, name, employee_id, salary, programming_language, team_size, project_name):
        super().__init__(name, employee_id, salary, programming_language, team_size)
        self.project_name = project_name

    def oversee_project(self):
        print(f"{self.name} is overseeing the project: {self.project_name}")


developer = Developer("Alice", "DEV001", 80000, "Python")
developer.display_info()
developer.write_code()

team_lead = TeamLead("Bob", "TL001", 100000, "Java", 5)
team_lead.display_info()
team_lead.write_code()
team_lead.conduct_meeting()

project_manager = ProjectManager("Charlie", "PM001", 1200000, "JS", 10, "Web Application")
project_manager.display_info()
project_manager.write_code()
project_manager.conduct_meeting()
project_manager.oversee_project()