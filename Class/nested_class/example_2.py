class OuterClass:
    def __init__(self):
        self.inner = self.InnerClass()

    def outer_method(self):
        print("Outer Method")

    class InnerClass:
        def inner_method(self):
            print("Inner Method")


outer_instance = OuterClass()
outer_instance.outer_method()

inner_instance = outer_instance.inner
inner_instance.inner_method()
