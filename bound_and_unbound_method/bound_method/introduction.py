# resource : https://www.geeksforgeeks.org/bound-methods-python/

"""
A bound method is the one which is dependent on the instance of the class as the first argument. It passes the instance as the first argument which is used to access the variables and functions.
In Python 3 and newer versions of python, all functions in the class are by default bound methods.
"""

class A:
    def method(self, value):
        self.value = value
        print(f"Value of {self}=", value)

obj = A()
obj.method(10)

"""
The instance obj is automatically passed as the first argument to the function called and hence the first parameter of the function will be used to access the variables/functions of the object.
"""

"""
Q : What is the Python bound method?
---> A bound method in Python is a method derived from an instance of a class that is “bound” to that instance. A bound method has its first parameter (usually called self) automatically set to the 
instance on which the method is called. This means that the method is associated with a specific object, allowing it to operate on the object’s data (attributes).
"""

class MyClass:
    def greet(self):
        print(f"Hello, I am a instance of {self.__class__.__name__}")

obj = MyClass()

# 'greet' is now a bound method, bound to the instance 'obj'
obj.greet()
