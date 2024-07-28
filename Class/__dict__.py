# __dict__ is a built in function. __dict__ function is a dictionary of Class and object attribute save like key-value pair

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def write(self):
        print("Name : ", self.name)
        print("Age : ", self.age)

person_one = Person("Aubdur Rob Anik", 14)
person_two = Person("Jafrin", 13)

print(Person.__dict__)
print(person_one.__dict__)
print(person_two.__dict__)
