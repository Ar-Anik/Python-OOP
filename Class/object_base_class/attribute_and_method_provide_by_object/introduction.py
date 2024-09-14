"""
The object class in Python provides a minimal set of attributes and methods that are common to all objects.
These are generally referred to as "magic methods" or "dunder methods" (double underscores). The object class
provides about 24 key methods and attributes.
"""

"""
Here are the main methods provided by the object class:

1. __new__(cls, *args, **kwargs) : This is the method responsible for creating a new instance of a class. It’s called before __init__() 
                                   and is often overridden in advanced cases like implementing singleton patterns or immutable types.

2. __init__(self, *args, **kwargs) : Initializes the instance created by __new__. This is one of the most common methods you interact 
                                     with when constructing objects.

3. __del__(self) : This is called when the object is about to be destroyed (i.e., when its reference count reaches zero or when the 
                   interpreter is shutting down). It's the destructor method, though it's rarely needed because Python has automatic 
                   garbage collection.

4. __repr__(self) : Returns a string that should be a valid Python expression which can recreate the object (if possible). It's often 
                    used in debugging and development environments.

5. __str__(self) : Returns a string representation of the object meant for human readability. It's called by print() and str().

6. __eq__(self, other) : This method is used to compare two objects for equality. By default, it checks for identity 
                         (i.e., if two objects are the same object in memory), but can be overridden to check for structural equality.

7. __ne__(self, other) : This is the negation of __eq__(). If you override __eq__(), you might also want to override this method.

8. __lt__(self, other) : Checks if an object is less than another object. It can be overridden to implement custom comparison logic.

9. __le__(self, other) : Checks if an object is less than or equal to another object.

10. __gt__(self, other) : Checks if an object is greater than another object.

11. __ge__(self, other) : Checks if an object is greater than or equal to another object.

12. __hash__(self) : Returns an integer hash value, used in hashing collections like sets and dictionaries. By default, object.__hash__() returns a hash based on the object's identity, but this method can be overridden to customize hashing.

13. __setattr__(self, name, value) : Handles setting an attribute. By default, it directly assigns the attribute, but you can override this method to customize the behavior (e.g., adding validation).

14. __getattr__(self, name) : This method is called if you try to access an attribute that doesn't exist. It's useful for dynamically handling attribute access.

15. __delattr__(self, name) : Handles the deletion of attributes.

16. __dir__(self) : Returns a list of attributes and methods of the object, which is useful when you use dir() on an object.

17. __sizeof__(self) : Returns the size of the object in bytes.

18. __reduce__() : Provides support for object serialization (used by the pickle module).

19. __reduce_ex__(self, protocol) : A more advanced version of __reduce__(), also related to object serialization.

20. __format__(self, format_spec) : Used when formatting an object using the format() function.

21. __subclasshook__(cls, subclass) : This is intended to customize issubclass() behavior for abstract base classes (ABCs).

22. __class__ : This is an attribute that returns the class of the object.

23. __doc__ : Contains the documentation string of the class, if provided.

24. __module__ : The name of the module in which the class is defined.
"""

