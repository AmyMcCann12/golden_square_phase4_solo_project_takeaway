from lib.dish import Dish
from lib.menu import Menu
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
Given an order
if we try to add an item to the order that is not on the menu
an error is received
"""



"""
Given an order
if we try to add a quantity of a dish that exceeds the availabilty
an error is raised
"""


"""
Given an order
with 3 items added
we can view that order in a formatted way
"""

"""
Given an order
when this order is confirmed, 
the availability for each item is updated
"""

"""
Given an order is confirmed, 
an instance of the receipt class is created
and we can calculate the total value of the order
"""

"""
Given an order which is confirmed
we can view the receipt 
which will contain an itemised contents with grand total
"""