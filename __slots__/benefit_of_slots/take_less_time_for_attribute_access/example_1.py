from timeit import timeit

class PersonWithDict:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class PersonWithSlots:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age

p_dict = PersonWithDict('Anik', 14)
p_slots = PersonWithSlots('Anik', 14)

num_instance = 1000000

# globals() function is used to pass the current global scope, This allows the code (the stmt argument) to access variables, functions, or objects that are defined outside the immediate string that timeit() is executing.
time_dict_access = timeit("p_dict.name", globals=globals(), number=num_instance)
print(f"TIme for attribute access without __slots__ : {time_dict_access:.4f} seconds.")

time_slots_access = timeit("p_slots.name", globals=globals(), number=num_instance)
print(f"Time for attribute access with __slots__: {time_slots_access:.4f} seconds.")

"""
The class with __slots__ will usually have a slightly faster attribute access time because accessing attributes from a tuple or array (used internally by __slots__) is quicker 
than looking them up in a dictionary (__dict__).
"""
