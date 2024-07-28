# The __str__ method in Python classes is used to define the string representation of an object.

class Information:
    university = "UAP"

    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def __str__(self):
        return f"{self.name}--{self.age}--{self.department}--{self.university}"

std = Information("Aubdur Rob Anik", 14, "CSE")
print(std)

# When you call the built-in str() function or use print() on an object, Python internally invokes the __str__ method of that object to determine how it should be represented as a string

def normal_function(x, y):
    return x+y

print(normal_function(1, 2))

# Function Call: normal_function(1, 2) is evaluated first.
# Return Value: The function normal_function executes and returns the result of the operation 1 + 2, which is 3.
# print() Function: The print() function is then called with 3 as its argument.
# String Conversion: The print() function internally calls str() on its argument to convert it to a string. Since 3 is an integer, str(3) calls the __str__ method of the integer object 3.
# Output: The print() function outputs the string representation of 3 to the console.

