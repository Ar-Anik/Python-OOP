"""
This attribute holds the docstring of the class, which can be accessed using .__doc__.
"""

class MyClass:
    """
        This is the docstring of MyClass. It describes what the class does.
    """

    def __init__(self, name):
        self.name = name

# Accessing the docstring
print(MyClass.__doc__)
