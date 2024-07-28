class Information:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def write(self):
        for key, value in self.__dict__.items():
            print(f"{key.capitalize()} : {value}")

# By super() method call parent class method
class Person(Information):
    def __init__(self, name, age, phone, occupation):
        super().__init__(name, age, phone)
        self.occupation = occupation

    def write(self):
        super().write()

# By parent class called parent class method
class Student(Information):
    occupation = "Student"
    def __init__(self, name, id, age, phone, institution):
        Information.__init__(self, name, age, phone)
        self.id = "181010" + id
        self.institution = institution

    def write(self):
        Information.write(self)
        print("Occupation : ", self.occupation)

prsn = Person("Anik", 14, "01324563789", "Worker")
prsn.write()

std = Student("Sourov", "73", 14, "01425364785", "JU")
std.write()
