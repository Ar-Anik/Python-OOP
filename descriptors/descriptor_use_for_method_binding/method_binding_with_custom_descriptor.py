# create a custom descriptor and observe the __get__ method

class MyDescriptor:
    def __get__(self, intance, owner):
        print(f"__get__ called: instance={intance}, owner={owner}")
        if intance is None:
            return self

        # Binding the instance to the function(creating a bound method)
        return lambda: self.function(intance)

    def __init__(self, function):
        self.function = function

    def __set_name__(self, owner, name):
        self.name = name

class MyClass:
    def my_method(self):
        print(f"Called my_method on {self}")

    my_method = MyDescriptor(my_method)

obj = MyClass()

# Accessing the method will call __get__
bound_method = obj.my_method

# Call the bound method
bound_method()
