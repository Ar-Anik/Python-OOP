from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self, device_id, status):
        self._device_id = device_id
        self._status = status

    @property
    def device_id(self):
        return self._device_id

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, action):
        self._status = action

    @property
    @abstractmethod
    def energy_consumption(self):
        pass

    @abstractmethod
    def control(self, action):
        pass

class Thermostat(Device):
    @property
    def energy_consumption(self):
        return 2.5     # Energy Consumption in KWH

    def control(self, action):
        self.status = action
        if action == 'heat':
            return 'Heating Turned On'
        elif action == 'cool':
            return 'Cooling Turned On'
        else:
            return 'Invalid Action'

class SmartLight(Device):
    @property
    def energy_consumption(self):
        return 0.7

    def control(self, action):
        self.status = action
        if action == 'on':
            return 'Light Turned On.'
        elif action == 'off':
            return 'Light Turned Off.'
        else:
            return 'Invalid Action.'

class SecurityCamera(Device):
    @property
    def energy_consumption(self):
        return 5.0

    def control(self, action):
        self.status = action
        if action == 'record':
            return 'Recording Started.'
        elif action == 'stop':
            return 'Recording Stopped.'
        else:
            return 'Invalid Action'

thermostat = Thermostat("T123", "off")
smart_light = SmartLight("L456", "off")
security_camera = SecurityCamera("C789", "off")

print(thermostat.control('heat'))
print(smart_light.control('on'))
print(security_camera.control('record'))

print("Thermostat Energy Consumption:", thermostat.energy_consumption, "kWh")
print("Smart Light Energy Consumption:", smart_light.energy_consumption, "kWh")
print("Security Camera Energy Consumption:", security_camera.energy_consumption, "kWh")

print(thermostat.status)
print(smart_light.status)
print(security_camera.status)
