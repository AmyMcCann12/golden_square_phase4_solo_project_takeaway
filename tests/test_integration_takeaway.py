from lib.dish import *
from lib.menu import *
from lib.order import *
from lib.receipt import *
import pytest

"""
Given a menu
When we add two dishes
We see those dishes reflected in the dishes property 
"""

def test_add_two_dishes_to_menu():
    dish1 = Dish("Pizza", 10, 5)
    dish2 = Dish("Pasta", 7.50, 3)
    menu = Menu()
    menu.add(dish1)
    menu.add(dish2)
    assert menu.dishes == [dish1, dish2]

"""
Given a menu
When we add three dishes
And remove one of those dishes
We see the remaining two dishes reflected in the dishes property
"""

def test_add_three_dishes_to_menu_remove_one():
    dish1 = Dish("Pizza", 10, 5)
    dish2 = Dish("Pasta", 7.50, 3)
    dish3 = Dish("Garlic Bread", 3, 2)
    menu = Menu()
    menu.add(dish1)
    menu.add(dish2)
    menu.add(dish3)
    menu.remove(dish2)
    assert menu.dishes == [dish1, dish3]

"""
Given a menu
If we try to remove a dish that has not been added,
We receive an error
"""
def test_remove_dish_that_is_not_on_menu():
    dish1 = Dish("Pasta", 10, 5)
    menu = Menu()
    with pytest.raises(Exception) as e:
        menu.remove(dish1)
    assert str(e.value) == "Dish cannot be removed as it is not on the menu"

"""
Given a menu
If we add a number of items to that menu
We are able to view a formatted version of the menu
to see both the dishes and their prices
"""

def test_menu_formatted():
    dish1 = Dish("Pizza", 10.50, 3)
    dish2 = Dish("Chips", 2.49, 6)
    dish3 = Dish("Ice Cream", 3, 5)
    menu = Menu()
    menu.add(dish1)
    menu.add(dish2)
    menu.add(dish3)
    assert menu.view_menu() == ["Pizza: £10.50", "Chips: £2.49", "Ice Cream: £3.00"]

"""
Given a menu
we are able to check if a certain dish 
is included in the menu
"""

def test_check_and_confirm_if_dish_on_menu():
    dish1 = Dish("Pizza", 9, 6)
    dish2 = Dish("Pasta", 7.50, 10)
    dish3 = Dish("Coffee", 1.50, 20)
    menu = Menu()
    menu.add(dish1)
    menu.add(dish2)
    assert menu.check_dish(dish1) == True
    assert menu.check_dish(dish3) == False

"""
Given an order
if we try to add an item to the order that is not on the menu
an error is received
"""
def test_add_item_not_on_menu():
    dish1 = Dish("Pizza", 9, 6)
    dish2 = Dish("Pasta", 7.50, 10)
    menu = Menu()
    menu.add(dish1)
    order = Order(menu)
    with pytest.raises(Exception) as e:
        order.add_to_order(dish2)
    assert str(e.value) == "Dish is not on the menu"

"""
Given an order
if we try to add a quantity of a dish that exceeds the availabilty
an error is raised
"""
def test_add_item_to_order_that_exceeds_quantity_available():
    dish1 = Dish("Pizza", 9, 2)
    menu = Menu()
    menu.add(dish1)
    order = Order(menu)
    with pytest.raises(Exception) as e:
        order.add_to_order(dish1, 3)
    assert str(e.value) == "We only have 2 Pizza available, please reduce the quantity for your order."
    

"""
Given an order
we can items to that order
and these will be added to the order_list property
"""

def test_add_item_to_order_and_view_order_list():
    dish1 = Dish("Pizza", 9, 3)
    dish2 = Dish("Pasta", 7, 2)
    menu = Menu()
    menu.add(dish1)
    menu.add(dish2)
    order = Order(menu)
    order.add_to_order(dish1, 2)
    order.add_to_order(dish2)
    assert order.order_list == [[dish1, 2], [dish2, 1]]

"""
Given an order
if we add an item to the order
that is already on the order
and there is enough availability, the quantity of that item is available
"""

def test_add_item_already_on_order_updates_quantity():
    dish1 = Dish("Pizza", 9, 5)
    menu = Menu()
    menu.add(dish1)
    order = Order(menu)
    order.add_to_order(dish1, 2)
    order.add_to_order(dish1, 2)
    assert order.order_list == [[dish1, 4]]

"""
Given an order, if we add an item to the order
that is aready on the order
but this exceeds the availability,
an error is raised
"""

def test_add_item_already_on_order_updates_quantity():
    dish1 = Dish("Pizza", 9, 3)
    menu = Menu()
    menu.add(dish1)
    order = Order(menu)
    order.add_to_order(dish1, 2)
    with pytest.raises(Exception) as e:
        order.add_to_order(dish1,2)
    assert str(e.value) == "We only have 3 Pizza available, you already have 2 on your order and you are trying to add an additional 2, please reduce the quantity you are trying to add."

"""
Given an order
with 2 items added
we can remove one of those items
"""

def test_remove_dish_from_order():
    dish1 = Dish("Pizza", 9, 20)
    dish2 = Dish("Pasta", 5.49, 5)
    menu = Menu()
    menu.add(dish1)
    menu.add(dish2)
    order = Order(menu)
    order.add_to_order(dish1)
    order.add_to_order(dish2,2)
    order.remove_from_order(dish1)
    assert order.order_list ==[[dish2,2]]

"""
Given an order
with an item added with a quantity of 3
we can reduce the quantity of that dish on the order
"""
def test_reduce_quantity_of_dish_on_order():
    dish1 = Dish("Pizza", 9, 20)
    dish2 = Dish("Pasta", 5.49, 5)
    menu = Menu()
    menu.add(dish1)
    menu.add(dish2)
    order = Order(menu)
    order.add_to_order(dish1,3)
    order.add_to_order(dish2,2)
    order.remove_from_order(dish1,2)
    assert order.order_list ==[[dish1,1], [dish2,2]]


"""
Given I have an order,
I can check if a dish is on the order
"""
def test_check_if_dish_is_on_order():
    dish1 = Dish("Pizza", 5, 10)
    dish2 = Dish("Pasta", 5.50, 4)
    menu = Menu()
    menu.add(dish1)
    menu.add(dish2)
    order = Order(menu)
    order.add_to_order(dish1)
    assert order.check_dish_on_order(dish1) == True
    assert order.check_dish_on_order(dish2) == False

"""
Given an order
with 3 items added
we can view that order in a formatted way
"""
def test_view_order_in_formatted_way():
    dish1 = Dish("Pizza", 10, 20)
    dish2 = Dish("Chips", 3.50, 10)
    menu = Menu()
    menu.add(dish1)
    menu.add(dish2)
    order = Order(menu)
    order.add_to_order(dish1)
    order.add_to_order(dish2,2)
    assert order.view_order() == "1 x Pizza: £10.00\n2 x Chips: £7.00\n"

"""
Given an order
when this order is confirmed, 
the availability for each item is updated
"""

def test_order_confirmed_dish_availability_updated():
    dish1 = Dish("Pizza", 10, 20)
    dish2 = Dish("Chips", 3.50, 10)
    dish3 = Dish("Garlic Bread", 3, 7)
    menu = Menu()
    menu.add(dish1)
    menu.add(dish2)
    menu.add(dish3)
    order = Order(menu)
    order.add_to_order(dish1)
    order.add_to_order(dish2,3)
    order.confirm_order()
    assert dish1.availability == 19
    assert dish2.availability == 7
    assert dish3.availability == 7

"""
Given an order is confirmed, 
we can calculate the total value of the order
"""

def test_calculate_total_value_of_order_once_confirmed():
    dish1 = Dish("Pizza", 10, 20)
    dish2 = Dish("Chips", 3.50, 10)
    menu = Menu()
    menu.add(dish1)
    menu.add(dish2)
    order = Order(menu)
    order.add_to_order(dish1)
    order.add_to_order(dish2,2)
    order.confirm_order()
    assert order.receipt.order_total() == 17

"""
Given an order which is confirmed
we can view the receipt 
which will contain an itemised contents with grand total
"""

def test_check_receipt_once_order_confirmed():
    dish1 = Dish("Pizza", 10, 20)
    dish2 = Dish("Chips", 3.50, 10)
    menu = Menu()
    menu.add(dish1)
    menu.add(dish2)
    order = Order(menu)
    order.add_to_order(dish1)
    order.add_to_order(dish2,2)
    assert order.confirm_order() == "Order Confirmation:\n1 x Pizza: £10.00\n2 x Chips: £7.00\nTotal Order: £17.00"
