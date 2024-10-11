class PriceDescriptor:
    def __init__(self):
        self.data = {}

    def __get__(self, instance, owner):
        return self.data.get(instance, None)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Price Must be a positive number.")
        self.data[instance] = value

    def __delete__(self, instance):
        if instance in self.data:
            del self.data[instance]

class QuantityDescriptor:
    def __init__(self):
        self.data = {}

    def __get__(self, instance, owner):
        return self.data.get(instance, None)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Quantitiy Must be a non-negative integer.")
        self.data[instance] = value

    def __delete__(self, instance):
        if instance in self.data:
            del self.data[instance]

class DiscountDescriptor:
    def __init__(self):
        self.data = {}

    def __get__(self, instance, owner):
        return self.data.get(instance, None)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)) or not(0 <= value <= 100):
            raise ValueError("Discount Must be a percentage between 0 to 100")
        self.data[instance] = value

    def __delete__(self, instance):
        if instance in self.data:
            del self.data[instance]

class Product:
    price = PriceDescriptor()
    quantity = QuantityDescriptor()
    discount = DiscountDescriptor()

    def __init__(self, price, quantity, discount=0):
        self.price = price
        self.quantity = quantity
        self.discount = discount

    def __repr__(self):
        return f"Product(price={self.price}, quantity={self.quantity}, discount={self.discount}%)"

    def calculate_total_price(self):
        return (self.price * self.quantity) * (1 - (self.discount/100))

product = Product(price=100, quantity=5, discount=10)
print(product)

total_price = product.calculate_total_price()
print(f"Total price after discount: {total_price:.2f} taka")

product.price = 120
product.quantity = 3
product.discount = 15

total_price = product.calculate_total_price()
print(f"New total price after discount: {total_price:.2f} taka")

try:
    product.price = -50
except ValueError as e:
    print(e)

try:
    product.quantity = -3
except ValueError as e:
    print(e)

try:
    product.discount = 150
except ValueError as e:
    print(e)
