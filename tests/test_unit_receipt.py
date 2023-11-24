from unittest.mock import Mock
from lib.receipt import *

"""
Given I have a receipt
I can calculate the total cost for the dishes
(use mock classes)
"""

def test_calculate_total_for_order():
    order_mock = Mock()
    dish1_mock = Mock()
    dish2_mock = Mock()
    dish1_mock.price = 10
    dish2_mock.price = 4
    order_mock.order_list = [[dish1_mock, 2], [dish2_mock,3]]
    receipt = Receipt(order_mock)
    assert receipt.order_total() == 32

"""
Given I have a receipt
I can view an itemised list of the order with the grand total
(use mock classes)
"""

def test_view_itemised_list_of_order():
    dish1_mock = Mock()
    dish1_mock.dish_name = "Pizza"
    dish1_mock.price = 10
    dish2_mock = Mock()
    dish2_mock.dish_name = "Pasta"
    dish2_mock.price = 7.50
    order_mock = Mock() 
    order_mock.order_list = [[dish1_mock, 2],[dish2_mock, 4]]
    order_mock.view_order.return_value = "2 x Pizza: £20.00\n4 x Pasta: £30.00\n"
    receipt = Receipt(order_mock)
    assert receipt.get_receipt() == "Order Confirmation:\n2 x Pizza: £20.00\n4 x Pasta: £30.00\nTotal Order: £50.00"
