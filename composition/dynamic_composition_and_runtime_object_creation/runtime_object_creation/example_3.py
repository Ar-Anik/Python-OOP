class Table:
    def __init__(self, table_number):
        self.table_number = table_number
        self.orders = []
        print(f"Table {self.table_number} is ready.")

    def add_order(self, order):
        self.orders.append(order)
        print(f"Order added to table {self.table_number} : {order}")

    def show_order(self):
        print(f"Orders for table {self.table_number} : {(', '.join(self.orders)) if self.orders else 'No Orders yet.'}")

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.tables = {}
        print(f"Restaurant {self.name} is now open")

    def add_table(self, table_number):
        if table_number not in self.tables:
            self.tables[table_number] = Table(table_number)
        else:
            print(f"Table {table_number} is already available.")

    def add_order_to_table(self, table_number, order):
        if table_number in self.tables:
            self.tables[table_number].add_order(order)
        else:
            print(f"Table {table_number} does not exist. Please add the table first.")

    def show_all_orders(self):
        print(f"All Orders in Restaurant {self.name}")
        for table in self.tables.values():
            table.show_order()

    def __del__(self):
        print(f"Restaurant {self.name} is closing. All tables and orders will be removed.")


restaurant = Restaurant("Dorbar Hall")

restaurant.add_table(1)
restaurant.add_table(2)

restaurant.add_order_to_table(1, "Pasta")
restaurant.add_order_to_table(1, "Salad")
restaurant.add_order_to_table(2, "Steak")

restaurant.show_all_orders()

del restaurant
