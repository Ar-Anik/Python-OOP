class AttributeDescriptor:
    def __init__(self, name):
        self.name = name
        self.data = {}

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.data.get(instance, None)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise ValueError(f"{self.name} must be a number.")
        self.data[instance] = value

    def __delete__(self, instance):
        if instance in self.data:
            del self.data[instance]


class MyClass:
    attribute_1 = AttributeDescriptor("attribute_1")
    attribute_2 = AttributeDescriptor("attribute_2")
    attribute_3 = AttributeDescriptor("attribute_3")

    def __init__(self, attr1, attr2, attr3):
        self.attribute_1 = attr1
        self.attribute_2 = attr2
        self.attribute_3 = attr3

    def __repr__(self):
        return f"MyClass(attribute_1={self.attribute_1}, attribute_2={self.attribute_2}, attribute_3={self.attribute_3})"

obj = MyClass(10, 20, 30)
print(obj)

obj.attribute_1 = 100
obj.attribute_2 = 200
obj.attribute_3 = 300

print(obj)

try:
    obj.attribute_1 = "Invalid Value"
except ValueError as e:
    print(e)