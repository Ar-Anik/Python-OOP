from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def introduce(self):
        pass


class Parent(Person):
    def __init__(self, name, age, occupation):
        super().__init__(name, age)
        self.occupation = occupation

    def display(self):
        return f"Name: {self.name}, Age: {self.age}, Occupation: {self.occupation}"


class Child(Parent):
    def __init__(self, name, age, occupation, grade):
        super().__init__(name, age, occupation)
        self.grade = grade

    def introduce(self):
        return f"I am {self.name}, a {self.age}-year-old {self.occupation} in {self.grade} grade."

child = Child("Jane Doe", 12, "Student", "6th")

print(child.display())
print(child.introduce())

'''
    must be callable function have all abstract method implemented
'''

# parent = Parent("John Doe", 45, "Engineer")
