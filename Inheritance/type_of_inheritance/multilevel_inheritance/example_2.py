class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name : {self.name}, Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Employee ID : {self.employee_id}, Department: {self.department}")


class FacultyMember(Employee):
    def __init__(self, name, age, employee_id, department, research_interests):
        super().__init__(name, age, employee_id, department)
        self.research_interests = research_interests

    def display_info(self):
        super().display_info()
        print(f"Research Innterests: {', '.join(self.research_interests)}")


class Professor(FacultyMember):
    def __init__(self, name, age, employee_id, department, research_interests, publications):
        super().__init__(name, age, employee_id, department, research_interests)
        self.publications = publications

    def display_info(self):
        super().display_info()
        print(f"Publications : {', '.join(self.publications)}")


class AssistantProfessor(Professor):
    def __init__(self, name, age, employee_id, department, research_interests, publications, teaching_load):
        super().__init__(name, age, employee_id, department, research_interests, publications)
        self.teaching_load = teaching_load

    def display_info(self):
        super().display_info()
        print(f"Teaching Load : {self.teaching_load}")


professor_1 = Professor("John Smith", 45, "PROF001", "Compter Science", ["Machine Learning", "Data Science"], ["A. Smith et al.", "Journal of AI"])
professor_1.display_info()

assistant_professor_1 = AssistantProfessor("Bob Johnson", 35, "ASST001", "Mathematics", ["Number Theory", "Algebra"], ["C. Johnson et al., Journal of Mathematics"], "Introductory Courses")
assistant_professor_1.display_info()