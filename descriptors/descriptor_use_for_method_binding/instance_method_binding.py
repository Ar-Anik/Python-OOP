"""
1. When an instance method is accessed through an object, Python binds the method to the instance.
2. Internally, this is done using a descriptor object (i.e., the function object) and its __get__ method.
3. The __get__ method returns a bound method when called on an instance. The bound method wraps the original function, and the instance
   becomes the first argument (self) to the method.
"""

class MyClass:
    def instance_method(self):
        print(f"Method bound to {self}")

obj = MyClass()

# obj.instance_method equivalent to obj.__class__.__dict__['instance_method'].__get__(obj, obj.__class__)

instance_method = MyClass.__dict__['instance_method'].__get__(obj, MyClass)       # This is equivalent to obj.instance_method

instance_method()       # This is equivalent to MyClass.instance_method(obj)

"""
Here MyClass.__dict__['instance_method'].__get__(obj, MyClass) or obj.instance_method returns a bound method via the __get__ descriptor.
"""