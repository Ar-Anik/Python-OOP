class Company:
    def __init__(self, name):
        self.name = name

    class Department:
        def __init__(self, name, employee_count, manager_name):
            self.name = name
            self.employee_count = employee_count
            self.manager_name = manager_name
            self.projects = []

        def describe(self):
            return f"{self.name} department has {self.employee_count} employees, managed by {self.manager_name}"

    class Project:
        def __init__(self, name, description):
            self.name = name
            self.description = description

class SoftwareCompany(Company):
    def __init__(self, name):
        super().__init__(name)

    class EngineeringDepartment(Company.Department):
        def __init__(self, name, employee_count, manager_name):
            super().__init__(name, employee_count, manager_name)

    class FrontendTeam(EngineeringDepartment):
        def __init__(self, name, employee_count, manager_name):
            super().__init__(name, employee_count, manager_name)

    class BackendTeam(EngineeringDepartment):
        def __init__(self, name, employee_count, manager_name):
            super().__init__(name, employee_count, manager_name)

class UIUXSubgroup(SoftwareCompany.FrontendTeam):
    def __init__(self, name, employee_count, manager_name, design_tool):
        super().__init__(name, employee_count, manager_name)
        self.design_tool = design_tool

    def describe(self):
        description = super().describe()
        return f"{description}. They use {self.design_tool} for UI/UX design."


class DatabaseSubgroup(SoftwareCompany.BackendTeam):
    def __init__(self, name, employee_count, manager_name, database_tool):
        super().__init__(name, employee_count, manager_name)
        self.database_tool = database_tool

    def describe(self):
        description = super().describe()
        return f"{description} They use {self.database_tool} for database management."


# Create a software company
my_company = SoftwareCompany("XYZ Limited")

# Create departments and teams
engineering_dept = my_company.EngineeringDepartment("Engineering", 100, "John Doe")
frontend_team = my_company.FrontendTeam("Frontend", 30, "Jane Smith")
uiux_subgroup = UIUXSubgroup("UI/UX", 10, "Alice Johnson", "Figma")
backend_team = my_company.BackendTeam("Backend", 50, "Bob Brown")
database_subgroup = DatabaseSubgroup("Database", 20, "Charlie Green", "MySQL")

# Assign projects
frontend_team.projects.append(my_company.Project("Website Redesign", "Redesigning company website"))
backend_team.projects.append(my_company.Project("Database Migration", "Migrating database to a new server"))

# Describe the company structure and projects
print(engineering_dept.describe())
print(frontend_team.describe())
print(uiux_subgroup.describe())
print(backend_team.describe())
print(database_subgroup.describe())

print("\nProjects:")
for team in [frontend_team, backend_team]:
    for project in team.projects:
        print(f"{team.name} is working on project '{project.name}': {project.description}")

print(DatabaseSubgroup.__mro__)
