class Parent:
    @classmethod
    def class_method(cls):
        print(f"Class name {cls.__name__}")
        print("-- Class method in Parent")

class Child(Parent):
    @classmethod
    def class_method(cls):
        print(f"Class name {cls.__name__}")
        print("-- Class method in Child")
        super().class_method()

Child.class_method()
