"""
The __reduce__() method is used internally by the pickle module to define how an object should be serialized. You can override this method to customize the
pickling behavior of your class, especially if your object needs special handling during serialization.
"""

import pickle

from object_serialization_and_deserialization import pickled_data


class CustomPickleClass:
    def __init__(self, data):
        self.data = data

    def __reduce__(self):
        # Custom reduce method to control how the object is serialized
        return (CustomPickleClass, (self.data,))


obj = CustomPickleClass([1,2,3])

# Serialize the object
pickled_obj = pickle.dumps(obj)
print("Serialized Data : ", pickled_obj)

unpickled_obj = pickle.loads(pickled_obj)
print("Unserialized Data : ", unpickled_obj.data)

