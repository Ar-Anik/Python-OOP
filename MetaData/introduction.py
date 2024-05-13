"""
Metadata refers to data that provides information about other data. In the context of programming, metadata often describes various aspects of program elements such as classes,
functions, modules, etc. Metadata can include things like docstrings, annotations, decorators, and other information that describes the characteristics or properties of code elements.

For example, in Python, metadata might include:

1. Docstrings: Strings enclosed in triple quotes that provide documentation for classes, functions, or modules.
2. Annotations: Type hints or other information attached to function parameters or return values.
3. Decorators: Functions that modify the behavior of other functions or classes.

Metadata is useful for documentation, introspection, and sometimes for altering the behavior of code dynamically.

Functions and classes have metadata accessible through attributes like __name__, __module__, __qualname__, __doc__ etc.
"""

# DocStrings

def name_print(name):
    """
    Parameters :
        name (str) : The name

    Return :
        str : A string
    """

    return f"Hello, {name}!"

print(name_print.__doc__)

# Annotations
# Annotations provide type hints or other information attached to function parameters or return values.
def add(x: int, y: int) -> int:
    return x + y


# Decorators
class Student:
    @classmethod
    def class_name_print(cls):
        print(cls.__name__)

Student.class_name_print()

# Attributes
# Attributes are pieces of metadata attached to various objects like classes, functions, or variables.
class Myclass:
    my_attribute = "metadata"


# Module-Level Metadata
import module_level_metadata

print("Author : ", module_level_metadata.__author__)
print("Version : ", module_level_metadata.__version__)
