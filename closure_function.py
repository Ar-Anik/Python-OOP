"""
Closures Function Link : https://www.geeksforgeeks.org/python/python-closures/

Q : What is Enclosing in Python?
-> In the context of functions, "enclosing" means that a function is wrapped inside another function — and the outer
function is said to be the enclosing function.
"""
def outer():        	# <--- Enclosing function
    x = 10           	# <--- Variable in enclosing scope
    def inner():     	# <--- Enclosed (inner) function
        print(x)     	# <--- Accessing variable from enclosing scope
    return inner
"""
Here, 
	* outer() is the enclosing function.
	* inner() is defined inside outer(), so it's enclosed by outer().
	* The variable x is in the enclosing scope of inner().

> Enclosing function : A function that contains another (nested) function inside it.
> Enclosed function : A function defined inside another function.
> Enclosing scope : The variable space of the enclosing function.

Q : What is Lexical Scope?
-> Lexical scope (also called static scope) means that Python decides variable scope based on where functions and 
variables are written in the code — not where they are called at runtime.
"""
def outer():
    msg = "Hello"
    def inner():
        print(msg)
    inner()

outer()
"""
msg is defined lexically (physically) inside outer(). inner() sees msg because of the lexical (text-based) location, 
not because it was called from outer().


Q : What is closures in python?
-> A closure in Python is a function that remembers the variables from the place where it was created, even after 
that place (outer function) is gone. Above example inner() is a closure function.

-> In Python, a closure is a function object that remembers values from its enclosing lexical scope, even if the 
outer function has finished executing.

A closure occurs when:
    * We have a nested function (a function defined inside another function),
    * The inner function references variables from the outer function, and
    * The outer function returns the inner function.
"""
def outer_function(msg):
    def inner_function():
        print(f"Message: {msg}")
    return inner_function

my_func = outer_function("Aubdur Rob Anik")
my_func()
"""
Even though outer_function has finished running, inner_function still has access to msg — that's a closure.

Q : Why closures are useful ?
> Encapsulation: You can hide data inside the closure.
> Function factories: They help in building customizable functions.
> State retention: Closures keep the state between calls without using global variables or classes.
"""

# Example Function Factory :
def multiplier(x):
    def multiply(y):
        return x * y
    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(5))
print(triple(10))

"""
Here, double and triple are closures that remember x as 2 and 3 respectively.
"""
