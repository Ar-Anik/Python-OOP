class Data:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

person = Data("Anik", "01243647385")
print("Name : ", person.name)

del person.name

print(person.__dict__)

del person

print(person)    # NameError: name 'person' is not defined
