class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = []

    def enroll(self, course):
        self.course.append(course)
        print(f"{self.name} has enrolled in {course}")

    def display_info(self):
        super().display_info()
        print(f"Student ID : ", self.student_id)
        print(f"Course Enrolled : ", end="")
        for course in self.course:
            print(course, end=", ")


std = Student("Anik", 14, 18101073)
std.enroll("Computer Science")
std.enroll("Mathematics")
print(std.course)
std.display_info()