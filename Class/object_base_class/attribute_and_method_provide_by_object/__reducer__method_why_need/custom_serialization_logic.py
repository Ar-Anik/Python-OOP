"""
In some cases, an object's internal state may require special handling during serialization. For example, the object might hold
resources that cannot be directly serialized (e.g., open file handles, database connections, sockets, etc.). You might need to
define how to save the state of the object and how to recreate it during deserialization.
"""

import pickle

class FileHandler:
    def __init__(self, filepath):
        self.filepath = filepath
        self.file = open(filepath, "r")

    def __reduce__(self):
        # Customizing pickling to only store the filepath, not the file object (which can't be pickled)
        return (FileHandler, (self.filepath,))

handler = FileHandler("example.txt")

print("File open in read mode : ", handler.file)

# Serialized the object
pickle_obj = pickle.dumps(handler)
print("Serialized Object : ", pickle_obj)

# Deserialized object
unpickle_obj = pickle.loads(pickle_obj)
print("Unserialized Object : ", unpickle_obj.filepath)
