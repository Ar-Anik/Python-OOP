class University:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.professors = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_professor(self, professor):
        self.professors.append(professor)

    def add_course(self, course):
        self.courses.append(course)

    class Student:
        def __init__(self, name, id, semester):
            self.name = name
            self.id = id
            self.semester = semester
            self.courses_taken = []

        def enroll(self, course):
            self.courses_taken.append(course)

    class Professor:
        def __init__(self, name, id, department):
            self.name = name
            self.id = id
            self.department = department
            self.courses_taught = []

        def assign_course(self, course):
            self.courses_taught.append(course)

    class Course:
        def __init__(self, name, code, professor):
            self.name = name
            self.code = code
            self.professor = professor
            self.students_enrolled = []

        def enroll_student(self, student):
            self.students_enrolled.append(student)


my_university = University("University of Asia Pacific")

professor_1 = my_university.Professor("John Doe", "101", "Computer Science");
my_university.add_professor(professor_1)

course_1 = my_university.Course("Introduction to Python", "CS101", professor_1)
my_university.add_course(course_1)

student_1 = my_university.Student("Anik", "18101073", "3-2")
my_university.add_student(student_1)
student_1.enroll(course_1)

course_1.enroll_student(student_1)

print(f"University : {my_university.name}")

print("Professors : ")
for professor in my_university.professors:
    print(f"- {professor.name}, Department: {professor.department}")

print("Students : ")
for student in my_university.students:
    print(f"- {student.name}, ID: {student.id}, Courses Taken: {[course.name for course in student.courses_taken]}")

print("Courses : ")
for course in my_university.courses:
    print(f"- {course.name}, Code: {course.code}, Professor: {course.professor.name}")
