# https://www.geeksforgeeks.org/metaprogramming-metaclasses-python/

# type of Variable
num = 23
lst = [1, 2, 4]
name = "Aubdur Rob Anik"

print("Type of num is : ",type(num))
print("Type of lst is : ", type(lst))
print("Type of name is : ", type(name))

# Every type in Python is defined by Class.
class Student:
    pass

stu_obj = Student()
print("Type Of  stu_obj is : ", type(stu_obj))

# A Class is also an object, A special Class type creates these Class objects.
print("Type of Student Class : ", type(Student))

# Class is a object of type class. So we can add or delete attribute or method from a class like a object
class Test:
    pass

print("Type of Test Class : ", type(Test))
Test.x = 69

def foo(self):
    print("Hello from MetaClass")

Test.foo = foo

test_obj = Test()
print("Bastard Variable : ", test_obj.x)
test_obj.foo()
