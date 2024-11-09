"""
The attribute lookup chain is the process Python uses to find an attribute when we try to access it on an object. It defines the order in which
Python searches for an attribute (like a variable or method) across different places. Understanding this chain is important because it influences
how Python interprets attribute access and decides what to return or whether to trigger certain methods (like those in descriptors).
"""

"""
# Step-by-Step Lookup Chain
1. Data Descriptors (Found in the Class or Any Parent Classes) : 
    1. Python first checks if the attribute is a data descriptor in the class or any of its parent classes (following the Method Resolution Order (MRO)).
    2. A data descriptor is an object that defines both a __get__ and a __set__ method (and possibly __delete__), giving it control over how the attribute is accessed and set.
    3. If Python finds a data descriptor for the attribute, it will:
        1. Call the descriptor's __get__ method when we try to read the attribute.
        2. Call the descriptor's __set__ method when we try to set the attribute.
    4. Data descriptors take precedence over instance attributes. This means that if both the instance dictionary and a data descriptor have the same attribute name, 
       Python will always use the data descriptor.
       
2. Instance Dictionary (__dict__ of the Instance) : 
    1. If there’s no data descriptor for the attribute in the class or parent classes, Python then checks the instance’s dictionary (__dict__) to see if the attribute 
       is defined directly on the instance.
    2. This dictionary contains all instance-specific attributes, which are usually assigned during instance creation (e.g., in __init__).
    3. If the attribute is found here, Python returns it directly.

3. Non-Data Descriptors (Found in the Class or Any Parent Classes) : 
    1. If the attribute isn’t in the instance dictionary, Python then checks the class and parent classes in the MRO for a non-data descriptor.
    2. A non-data descriptor is an object that defines only a __get__ method (but not __set__ or __delete__).
    3. Non-data descriptors don’t take precedence over instance attributes. If an attribute is defined both as an instance attribute and as a non-data descriptor in the 
       class, Python will use the instance attribute.
    4. If a non-data descriptor is found, Python will call its __get__ method to retrieve the value.

4. Class Attributes (Directly in the Class or Parent Classes) : 
    1. If no descriptors (data or non-data) or instance attributes are found, Python then checks the class and parent classes (according to MRO) for a regular 
       class attribute with the given name.
    2. A class attribute is any attribute defined directly in the class that isn’t a descriptor.
    3. If Python finds the attribute, it returns its value directly.

5. Inheritance Chain (Following the MRO) : 
    1. If Python doesn’t find the attribute in the instance, the class, or any descriptors, it moves up the inheritance chain, following the 
       Method Resolution Order (MRO) to check parent classes.
    2. Python will repeat the checks as described above (first for data descriptors, then instance dictionary, etc.) for each class in the MRO.
    3. If it finds an attribute in one of the parent classes, it returns the value from there.

6. __getattr__ Method (if Defined in the Class) : 
    1. If the attribute isn’t found in any of the above steps, Python calls the class’s __getattr__ method if it’s defined.
    2. __getattr__ is a special method that acts as a fallback and allows custom behavior for attribute access. It’s called only if the attribute wasn’t found through the 
       usual lookup process.
    3. we can define custom logic in __getattr__ to return a value, raise an exception, or perform some other action when an attribute is missing.

7. Raise AttributeError : 
    1. If the attribute isn’t found through any of the previous steps and __getattr__ is not defined, Python raises an AttributeError.
    2. This signals that the attribute is not available on the object.
"""
