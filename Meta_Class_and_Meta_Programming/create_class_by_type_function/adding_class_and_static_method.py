@classmethod
def class_method(cls):
    print(f"Class method called from {cls.__name__}")

@staticmethod
def static_method():
    print("Static method called.")

Mycls = type('Myclass', (), dict(class_method = class_method, static_method = static_method))

Mycls.class_method()

obj = Mycls()
obj.class_method()
obj.static_method()
