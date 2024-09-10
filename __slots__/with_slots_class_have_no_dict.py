"""
In Python, the __slots__ mechanism is used to prevent the automatic creation of a __dict__ for instances of a class,
thereby saving memory by avoiding the overhead associated with dynamic attribute management. Normally, instances of Python
classes store their attributes in a dictionary (__dict__). However, by using __slots__, you define a fixed set of attributes
for each instance, and the instance won’t have a __dict__ attribute.
"""

class Person:
    __slots__ = ['name', 'age']

p = Person()
p.name = "Aubdur Rob Anik"
p.age = 14

print(f"{p.name} {p.age}")

print(p.__dict__)   # This will raise an error since __dict__ is not available
