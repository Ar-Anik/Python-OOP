# step-1
class MyClass:
    def my_method(self):
        print(f"Called my_method on {self}")

"""
When the class MyClass is defined, my_method is just a regular function, defined with one parameter (self), which will eventually refer to the instance of the class. 
Right now, it is unbound and simply a function stored in the class' __dict__.
"""
print(MyClass.__dict__)

# Step-2
obj = MyClass()

"""
1. `obj` is an instance of MyClass. When `obj` is created, Python constructs the object and stores it in memory.
2. At this point, my_method is still unbound, and hasn't interacted with `obj` yet.
"""

# Step-3
bound_method = obj.my_method

"""
1. When we access obj.my_method, Python doesn't directly return the function my_method. Instead, it uses the descriptor protocol and calls the __get__ method of the function object.

2. Internally, this is what happens:
            bound_method = MyClass.__dict__['my_method'].__get__(obj, MyClass)

3.The __get__ method receives two arguments:
    1. instance (in this case, obj).
    2. owner (in this case, MyClass, the class where my_method is defined).

4. If instance is not None (which it isn’t, because obj is passed), the method is bound to obj. Now, obj will be passed as the first argument (self) whenever bound_method is called.

5. As a result, the function is transformed into a bound method:
        <bound method MyClass.my_method of <__main__.MyClass object at 0x...>>
"""

print(bound_method)

# Step-4
bound_method()      # Internally calls obj.my_method()

"""
1. When bound_method() is called, Python internally passes obj as the first argument to my_method. So, it’s equivalent to calling obj.my_method(), which is why self refers to obj.
2. The output will be: Called my_method on <__main__.MyClass object at 0x...>
"""
