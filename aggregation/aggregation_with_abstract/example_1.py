from abc import ABC, abstractmethod

class OrderComponent(ABC):
    @abstractmethod
    def get_details(self):
        pass

class Customer(OrderComponent):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_details(self):
        return f"Customer: {self.name}, Email: {self.email}"

class Product(OrderComponent):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_details(self):
        return f"Product: {self.name}, Price: ${self.price}, Quantity: {self.quantity}"

class ShippingDetails(OrderComponent):
    def __init__(self, address, method):
        self.address = address
        self.method = method

    def get_details(self):
        return f"Shipping Address: {self.address}, Method: {self.method}"

class Order:
    def __init__(self, customer, product, shipping_address):
        self.customer = customer
        self.product = product
        self.shipping_address = shipping_address

    def get_order_summary(self):
        return "\n".join([
            self.customer.get_details(),
            self.product.get_details(),
            self.shipping_address.get_details()
        ])

customer = Customer("Anik", "anik13331@gmail.com")
product = Product("Laptop", 8500, 1)
shipping_address = ShippingDetails("Road-5, Banani, Dhaka", "Cash On Delivery")

customer_order = Order(customer, product, shipping_address)

print("Order Summary : ")
print(customer_order.get_order_summary())
