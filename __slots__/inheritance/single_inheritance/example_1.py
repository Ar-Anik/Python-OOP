"""
In the case of single inheritance, the __slots__ feature works to limit the attributes for both the parent and child classes.
"""

class Animal:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    __slots__ = ['breed']

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

dog = Dog("Modi", 5, 'Golden Retriever')

print("Name : ", dog.name)
print("Age : ", dog.age)
print("Breed : ", dog.breed)

# print(dog.__dict__)       #AttributeError: 'Dog' object has no attribute '__dict__'

# Trying to add a new attribute dynamically would result in an error
# dog.color = 'Brown'     # Raises AttributeError: 'Dog' object has no attribute 'color'

"""
1. __slots__ in Parent and Child Classes: When the parent class uses __slots__, the child class can define its own __slots__ for additional attributes. Both slots lists work together, 
                                          and instances will not have a __dict__ attribute.

2. Inheritance with __slots__: In single inheritance, you can add slots in the child class, and the memory savings are applied to both the parent and child class's attributes.

3. Memory Efficiency: Using __slots__ reduces the memory footprint by avoiding the need for an internal dictionary for each instance.
"""
