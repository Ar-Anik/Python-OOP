"""
When only the parent class has __slots__ and the child class does not, the child class will revert to using the standard instance attribute storage mechanism (__dict__).
However, the parent class's memory efficiency will still apply to the attributes defined within its __slots__. In this scenario, the child class can still add attributes
dynamically through the standard __dict__, while the attributes defined in the parent class's __slots__ are managed using the memory-efficient mechanism.
"""

class Animal:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age

# class without __slots__
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def __str__(self):
        return f"Name : {self.name}, Age : {self.age}, Breed : {self.breed}"

dog = Dog("Putin", 5, "Golden Retriever")

print(hasattr(dog, '__dict__'))
print(hasattr(dog, '__slots__'))

print("Instance Dictionary : ", dog.__dict__)
print("Instance Slots : ", dog.__slots__)

# Dog class doesn't have __slots__, we can add new attributes dynamically
dog.color =  'Brown'
print(dog)
print(dog.color)

"""
----> The attributes defined in the parent's __slots__ will still benefit from the memory optimization. However, any attributes defined or dynamically added in the child class will be 
stored in the standard __dict__, and those attributes won't get the memory savings.

----> The parent class's __slots__ restricts dynamic attribute assignment for the parent, but the child class without __slots__ allows dynamic attribute addition, and attributes in the 
child class are stored in the normal way using __dict__.
"""
