class FirstBase:
    def first_method(self):
        print(f"Method from first base class")

class SecondBase:
    def second_method(self):
        print(f"Method from second base class")

MultiBaseClass = type('MultiBase', (FirstBase, SecondBase), dict())

print("Class Name : ", MultiBaseClass.__name__)
print(MultiBaseClass.mro())

obj = MultiBaseClass()

obj.first_method()
obj.second_method()
