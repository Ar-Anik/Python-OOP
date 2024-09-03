"""
Create classes using the type() function directly. It can be called in following ways –
1. When called with only one argument, it returns the type. We have seen it before in the above examples.
2. When called with three parameters, it creates a class. Following arguments are passed to it –
    1. Class name
    2. Tuple having base classes inherited by class
    3. Class Dictionary: It serves as a local namespace for the class, populated with class methods and variables
"""

def myfun(self):
    print("This is function outside of base class.")

class Base:
    def basefun(self):
        print("This is function from Base class.")

# Create Class
Test = type('Test', (Base, ), dict(author_name="Anik", my_method = myfun))

# Create Object
obj = Test()

print("Type of Test Class : ", type(Test))
print("Type of Test Class Object : ", type(obj))

print("Author Name : ", obj.author_name)
obj.my_method()
obj.basefun()
