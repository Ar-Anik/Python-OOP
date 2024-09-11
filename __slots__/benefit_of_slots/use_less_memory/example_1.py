# The object with __slots__ uses less memory because it doesn't have a __dict__.

import sys

class WithoutSlots:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class WithSlots:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age


obj_without_slots = WithoutSlots("Anik", 14)
obj_with_slots = WithSlots("Anik", 14)

print(f"Memory Usage Without Slots : {sys.getsizeof(obj_without_slots.__dict__)}")
print(f"Memory Usage With Slots : {sys.getsizeof(obj_with_slots)}")
