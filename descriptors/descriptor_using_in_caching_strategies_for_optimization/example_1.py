"""
Descriptors can be useful for caching strategies to optimize performance, particularly when the cost of recomputing a value is high
and it doesn't change frequently. The goal of using descriptors in caching is to store the computed result and return it when the
attribute is accessed again, avoiding unnecessary recalculations.
"""

# it's not actual optimization example, it's a way.
class CacheProperty:
    def __init__(self, func):
        self.func = func
        self.cache_name = f"_{func.__name__}_cache"

    def __get__(self, instance, owner):
        if instance is None:
            return self

        print("Instance __dict__ : ", instance.__dict__)
        if not hasattr(instance, self.cache_name):
            setattr(instance, self.cache_name, self.func(instance))

        return getattr(instance, self.cache_name)

class ExpensiveComputation:
    def __init__(self, value):
        self.value = value

    @CacheProperty
    def compute_square(self):
        print("Performing Expensive Computation.")
        return self.value ** 2

obj = ExpensiveComputation(10)
print(obj.compute_square)

print(obj.compute_square)

"""
The first time compute_square is accessed, the expensive computation is performed. On the second access, the cached result is returned immediately.

---> When to Use Descriptors for Caching : 
    1. Expensive computations: If a property or method involves a resource-intensive calculation that remains constant after its first evaluation, caching is beneficial.
    2. Lazy Evaluation: Descriptors can be used to delay computation until the first time the value is needed (as shown in the example).
    3. Custom access logic: Descriptors provide flexibility for implementing logic that manages when a value should be cached, invalidated, or recomputed.
"""

