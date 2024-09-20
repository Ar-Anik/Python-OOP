"""
If we want to still have a __dict__ for dynamic attributes while using __slots__, we can explicitly define it by including '__dict__' in the __slots__ definition.
"""

class Person:
    __slots__ = ['name', 'age', '__dict__']

    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Anik", 14)
p.address = "Gulistan, Bangobondu Avenue"

print(p.name, p.age, p.address)

print(hasattr(p, '__dict__'))
print(p.__dict__)

"""
In this case, memory is still allocated for both the fixed attributes defined in __slots__ and the dynamic attributes stored in __dict__. As a result, memory savings 
are diminished or eliminated. Including __dict__ in __slots__ is similar to a normal object that doesn’t use __slots__.
"""
