def greet(self):
    print(f"Hello, my name is {self.name}")

Person = type('Person', (), {'name': 'Anik', 'greet': greet})

person = Person()
print(person.name)
person.greet()
