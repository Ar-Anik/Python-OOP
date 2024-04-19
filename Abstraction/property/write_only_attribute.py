class Temperature:
    def __init__(self):
        self._celsius = 0

    @property
    def temperature(self):
        raise AttributeError("Temperature is Write-Only")

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature cann't be less than -273.15")
        self._celsius = value

temp = Temperature()
temp.temperature = -273.14

print(temp.temperature)
