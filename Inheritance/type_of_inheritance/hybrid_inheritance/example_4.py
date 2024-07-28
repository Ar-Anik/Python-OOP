class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name : {self.name}, Age : {self.age}")


class Employee(Person):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Employee ID : {self.employee_id}, Department : {self.department}")


class Faculty(Employee):
    def __init__(self, name, age, employee_id, department, position):
        super().__init__(name, age, employee_id, department)
        self.position = position

    def display_info(self):
        super().display_info()
        print(f"Position : {self.position}")


class Course:
    def __init__(self, course_code, course_name, credits):
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits

    def display_info(self):
        print(f"Course Code : {self.course_code}, Course Name: {self.course_name}, Course Credit: {self.credits}")


class Student(Person):
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age)
        self.student_id = student_id
        self.major = major
        self.course_enrolled = []

    def enroll_course(self, course):
        self.course_enrolled.append(course)

    def display_info(self):
        super().display_info()
        print(f"Student ID : {self.student_id}, Major : {self.major}")
        print("Course Schedule : ")
        for course in self.course_enrolled:
            course.display_info()


class Department:
    def __init__(self, department_name, department_head):
        self.department_name = department_name
        self.department_head = department_head

    def display_info(self):
        print(f"Department : {self.department_name}, Department Head : {self.department_head.display_info()}")


class CourseSchedule:
    def __init__(self, department_name):
        self.department_name = department_name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def display_schedule(self):
        print(f"Department: {self.department_name}")
        print("Course Schedule : ")
        for course in self.courses:
            course.display_info()


class UniversitySystem(Department, CourseSchedule):
    def __init__(self, department_name, department_head):
        Department.__init__(self, department_name, department_head)
        CourseSchedule.__init__(self, department_name)

    def add_course(self, course):
        CourseSchedule.add_course(self, course)

    def display_info(self):
        super().display_info()
        print("Course Schedule : ")
        CourseSchedule.display_schedule(self)


faculty_1 = Faculty("John Doe", 40, "F001", "Computer Science", "Professor")
university_system = UniversitySystem("Computer Science", faculty_1)

course_1 = Course("CS101", "Introduction to Computer Science", 3)
course_2 = Course("CS202", "Data Structures and Algorithms", 4)

university_system.add_course(course_1)
university_system.add_course(course_2)

university_system.display_info()

student1 = Student("Alice Smith", 20, "S001", "Computer Science")
student2 = Student("Bob Johnson", 21, "S002", "Computer Science")
student1.enroll_course(course_1)
student2.enroll_course(course_2)

student1.display_info()
student2.display_info()