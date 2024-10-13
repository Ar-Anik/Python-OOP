"""
In real-world applications, we may also need to invalidate the cache when the underlying data changes.
"""

class CachePropertyWithInvalidation:
    def __init__(self, func):
        self.func = func
        self.cache_name = f"_{func.__name__}_cache"

    def __get__(self, instance, owner):
        if instance is None:
            return self

        if not hasattr(instance, self.cache_name):
            setattr(instance, self.cache_name, self.func(instance))

        return getattr(instance, self.cache_name)

    def __set__(self, instance, value):
        print("Called for Set Value.")
        setattr(instance, self.cache_name, value)

    def invalidate_cache(self, instance):
        print("Called For Invalidate The Cache")
        print("Self : ", self)
        print("Instance : ", instance)
        if hasattr(instance, self.cache_name):
            delattr(instance, self.cache_name)

class ClassWithInvalidation:
    def __init__(self, value):
        self.value = value

    @CachePropertyWithInvalidation
    def compute_cube(self):
        print("Perfoming Expensive Computation.")
        return self.value * self.value * self.value

obj = ClassWithInvalidation(10)
print(obj.compute_cube)

obj.compute_cube = 20

print(obj.compute_cube)

ClassWithInvalidation.compute_cube.invalidate_cache(obj)

print(obj.compute_cube)
