class DataDescriptor:
    def __get__(self, instance, owner):
        print("Call Get Method.")
        return 69

class Example:
    attr = DataDescriptor()

obj = Example()

obj.attr = 100
print(obj.attr)

print("Before Instance Attribute Assign : ", obj.__dict__)

obj.__dict__['attr'] = 50
print(obj.attr)

print("After Instance Attribute Assign : ", obj.__dict__)
