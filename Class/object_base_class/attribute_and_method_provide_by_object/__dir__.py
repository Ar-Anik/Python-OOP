"""
This method allows you to control what gets returned when you call dir() on an object.
"""

class CustomDir:
    def __init__(self, name):
        self.name = name

    def custom_method(self):
        return "This is a custom method"

    def __dir__(self):
        # Returning a custom set of attributes
        return ['name', 'custom_method']

obj = CustomDir("Anik")

print(dir(obj))
print(obj.__dir__())

