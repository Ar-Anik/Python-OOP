"""
Pympler is a Python module for analyzing memory usage in your Python programs. The asizeof function from pympler.asizeof
measures the memory footprint of objects.
"""

from pympler import asizeof

class WithOutSlots:
    def fun(self):
        self.university = "UAP"


class WithSlots:
    __slots__ = ('name', 'age', 'university')


obj = WithOutSlots()
obj.name = "Anik"
obj.age = 14
obj.fun()


obj_s = WithSlots()
obj_s.name = "Anik"
obj_s.age = 14
obj_s.university = "UAP"

# Measure memory size of the object in bytes
print(f"Size of Object Without Slots : {asizeof.asizeof(obj)} bytes.")
print(f"Size of Object With Slots : {asizeof.asizeof(obj_s)} bytes.")

"""
Pympler is a Python module for analyzing memory usage in your Python programs. The asizeof function from pympler.asizeof 
measures the memory footprint of objects. It recursively tracks all components of an object to get the full size in bytes.
"""

def print_fun(lst):
    for key, val in lst:
        print(f"{key}: {val}")


def get_attributes(objt):
    if hasattr(objt, '__slots__'):
        return [(attr, getattr(objt, attr)) for attr in objt.__slots__ if hasattr(objt, attr)]
    else:
        return [(key, val) for key, val in objt.__dict__.items()]


print_fun(get_attributes(obj))
print_fun(get_attributes(obj_s))
