class Menu:
    def __init__(self, items):
        self.items = items      # dict of item names and prices

    def get_item_price(self, item_name):
        return self.items.get(item_name, None)

class Order:
    def __init__(self):
        self.order_items = []

    def add_item(self, item_name, quantity):
        self.order_items.append((item_name, quantity))

class Restaurant:
    def __init__(self, menu):
        self.menu = menu
        self.order = Order()

    def add_to_order(self, item_name, quantity):
        if self.menu.get_item_price(item_name):
            self.order.add_item(item_name, quantity)
        else:
            raise ValueError(f"{item_name} is not on the menu.")

