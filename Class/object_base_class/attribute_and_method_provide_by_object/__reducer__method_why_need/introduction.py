"""
Why Use __reduce__()?
While many objects are simple and can be pickled automatically by Python without needing to override the __reduce__() method,
some objects are more complex or have special behavior that needs customization for correct pickling and unpickling. The __reduce__()
method gives you full control over how your object is serialized and deserialized.

Here are a few reasons why need the __reduce__() method:
1. when object has non-picklable components (e.g., open files, network connections).
2. when we want to customize or optimize what gets pickled/serialized-object.
3. when object has complex state or custom constructors. (Describe Below)
4. when dealing with cycles or special references between objects.


---> Object With Cycles or References or Custom Constructors : When dealing with objects that reference themselves or other objects with complex relationships,
                                                               Python might not know how to handle the references properly. The __reduce__() method can be used
                                                               to customize the way these references are saved and restored.
"""
