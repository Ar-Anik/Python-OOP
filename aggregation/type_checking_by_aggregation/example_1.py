from typing import List

# Product class representing items available for sale
class Product:
    def __init__(self, product_id: int, name: str, price: float):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (ID: {self.product_id}) - ${self.price:.2f}"


class Order:
    def __init__(self, order_id: int):
        self.order_id = order_id
        self.products: List[Product] = []  # Aggregates Product objects

    def add_product(self, product):
        # Type checking to ensure only Product objects are added
        if not isinstance(product, Product):
            raise TypeError("Only objects of type 'Product' can be added to the order.")
        self.products.append(product)
        print(f"Product {product} added to order #{self.order_id}.")

    def calculate_total(self):
        return sum(product.price for product in self.products)

    def summary(self):
        print(f"Order #{self.order_id} Summary:")
        if not self.products:
            print("No products in the order.")
        else:
            for product in self.products:
                print(f" - {product}")
            print(f"Total Price: ${self.calculate_total():.2f}")


try:
    laptop = Product(101, "Laptop", 999.99)
    mouse = Product(102, "Wireless Mouse", 49.99)
    keyboard = Product(103, "Mechanical Keyboard", 79.99)

    my_order = Order(order_id=5001)

    my_order.add_product(laptop)
    my_order.add_product(mouse)

    my_order.add_product(keyboard)

    my_order.summary()

    my_order.add_product("Not a product")  # This will raise a TypeError

except TypeError as e:
    print(e)
