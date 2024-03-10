# We can check wheter the object passed to the method has the method being invoked or not.
# hasattr() function is used to check whether the object has a method or not.
# like : hasattr(object, attribute), where attribute can be a method or variable. If it is found in the object then this method returns True else False.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

class Course:
    def __init__(self, code, title):
        self.code = code
        self.title = title

class Department:
    def __init__(self, name, head):
        self.name = name
        self.head = head
        self.courses = []

class University:
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments

student_1 = Student("Alice", 20, "A123")
student_2 = Student("Bob", 22, "B456")

course_1 = Course("CS101", "Introduction to Computer Science")
course_2 = Course("ENG201", "Advanced English")

department_1 = Department("Computer Science", Person("Dr.Smith", 45))
department_1.courses.append(course_1)

department_2 = Department("English", Person("Prof. Johnson", 50))
department_2.courses.append(course_2)

university = University("Tech University", [department_1])

def check_attribute(obj, attributes):
    current_obj = obj
    for attribute in attributes:
        if type(current_obj) == list:
            if hasattr(current_obj[0], attribute):
                current_obj = getattr(current_obj[0], attribute)
        elif hasattr(current_obj, attribute):
            current_obj = getattr(current_obj, attribute)
        else:
            return None
    return current_obj

attributes_to_check = ["departments", "courses", "title"]
result = check_attribute(university, attributes_to_check)

if result is not None:
    print("Result : ", result)
else:
    print("Attribute not found or structure doesn't match.")
