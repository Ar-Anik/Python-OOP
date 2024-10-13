import requests
from time import time

class APICashDescriptor:
    def __init__(self, func, timeout=60):
        self.func = func
        self.timeout = timeout  # cache expiration time in seconds
        self.cache_name = f"_{func.__name__}_cache"
        self.timestamp_name = f"_{func.__name__}_timestamp"

    def __get__(self, instance, owner):
        if instance is None:
            return self

        current_time = time()
        minus = current_time - getattr(instance, self.timestamp_name, 0)
        print("Current Time : ", current_time, "   minus : ", minus)

        if (not hasattr(instance, self.cache_name)) or (current_time - getattr(instance, self.timestamp_name, 0) > self.timeout):
            print("Fetching Data From The Api.")
            result = self.func(instance)
            setattr(instance, self.cache_name, result)
            setattr(instance, self.timestamp_name, current_time)
        else:
            print("Return Result Using Cached Api Result.")

        return getattr(instance, self.cache_name)


class Weather:
    def __init__(self, city):
        self.city = city

    @APICashDescriptor
    def get_weather(self):
        response = requests.get(f"https://api.weatherapi.com/v1/current.json?key=51e0972f0969406d9b0152251241310&q={self.city}")
        print("response : ", response)
        return response.json()

weather = Weather("Bangladesh")

print(weather.get_weather)
print(weather.get_weather)
