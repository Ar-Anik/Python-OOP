"""
In Python, "pickle" refers to the process of serializing and deserializing Python objects. The term comes from the pickle module, which is Python’s
built-in library for object serialization. The term "pickling" is a playful analogy to the process of preserving data, just as food is preserved by
pickling. In Python, pickling preserves the object state so that it can be reconstructed later.


# What is Serialization?
---> Serialization is the process of converting a Python object (like lists, dictionaries, custom classes, etc.) into a byte stream so that it can be
     saved to a file, sent over a network, or stored in a database. This byte stream can later be deserialized (unpickled) back into a Python object.


# Key Terms:
1. Pickling: The process of converting a Python object into a byte stream (serialization).
2. Unpickling: The reverse process of converting a byte stream back into a Python object (deserialization).


# Why Use Pickling?
1.Persistence: You can save the state of an object to disk and load it later.
2.Data Transfer: You can send a serialized object over a network, and the receiver can deserialize it to get the original object.
3.Caching: You can store the state of expensive computations and reuse it later.
"""

#  Basic example of pickling and unpickling work

import pickle

class ExamMark:
    def __init__(self, subject, mark):
        self.subject = subject
        self.mark = mark

obj = ExamMark("Math", 100)


# Pickling/Serializing the object to a byte stream
pickled_data = pickle.dumps(obj)
print("Serialized Object : ", pickled_data)

# Unpickling/deserializing the byte stream back to an object
unpickled_obj = pickle.loads(pickled_data)
print("Unpickled Object : ", unpickled_obj.subject, unpickled_obj.mark)
