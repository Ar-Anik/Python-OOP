class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        print(f"Deleting {self._name}'s name.")
        del self._name

person = Person("Jhon")

print(person.name)
person.name = "Mike"

print(person.name)
del person.name
