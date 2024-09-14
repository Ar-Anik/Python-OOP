"""
This method allows objects to be hashable, meaning they can be used in sets or as keys in dictionaries.
"""

class HashablePoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        # Hashing the object based on its x and y coordinates
        return hash((self.x, self.y))

    def __eq__(self, other):
        # Equality comparison based on coordinates
        return isinstance(other, HashablePoint) and self.x == other.x and self.y == other.y

p1 = HashablePoint(1, 2)
p2 = HashablePoint(1, 2)
p3 = HashablePoint(10, 15)

# Calling hash() directly
print(hash(p1))
print(hash(p3))

# Or, call the __hash__() method directly
print(p1.__hash__())
print(p3.__hash__())

# make a set by object, when make a set each object will be hashed.
my_set = {p1, p2, p3}
print(len(my_set))  # Output: 2 (since p1 and p2 are considered equal due to the hash method)
