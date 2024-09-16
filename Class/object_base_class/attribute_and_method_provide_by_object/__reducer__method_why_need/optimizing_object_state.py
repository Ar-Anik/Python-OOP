"""
Sometimes, we want to serialize only part of an object's state or transform it into a more compact form during serialization. The __reduce__() method allows us
to reduce the amount of data that gets pickled by controlling what part of the object's state should be serialized.
"""

import pickle

class LargeObject:
    def __init__(self, data):
        self.data = data
        self.cache = [i for i in range(1000000)]

    def __reduce__(self):
        # customizing pickling to exclude the cache
        return (self.__class__, (self.data,))

obj = LargeObject("important_data")

# pickling the object without the large cache
pickled_obj = pickle.dumps(obj)
print("Serialized Object : ", pickled_obj)

deserialize_obj = pickle.loads(pickled_obj)
print("Deserialized Object : ", deserialize_obj.data, deserialize_obj.cache)

"""
In this case, we don't want to pickle the cache because it’s just a temporary large structure that can be rebuilt upon deserialization. 
The __reduce__() method allows us to exclude it from the serialized form.
"""
