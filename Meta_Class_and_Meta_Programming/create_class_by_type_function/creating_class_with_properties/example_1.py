def get_name(self):
    print("name get")
    return self._name

def set_name(self, value):
    print("name set")
    self._name = value

def delete_name(self):
    print("name delete")
    del self._name

name_property = property(get_name, set_name, delete_name)

Person = type('Person', (), {'name': name_property})

person = Person()
person.name = "Anik"

print(person.name)

del person.name
