def __init__(self, name):
    self._name = name

def get_name(self):
    return self._name

def set_name(self, name):
    self._name = name

name_property = property(get_name, set_name)

Person = type('Person', (), {
    'name': name_property,
    '__init__': __init__
})

person = Person("Anik")
print(person.name)

person.name = "Aubdur Rob"
print(person.name)
