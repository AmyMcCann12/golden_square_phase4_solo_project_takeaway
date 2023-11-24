from lib.order import Order
from unittest.mock import Mock
import pytest

"""
Given I have an order
it is initialised with an empty list of dishes
"""
def test_order_initialised_with_empty_list_of_dishes():
    order = Order("", "")
    assert order.order_list == []

"""
Given an order, if we try to add an item to the order
that is not on the menu, an error is received
(use a mock class)
"""

def test_order_item_not_on_menu():
    dish_mock = Mock()
    menu_mock = Mock()
    menu_mock.check_dish.return_value = False
    receipt_mock = Mock()
    order = Order(menu_mock, receipt_mock)
    with pytest.raises(Exception) as e:
        order.add_to_order(dish_mock)
    assert str(e.value) == "Dish is not on the menu"

"""
Given an order, if we try to add a quantity of a dish
that exceeds the availability, 
an error is raised
(use a mock class)
"""

def test_add_quantity_of_item_higher_than_availability():
    dish_mock = Mock()
    dish_mock.availability = 2
    dish_mock.dish_name = "Pizza"
    menu = Mock()
    receipt = Mock()
    order = Order(menu, receipt)
    with pytest.raises(Exception) as e:
        order.add_to_order(dish_mock, 3)
    assert str(e.value) ==  "We only have 2 Pizza available, please reduce the quantity for your order."

"""
Given I have an order
I can add items to that order and these
will be added to the order_list property
(use mock class)
"""

def test_items_added_to_order():
    menu_mock = Mock()
    dish1_mock = Mock()
    dish1_mock.availability = 3
    dish2_mock = Mock()
    dish2_mock.availability = 2
    menu_mock.check_dish.return_value = True
    receipt_mock = Mock()
    order = Order(menu_mock, receipt_mock)
    order.add_to_order(dish1_mock)
    order.add_to_order(dish2_mock)
    assert order.order_list == [[dish1_mock, 1], [dish2_mock,1]]

"""
Given an order if we add an item that is already
on the order, and there is enough availability
the quantity of that item is increased
"""
def test_item_added_to_order_already_on_order_but_available():
    menu_mock = Mock()
    dish1_mock = Mock()
    dish1_mock.availability = 3
    menu_mock.check_dish.return_value = True
    receipt_mock = Mock()
    order = Order(menu_mock, receipt_mock)
    order.add_to_order(dish1_mock)
    order.add_to_order(dish1_mock, 2)
    assert order.order_list == [[dish1_mock, 3]]

"""
Given an order, if we add an item to the order
that is already on the order, and there is not enough availability
an error is raised
"""
def test_item_added_to_order_already_on_order_and_not_enough_available():
    menu_mock = Mock()
    dish1_mock = Mock()
    dish1_mock.availability = 3
    dish1_mock.dish_name = "Pizza"
    menu_mock.check_dish.return_value = True
    receipt_mock = Mock()
    order = Order(menu_mock, receipt_mock)
    order.add_to_order(dish1_mock)
    with pytest.raises(Exception) as e:
        order.add_to_order(dish1_mock, 3)
    assert str(e.value) == "We only have 3 Pizza available, you already have 1 on your order and you are trying to add an additional 3, please reduce the quantity you are trying to add."


"""
Given I have an order
I can remove items from the order 
and these will be removed from the order property
(use mock class)
"""

def test_item_can_be_removed_from_order():
    menu_mock = Mock()
    dish1_mock = Mock()
    dish1_mock.availability = 3
    dish2_mock = Mock()
    dish2_mock.availability = 2
    menu_mock.check_dish.return_value = True
    receipt_mock = Mock()
    order = Order(menu_mock, receipt_mock)
    order.add_to_order(dish1_mock)
    order.add_to_order(dish2_mock)
    order.remove_from_order(dish1_mock)
    assert order.order_list == [[dish2_mock, 1]]

"""
Given I have an order 
with an item with a quantity of 4
we can reduce the quantity of that dish on the order
"""
def test_item_quantity_can_be_reduced_on_order():
    menu_mock = Mock()
    dish1_mock = Mock()
    dish1_mock.availability = 5
    menu_mock.check_dish.return_value = True
    receipt_mock = Mock()
    order = Order(menu_mock,receipt_mock)
    order.add_to_order(dish1_mock,4)
    order.remove_from_order(dish1_mock,3)
    assert order.order_list == [[dish1_mock, 1]]
"""
Given I have an order,
I can check if a dish is on the order
"""
def test_check_dish_on_order():
    menu_mock = Mock()
    dish1_mock = Mock()
    receipt_mock = Mock()
    order = Order(menu_mock, receipt_mock)
    assert order.check_dish_on_order(dish1_mock) == False


"""
Given I have an order
I can view this order in a formatted way
(use mock class)
"""

def test_view_order_in_formatted_way():
    menu_mock = Mock()
    dish1_mock = Mock()
    dish1_mock.price = 10
    dish1_mock.availability = 3
    dish1_mock.dish_name = "Pizza"
    dish2_mock = Mock()
    dish2_mock.price = 3
    dish2_mock.availability = 1
    dish2_mock.dish_name = "Chips"
    menu_mock.check_dish.return_value = True
    receipt_mock = Mock()
    order = Order(menu_mock, receipt_mock)
    order.add_to_order(dish1_mock, 2)
    order.add_to_order(dish2_mock, 1)
    dish1_mock.format_price.return_value = "£20.00"
    dish2_mock.format_price.return_value = "£3.00"
    assert order.view_order() == "2 x Pizza: £20.00\n1 x Chips: £3.00\n"

"""
Given I have an order
I can clear the contents of my order
which will remove all dishes from my order property
(use mock class)
"""

def test_clear_contents_of_order():
    menu_mock = Mock()
    dish1_mock = Mock()
    dish1_mock.availability = 3
    menu_mock.check_dish.return_value = True
    receipt_mock = Mock()
    order = Order(menu_mock, receipt_mock)
    order.add_to_order(dish1_mock,3)
    order.clear_order()
    assert order.order_list == []

"""
Given I have an order, the order status is initially pending.
"""
def test_order_status_is_initially_pending():
    order = Order("", "")
    assert order.status == "Pending"

"""
Given I have an order
when the order is confirmed, the status property is updated to confirmed
and we confirm the decrease_availability method is called
(use mock class)
"""
def test_order_status_updated_when_order_confirmed():
    receipt_mock = Mock()
    order = Order("", receipt_mock)
    order.confirm_order()
    assert order.status == "Confirmed"

