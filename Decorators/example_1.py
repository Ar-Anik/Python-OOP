# without decorator syntax
def validate_age(method):
    def wrapper(self, age):
        if age < 0:
            raise ValueError("Age Cannot Be Negative")
        method(self, age)
    return wrapper

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_age(self, age):
        self.age = age

Person.set_age = validate_age(Person.set_age)
print("Name of set_age function after : ", Person.set_age.__name__)

p = Person("Anik", 20)
p.set_age(14)
print(f"Name : {p.name}, Age : {p.age}")


# With Decorator Syntax

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @validate_age
    def set_age(self, age):
        self.age = age

print("In Human Class name of the set_age function : ", Human.set_age.__name__)

h = Human("Sourav", 22)
h.set_age(21)

print(f"Name : {h.name}, Age : {h.age}")
