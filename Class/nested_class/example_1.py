# A nested class is a class declared within another class

class OuterClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def write(self):
        print("This is from outer method")
        print(f"Name : {self.name}, Age : {self.age}")

    class InnerClass:
        def __init__(self, id, country):
            self.id = id
            self.country = country

        def inner_write(self):
            print("This is from innner method")
            print(f"Id : {self.id}, Country: {self.country}")


outer = OuterClass("Anik", 14)
outer.write()

firstWay = OuterClass.InnerClass(1001, "Bangladesh")
firstWay.inner_write()

secondWay = outer.InnerClass(1002, "India")
secondWay.inner_write()
