"""
For static methods, the __get__ method does not bind the instance. Static methods don’t need access to an instance (self) or the class (cls); they behave like
regular functions but belong to a class namespace.

When we access a static method, the __get__ method returns the function itself, without any binding.
"""

class MyClass:
    @staticmethod
    def my_static_method():
        print("Called static method.")

obj = MyClass()

# we can access method also by obj.my_static_method
static_method = MyClass.__dict__['my_static_method'].__get__(None, MyClass)

static_method()

"""
1. When MyClass.my_static_method is accessed, the __get__ method is called.
2. The instance (None) is ignored, and the staticmethod descriptor simply returns the original function without any binding.
"""
