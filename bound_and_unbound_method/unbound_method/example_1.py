class MyClass:
    def greet(self):
        print(f"Hello from {self.__class__.__name__}")

obj = MyClass()

# Bound Method
obj.greet()

# Unbound Method
MyClass.greet(obj)  # Need to explicitly pass `obj` as self

MyClass.greet()     # Show Error: unbound method requires an instance of the class as first argument.