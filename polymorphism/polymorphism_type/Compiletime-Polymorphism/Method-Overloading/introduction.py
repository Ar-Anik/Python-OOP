"""
In Java or C++ when more than one method with the same name but different type of argument is defined in the same class,
it is known as method overloading.
"""

# In python, If a method is written such that it can perform more than one task, is called method overloading.

"""
Actually, in Python, method overloading refers to the ability of a single method to handle different numbers or types of parameters. 
It's not about a method performing more than one task.
"""

''' In Python, we don't explicitly write multiple methods with the same name to handle different tasks. Instead, we can achieve similar functionality
 by defining a single method with default parameter values or using variable numbers of arguments (*args or **kwargs) to handle different cases. '''

"""
Dis-advantage of Python Method Overloading
Performing More Than One Task: If a method is designed to perform multiple tasks, it's often a sign of poor design, violating the Single
Responsibility Principle (SRP) from SOLID principles. It's generally recommended to have methods focused on a single task or responsibility.
"""

class Calculator:
 def add(self, a, b=0, c=0):
     return a+b+c

calc = Calculator()

print(calc.add(2, 3))
print(calc.add(2, 3, 4))
# print(calc.add(2, 3, 4, 5))
print(calc.add(2))
