from time import time

class PersonWithDict:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class PersonWithSlots:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age

num_instances = 1000000

# Measure time for class without __slots__
start_time = time()
person_with_dict = [PersonWithDict(f"Person_{i}", i) for i in range(num_instances)]
end_time = time()
print(f"Time taken without slots : {end_time - start_time}")


# Measure time for class with __slots__
start_time = time()
person_with_slots = [PersonWithSlots(f"Person_{i}", i) for i in range(num_instances)]
end_time = time()
print(f"Time taken with slots : {end_time - start_time}")

