"""
# Test Components in Isolation
1. Test each class independently before testing the composed object.
2. Use unit tests to verify the correctness of individual methods and behaviors.
"""

from code import Menu, Order, Restaurant

def test_menu_get_item_price():
    menu = Menu({"Pizza": 10.99, "Burger": 8.99})
    assert menu.get_item_price('Pizza') == 10.99, "Not Found in Item"
    assert menu.get_item_price('Burger') == 8.99, "Not Found in Item"
    assert menu.get_item_price("Sushi") is None, "Item Not Work"

test_menu_get_item_price()      # run from terminal, `python unit_testing.py test_menu_get_item_price`

def test_order_add_item():
    order = Order()
    order.add_item('Pizza', 2)
    assert order.order_items == [('Pizza', 2)], "Order Item Not Found"

test_order_add_item()       # run from terminal, `python unit_testing.py test_order_add_item`

def test_restaurant_add_to_order():
    menu = Menu({'Pizza': 10.99, 'Burger': 8.99})
    restaurant = Restaurant(menu)

    restaurant.add_to_order('Pizza', 3)
    assert restaurant.order.order_items == [('Pizza', 3)], 'Order service not work properly'

    try:
        restaurant.add_to_order('Sushi', 2)
    except Exception as e:
        print(e)
        assert str(e) == "Sushi is not on the menu."

test_restaurant_add_to_order()      # run from terminal, `python unit_testing.py test_restaurant_add_to_order`
