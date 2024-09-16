"""
If our class has a non-standard constructor or if we want to customize how an object is re-created after unpickling, we can use __reduce__()
to specify how the constructor should be called.
"""
import pickle

class CustomConstructor:
    def __init__(self, value, multiplier):
        self.value = value
        self.result = value * multiplier

    def __reduce__(self):
        # Customize unpickling by specifying how to call the constructor
        return (self.__class__, (self.value, 2))

obj = CustomConstructor(5, 3)
print("Result : ", obj.result)

serialized_obj = pickle.dumps(obj)
deserialize_obj = pickle.loads(serialized_obj)
print("After Deserialized Result : ", deserialize_obj.result)
