"""
Metadata about a module can be stored in special attributes like __author__, __version__ or custom attributes defined within the module.
"""

__author__ = "Aubdur Rob Anik"
__version__ = "1.0"
__python_version__ = "3.10"

def greet(name):
    """Greets The Given Name."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    # If this module is run as a script, demonstrate the greet function
    print(greet("Sourov"))
