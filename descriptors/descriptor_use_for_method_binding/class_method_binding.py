"""
For class methods, the __get__ method binds the method to the class rather than an instance. This means the first argument passed to the method is the class (cls), not an instance.
"""

class MyClass:
    @classmethod
    def my_class_method(cls):
        print(f"Called Class Method on {cls} Object.")

obj = MyClass()

# we can also bind this method by obj.my_class_method
class_method = MyClass.__dict__['my_class_method'].__get__(None, MyClass)

class_method()

"""
1. When MyClass.my_class_method is accessed, the __get__ method of the classmethod object is called.
2. It binds the class (MyClass) to the method, returning a bound method where cls is automatically passed as the first argument.
3. Whether accessed from an instance or directly from the class, cls refers to the class.
"""
