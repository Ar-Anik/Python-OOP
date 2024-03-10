# In python follow a principle - `If it walks like a duck and talks like a duck, it must be a duck` which means python doesn't care about which class of object it is,
# if it is an object and required behavior is present for that object then it will work. The type of object is distinguished only at runtime. This is called as duck typing.

# Python doesn't care about which class of object it is, in order to call an existing method on an object. If the method is defined on the object, then it will be called.

# Example-1
class Duck:
    def walk(self):
        print("Thapak Thapak")

class Horse:
    def walk(self):
        print("Tabdak Tabdak")

class Cat:
    def talk(self):
        print("Meow Meow")

def myfunction(obj):
    obj.walk()

d = Duck()
myfunction(d)

h = Horse()
myfunction(h)

c = Cat()
myfunction(c)

# type specific
a = 10
# here `a` variable type depend on value, 10 is integer so a is integer type

a = "Hello"
#  `Hello` is string so a is string type.