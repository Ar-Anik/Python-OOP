# https://medium.com/@bindubc/association-aggregation-and-composition-in-oops-8d260854a446
# https://faun.pub/association-aggregation-composition-python-ec9947832cbd

"""
In Python Object-Oriented Programming (OOP), association describes a relationship between two or more objects, where one object is linked to another,
but neither owns the other. The association is not as strict as inheritance; it focuses on the "uses-a" relationship rather than a "is-a" relationship.

Its a relationship between two classes and that relationship is established through their objects. Each object has its own life cycle and there is no
owner object. It is a weak type of relationship. It can be one-to-one, one-to-many, many-to-one, or many-to-many. For example students and teachers,
both classes are associated with each other. The objects of each class have their own life cycle and there is no owner.
"""

"""
Association : The objects that are part of the association relationship can be created and destroyed independently.
    1. Association is a semantically weak relationship (a semantic dependency) between otherwise unrelated objects.
    2. An association is a “using” relationship between two or more objects in which the objects have their own lifetime and there is no owner.
    3. Composition and Aggregation are the two forms of association.
"""

"""
Characteristics
    1. Association emphasizes independent objects that are loosely coupled.
    2. It does not impose strict ownership or lifecycle dependencies.
    3. It is implemented by referencing objects through instance variables or method arguments.
"""

