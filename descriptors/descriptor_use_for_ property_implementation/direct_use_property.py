class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    def get_temperature(self):
        print("Getting Value.")
        return self._temperature

    def set_temperature(self, value):
        print("Setting Value.")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value

    def delete_temperature(self):
        print("Deleting Value.")
        del self._temperature

    temperature = property(get_temperature, set_temperature, delete_temperature)

"""
property() function is a descriptor that uses the protocol:
1. __get__: When celsius.temperature is accessed, the __get__ method of the descriptor calls the get_temperature() method.
2. __set__: When celsius.temperature = 30 is executed, the __set__ method of the descriptor calls the set_temperature() method.
3. __delete__: When del celsius.temperature is used, the __delete__ method calls the del_temperature() method.

Thus, property() is essentially a convenient way to create a descriptor without manually writing the __get__, __set__, and __delete__ methods m
"""

c = Celsius()

c.temperature = 40

print(c.temperature)

del c.temperature
