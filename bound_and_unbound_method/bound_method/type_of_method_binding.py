"""
Method binding refers to how methods are associated with objects or classes, determining how they are invoked. In Python, there are two types of method binding:
1. Static binding (early binding) (Class/Static Method Binding)
2. Dynamic binding (late binding) (Instance Method Binding).
"""

"""
1. Static (Early) Binding:
    1. Occurs at compile-time, meaning the method to be invoked is determined when the program is compiled.
    2. In Python, this happens when calling static methods or class methods. These methods are bound to the class rather than to the instance.
    3. For example, static methods and class methods do not have access to instance-specific data but can work with class-level data.
"""

"""
Q : Why Static Methods in Static Method Binding?
----> Static methods are not bound to either the class or the instance. They behave like regular functions that happen to live inside a class. The key thing is:
        1. No instance or class binding occurs.
        2. We can call a static method without creating an instance of the class.
"""

class StaticMethodClass:
    @staticmethod
    def static_method():
        print("Static Method Called.")

StaticMethodClass.static_method()

"""
In this case, there is no binding to an instance (self) or the class (cls). The method behaves just like a normal function, which is why it's called a static method. 
It is included in method binding in the sense that it is still part of the class’s namespace, but it doesn’t bind to the instance. The key distinction is that they are 
not dynamically bound to any specific object at runtime.
"""

"""
Q : Why Class Methods in Static Method Binding?
----> Class methods are methods that are bound to the class, not to an instance of the class. This means that when we call a class method, Python automatically passes 
the class (cls) as the first argument, instead of an instance.
"""

class ClassMethodClass:
    @classmethod
    def class_method(cls):
        print(f"Class Method Bound to {cls}")

ClassMethodClass.class_method()

"""
Here, the class method is bound to the class, so when it is called, Python passes the class (ClassMethodClass) as the first argument, allowing the method to interact with the class 
itself (not with instances). This type of method binding is called static binding because it happens at the class level, rather than dynamically at runtime like instance methods.
"""


"""
2. Dynamic (Late) Binding:
    1. Occurs at runtime, meaning the method to be called is determined during program execution.
    2. In Python, instance methods are dynamically bound. This means when an instance method is invoked on an object, the method is bound to the specific instance.
    3. The self parameter refers to the instance, allowing instance-specific data to be accessed.
"""

class DynamicBinding:
    def instance_method(self):
        print(f"Method Bound to {self}")

obj = DynamicBinding()
obj.instance_method()      # Late Binding, Bound to `obj`

