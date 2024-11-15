from datetime import datetime

class TimestamMixin:
    def __init__(self):
        self.created_at = datetime.now()
        self.updated_at = None

    def update_timestamp(self):
        self.updated_at = datetime.now()

class Order(TimestamMixin):
    def __init__(self, product, quantity):
        super().__init__()
        self.product = product
        self.quantity = quantity

    def update_order(self, new_qunatity):
        self.quantity = new_qunatity
        self.update_timestamp()

order = Order("Laptop", 3)
print("Order Created At : ", order.created_at)

order.update_order(5)
print("Order Update At : ", order.updated_at)
