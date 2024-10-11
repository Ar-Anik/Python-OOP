"""
property is a class that implements the descriptor protocol.
"""

"""
The property class is defined in Python's built-in types and is designed specifically to create managed attributes. When we call the property() function, we create a new 
descriptor instance that manages the access to an attribute with the specified getter, setter, and deleter methods.
"""

# Here’s a simplified version of what happens when we call property(getter, setter, deleter)

class property:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, instance, owner):
        if self.fget is None:
            raise AttributeError("Unreadable Attribute.")
        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("Can't Set Attribute.")
        return self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("Can't Delete Attribute.")
        return self.fdel(instance)

"""
When we create a property using the property() function, here's the step-by-step process:

1. Calling property(): When we call property(getter, setter, deleter), we provide the methods that will manage the access to the attribute. This call constructs a new instance of the property class.

2. Storing Methods: The __init__ method of the property class stores references to the provided getter, setter, and deleter methods in the instance variables self.fget, self.fset, and self.fdel.

3. Descriptor Methods: 
 The instance of the property class implements the descriptor protocol:
    1. __get__: Invoked when you access the property. It calls the fget method.
    2. __set__: Invoked when you set a value to the property. It calls the fset method.
    3. __delete__: Invoked when you delete the property. It calls the fdel method.
"""

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature Below -273.15 is not possible")
        self._temperature = value

    def del_temperature(self):
        del self._temperature

    temperature = property(get_temperature, set_temperature, del_temperature)

c = Celsius()
c.temperature = 25
print(c.temperature)
del c.temperature

"""
The calls are resolved as follows:
1. c.temperature invokes Celsius.temperature.__get__(c, Celsius), which calls get_temperature(c).
2. c.temperature = 25 invokes Celsius.temperature.__set__(c, 25), which calls set_temperature(c, 25).
3. del c.temperature invokes Celsius.temperature.__delete__(c), which calls del_temperature(c).
"""