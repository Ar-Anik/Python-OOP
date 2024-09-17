"""
The __reduce__() method is used internally by the pickle module to define how an object should be serialized. You can override this method to customize the
pickling behavior of your class, especially if your object needs special handling during serialization.
"""

import pickle

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

"""
1. `Pickle` is Python’s built-in module for serializing and deserializing objects.
2. `Pickling` is the process of converting an object into a byte stream (serialization).
3. `Unpickling` is the reverse, converting a byte stream back into an object (deserialization).
"""

"""
When we call pickle.dumps(obj), Python follows these steps to serialize the object:

1. Inspecting the Object : Python first checks if the object obj can be pickled. If it’s a built-in type (like int, str, list), Python uses its internal 
mechanisms for pickling. If the object is an instance of a custom class, Python checks if the object has a __reduce__() method or a __getstate__() method.

2. Calling __reduce__(): If __reduce__() is defined in the object’s class, Python calls it. The __reduce__() method should return a tuple that specifies 
how the object should be pickled. This tuple typically contains:
        # Callable: A reference to the class or function that can recreate the object.
        # Arguments: A tuple of arguments needed to call that callable.
        # (Optional) State: A dictionary or other data that represents the internal state of the object, which can be used to restore the object's 
                            state after it is reconstructed.                                           

3. Pickling the Data: Based on the result of __reduce__(), Python serializes the class or callable, the arguments, and the internal state (if provided). 
This information is converted into a byte stream using pickle.dumps().
"""

"""
When we call pickle.loads(data) to deserialize the byte stream back into an object, Python follows these steps:

1. Recreate the Object: Python examines the byte stream to identify the callable and its arguments. If the __reduce__() method was used during pickling, 
Python retrieves the class and the arguments specified by __reduce__().

2. Calling the Callable: Python calls the class (or function) with the arguments returned by __reduce__(). This creates a new instance of the object.

3. Restoring the State: If additional state information (like a dictionary) was provided by __reduce__(), Python will also restore the object's internal 
state by setting the attributes or calling a method like __setstate__().
"""
