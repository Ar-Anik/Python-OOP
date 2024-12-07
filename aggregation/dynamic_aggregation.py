"""
Dynamic aggregation in Python OOP refers to the process of associating one object with another at runtime, instead of establishing a fixed relationship
during the design or instantiation of the objects.
"""

class OrderItem:
    """
        1. have No enforcement at instantiation.
        2. Raises runtime error if method is called directly.
    """
    def process(self):
        raise NotImplementedError("Subclassess must implement `process` method.")

class PhysicalProduct(OrderItem):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def process(self):
        return f"Shipping physical product: {self.name}, Weight: {self.weight}kg."


class DigitalProduct(OrderItem):
    def __init__(self, name, download_link):
        self.name = name
        self.download_link = download_link

    def process(self):
        return f"Providing download link for digital product: {self.name}. Link: {self.download_link}"


class Service(OrderItem):
    def __init__(self, description, duration):
        self.description = description
        self.duration = duration

    def process(self):
        return f"Scheduling service: {self.description} for {self.duration} hours."


class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.items = []

    def add_item(self, item):
        if isinstance(item, OrderItem):
            self.items.append(item)
            print(f"{item.__class__.__name__} added to order {self.order_id}")
        else:
            print("Item is not valid.")

    def remove_item(self, item):
        if isinstance(item, OrderItem):
            self.items.remove(item)
            print(f"{item.__class__.__name__} removed from order {self.order_id}.")
        else:
            print("Item is not valid.")

    def process_order(self):
        if not self.items:
            print("No items exist in this order.")
        else:
            for item in self.items:
                print(item.process())

order = Order("7654")

physical_product = PhysicalProduct("Laptop", 3)
digital_product = DigitalProduct("Automate the Boring Stuff with Python", "https://automatetheboringstuff.com/")
service = Service("Consultation", 2)

order.add_item(physical_product)
order.add_item(digital_product)

print("\n")
order.process_order()

print("\n")
order.add_item(service)

print("\n")
order.process_order()

print("\n")
order.remove_item(digital_product)

print("\n")
order.process_order()
