"""
-> In a metaclass, __call__ controls what happens when a class (created using that metaclass) is instantiated. That is:
    obj = MyClass()  -> it triggers metaclass's __call__

-> In a metaclass, the __call__ method is responsible for Internally calling the class’s __new__ method first, then its
__init__ method — in this order : __call__ → __new__ → __init__

-> __new__ (of the target class) is called to create an instance and __init__ (of the target class) is then called to initialize it.
"""

class MyMeta(type):
    def __call__(cls, *args, **kwargs):
        print("MyMeta.__call__ started")
        instance = cls.__new__(cls, *args, **kwargs)
        print("MyMeta.__call__ got instance from __new__")
        cls.__init__(instance, *args, **kwargs)
        print("MyMeta.__call__ completed __init__")
        return instance

class MyClass(metaclass=MyMeta):
    def __new__(cls, *args, **kwargs):
        print("MyClass.__new__")
        return super().__new__(cls)

    def __init__(self, name):
        print("MyClass.__init__")
        self.name = name

obj = MyClass("Alice")  # it call MyMeta.__call() method

"""
Step 1: MyClass("Alice") is evaluated
MyClass is a class object. Python sees we're calling a class like a function → it calls the 
metaclass's __call__ method. Since MyClass uses MyMeta, Python executes:
    MyMeta.__call__(MyClass, "Alice")

Step 2: __call__ of metaclass executes __new__
    instance = cls.__new__(cls, *args, **kwargs)
→ which means: MyClass.__new__(MyClass, "Alice")

Step 3: __new__ returns a new instance of the class
    return super().__new__(cls)  -> it returns a new (uninitialized) instance of MyClass.
Now back in MyMeta.__call__, where instance = <new MyClass object>

Step 4: __call__ of metaclass calls __init__ on the instance
    cls.__init__(instance, *args, **kwargs) → MyClass.__init__(instance, "Alice")

Step 5: __init__ initializes the instance (e.g., sets self.name = "Alice")

Step 6: Return the instance
The variable obj now holds a fully initialized instance of MyClass.


Full Senario : 
obj = MyClass("Alice")
      │
      ▼
MyMeta.__call__(MyClass, "Alice")
      │
      ├──> MyClass.__new__(MyClass, "Alice")
      │       └──> object.__new__(MyClass)
      │
      ├──> MyClass.__init__(instance, "Alice")
      │
      └──> return instance → obj

"""


"""
-> Even if we don’t override __call__() in a metaclass, Python still uses type.__call__() to create 
and initialize our objects — it’s the default, built-in process that powers object instantiation.

-> If we override the metaclass’s __call__() and do not call super().__call__(), then Python will 
not automatically call __new__() and __init__() — because that's the job of type.__call__().
"""
