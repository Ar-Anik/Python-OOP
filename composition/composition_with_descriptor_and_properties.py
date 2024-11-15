class PriceDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, 0)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        raise AttributeError("Cannot delete the price attribute.")


class Product:
    price = PriceDescriptor("price")        # it's composition

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price_with_tax(self):
        return self.price * 1.1    # assuming 10% tax

    @price_with_tax.setter
    def price_with_tax(self, value):
        self.price = value / 1.1       # set product price after reduction the tax

    def __str__(self):
        return f"Product - name={self.name}, price={self.price}, price with tax = {self.price_with_tax}"


p = Product("Laptop", 1000)
print(p)

p.price_with_tax = 1100.00
print(p)

p.price = 1200
print(p)

try:
    p.price = -50
except ValueError as e:
    print(e)

"""
When we call Product("Laptop", 1000), here's the flow:
1. Argument Passing to __init__:
    1. The Product class’s __init__ method receives name="Laptop" and price=1000 as arguments.
    2. At this point, price in __init__(self, name, price) is the value we want to set (1000), not the descriptor itself.

2. What self.price = price Really Does:
    1. When self.price = price is executed inside __init__, Python identifies that self.price corresponds to the PriceDescriptor descriptor, which was set at the class 
       level (price = PriceDescriptor("price")).
    2. So, self.price = price (or self.price = 1000) triggers the descriptor's __set__ method, passing self (the Product instance) and 1000 as the value.
    3. The __set__ method in the descriptor validates and then stores 1000 in the instance’s dictionary (self.__dict__["price"] = 1000).
"""
