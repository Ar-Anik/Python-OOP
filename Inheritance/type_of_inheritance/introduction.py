"""
Inheritance in object-oriented programming (OOP) is a mechanism where a new class (child or subclass) derives properties and behaviors (methods)
from an existing class (parent or superclass). This concept allows for code reuse and the creation of hierarchical relationships between classes.
"""

# Type of Inheritance

"""
1. Single Inheritance
Definition: A subclass inherits from one and only one superclass.

Characteristics:
Simplicity: Easy to understand and implement.
Hierarchy: Creates a linear hierarchy between classes.
"""

"""
2. Multiple Inheritance
Definition: A subclass inherits from more than one superclass.

Characteristics:
Flexibility: Allows a class to inherit features from multiple sources.
Complexity: Can lead to issues like the Diamond Problem, where ambiguity arises if multiple superclasses define the same method.
Use Case: Useful when a class needs to combine functionality from multiple classes.
"""

"""
3. Multilevel Inheritance
Definition: A subclass inherits from a superclass, which in turn inherits from another superclass, creating a chain.

Characteristics:
Hierarchical: Builds a multi-tiered class hierarchy.
Use Case: Useful for creating a hierarchy where subclasses build on functionality from multiple levels.
"""

"""
4. Hierarchical Inheritance
Definition: Multiple subclasses inherit from a single superclass.

Characteristics:
Single Source: All subclasses share common functionality from the superclass.
Use Case: Useful when different subclasses share common behavior or properties.
"""

"""
5. Hybrid Inheritance
Definition: A combination of two or more types of inheritance (e.g., multiple and multilevel inheritance).

Characteristics:
Complexity: Can be complex to design and manage.
Flexibility: Offers powerful features but may lead to ambiguity or complexity.
Use Case: Used in sophisticated scenarios where multiple inheritance types are needed.
"""

"""
Summary:
1. Single Inheritance: Inherits from one superclass.
2. Multiple Inheritance: Inherits from more than one superclass.
3. Multilevel Inheritance: Inherits through a chain of classes.
4. Hierarchical Inheritance: Multiple subclasses inherit from a single superclass.
5. Hybrid Inheritance: Combination of different types of inheritance.
"""