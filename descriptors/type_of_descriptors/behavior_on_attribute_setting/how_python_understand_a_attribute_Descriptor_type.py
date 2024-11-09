"""
## Attribute Resolution Process:
----> When Python accesses or sets an attribute, it checks the following in a strict order:

1. First, check the class for a descriptor. Python has to know first whether the class attribute is a descriptor (either a data descriptor or a non-data descriptor).
This allows Python to decide whether to follow the descriptor protocol or use the instance's __dict__. This is where Python checks the class for methods like
__get__, __set__, or __delete__ to determine if the class attribute is a descriptor. If it's a data descriptor, Python gives it priority.

2. Data descriptors implement both __get__ and __set__. When Python finds a data descriptor, it immediately uses its __get__ or __set__ methods before even looking
in the instance’s __dict__. This means the data descriptor overrides anything in the instance’s __dict__. If it's a non-data descriptor, check the instance's __dict__.

3. Non-data descriptors implement only __get__. Python will first check if the attribute exists in the instance’s __dict__. If it does, Python will return that value,
and the descriptor is ignored. If the attribute isn’t in the instance’s __dict__, Python will use the __get__ method from the non-data descriptor.
"""

"""

# Why does Python check the class first when accessing an attribute of an instance? ?
-----> The class is checked first because descriptors are defined at the class level. Python cannot know if an attribute is a descriptor just by looking at the instance's 
__dict__. This is why Python first looks at the class attributes to determine if the attribute is a descriptor and whether it's a data descriptor or non-data descriptor.

"""

"""
# Overall in Attribute Access : 
1. Python checks the class first for a descriptor.
2. If the class attribute is a descriptor, Python checks whether it has both __get__ and __set__.
3. If both exist, it's a data descriptor and takes priority over the instance's __dict__.
4. If only __get__ exists, it's a non-data descriptor, and Python checks the instance's __dict__ before using the descriptor.
5. Only after deciding whether the attribute is a descriptor (data or non-data) does Python proceed with the actual attribute access.
"""