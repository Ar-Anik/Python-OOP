from __hash__ import HashablePoint

class ExampleClass:
    pass

print(ExampleClass.__module__)

"""
If you define a class in another module and import it, __module__ would contain the name of that module.
"""

print(HashablePoint.__module__)