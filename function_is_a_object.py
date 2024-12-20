"""
When we create a function using the def keyword or the lambda keyword, Python internally creates an object of function class.
which means this object type is function. This function object includes several attributes and references, such as:

1. The code object (__code__): Contains the compiled bytecode of the function.

2. The function's name (__name__): A reference to the name of the function.

3. The docstring (__doc__): A reference to the function's documentation string, if provided.

4. The module (__module__): A reference to the module in which the function was defined.

5. Defaults for arguments (__defaults__): Contains the default values for the function's parameters.

6. Closure (__closure__): Contains references to any variables captured in the function's closure (in the case of nested functions or lambdas).

7. Globals (__globals__): A reference to the global namespace in which the function was defined.
"""

def my_function(x, y=10):
    """This is a simple function."""
    return x + y


print(type(my_function))

print(my_function.__code__)
print(my_function.__name__)
print(my_function.__doc__)
print(my_function.__defaults__)
print(my_function.__module__)
print(my_function.__globals__)

"""
when we assign a function to another variable, Python does not create a new function object—it creates a new reference to the same function object. 
The memory address of the function object remains unchanged. 
"""
print(my_function)
another_reference = my_function
print(another_reference)
print(another_reference is my_function)


"""
Since functions are objects, we can dynamically add attributes to them or pass them around as first-class objects:
"""
my_function.description = "This function adds two number."
print(my_function.description)


"""
--> __code__ give us the code object.
Q : What Is a Code Object?
--> A code object in Python represents the internal compiled bytecode of a function, method, or module. The bytecode is a low-level, platform-independent 
representation of your code, which the Python interpreter executes.
"""

code_object = my_function.__code__
print(code_object.co_code)          # Raw bytecode instructions
print(code_object.co_name)          # Name of the function
print(code_object.co_filename)      # File where the function is defined
print(code_object.co_firstlineno)   # Line number where the function starts
print(code_object.co_varnames)      # Local variable names

