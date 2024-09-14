# __sizeof__ method returns the size of the object in bytes.

class Myclass:
    def __init__(self, data):
        self.data = data

    def __sizeof__(self):
        # Returning the size of the object, including the size of the data attribute
        return super().__sizeof__() + self.data.__sizeof__()
        

obj = Myclass([1, 2, 3, 4, 5, 6])

print(obj.__sizeof__())    # Output: size in bytes (depends on system)
