"""
### What is Dynamic Typing?
In a dynamically typed language like Python, the type of a variable is determined at runtime, rather than at compile time. This means that you don't have to declare the type of a
variable when you create it, and a variable can change its type as the program executes.

For example:
x = 5         # x is an integer
x = "Hello"   # Now x is a string

Here, x first holds an integer value and later holds a string. The type of x is determined dynamically when the assignment happens.

### How Dynamic Typing Affects Method Overloading
In statically typed languages like Java or C++, the types of variables (including method parameters) are known at compile time. This allows these languages to support method overloading
because the compiler can distinguish between different methods based on their signatures (the number and types of parameters).

For example, in Java:
class MyClass {
    void myMethod(int a) { ... }
    void myMethod(String a) { ... }
}

Here, the compiler knows which myMethod to call based on whether you pass an integer or a string.

However, in Python: Type Determination at Runtime: Since types are determined at runtime, there’s no need to differentiate methods by type at compile time. A single method can be written
to handle different types of inputs, and Python will resolve what to do based on the actual type of the argument when the method is called.

Flexibility in Method Design: Python’s dynamic typing encourages writing more flexible methods that can handle different types and numbers of arguments. Instead of relying
on method overloading, Python developers can use:
1. Default Arguments: To provide different behaviors based on the presence or absence of arguments.
2. Variable-Length Arguments: Using *args and **kwargs allows a method to accept and process a variable number of positional or keyword arguments.
3. Type Checking Inside Methods: If needed, you can check the type of arguments within the method and alter behavior accordingly.
4. Simpler and More Pythonic Code: Dynamic typing allows Python to maintain a simpler and more consistent approach to method definitions. Instead of creating multiple versions of a
   method with slightly different signatures, you can often handle everything in a single method, leading to more concise and readable code.

For Example:

class MyClass:
    def my_method(self, a):
        if isinstance(a, int):
            print(f"Handling integer: {a}")
        elif isinstance(a, str):
            print(f"Handling string: {a}")
        else:
            print(f"Handling unknown type: {a}")

obj = MyClass()
obj.my_method(10)       # Handling integer: 10
obj.my_method("Hello")  # Handling string: Hello

In this example, a single method my_method handles both integers and strings by checking the type of a at runtime. There's no need to create separate methods for each type.
"""

"""
Python does not natively support method overloading in the same way as languages like Java or C++. In those languages, you can define multiple methods with the same name but different 
parameter lists, and the appropriate method is selected at runtime based on the arguments passed.

Here’s why Python doesn’t natively support method overloading:

1. Dynamic Typing : Python is dynamically typed, meaning that the type of a variable is determined at runtime, not at compile time. This makes it less critical to have multiple versions of a 
                    method with different parameter types because Python functions can handle different types and numbers of arguments using features like default arguments, variable-length 
                    arguments (*args, **kwargs), and type checking within the method.
                    
2. Last Defined Method Wins : If you define multiple methods with the same name in a Python class, the last one defined will overwrite any previously defined ones. This behavior contrasts with 
                              languages that support method overloading where each version of the method is preserved.
"""