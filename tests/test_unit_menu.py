from lib.menu import Menu
from unittest.mock import Mock
import pytest

"""
Given I have a menu
it is initialised with an empty list of dishes
"""
def test_menu_has_dishes_property_when_created():
    menu = Menu()
    assert menu.dishes == []

"""
Given I have a menu with no dishes,
view_menu returns an empty list
"""

def test_empty_menu_formatted():
    menu = Menu()
    assert menu.view_menu() == ""

"""
Given I have a menu, I can add dishes 
to the menu (use mock classes)
and these are reflected in the list of dishes property
"""
def test_add_two_dishes_to_menu():
    dish1_mock = Mock()
    dish2_mock = Mock()
    menu = Menu()
    menu.add(dish1_mock)
    menu.add(dish2_mock)
    assert menu.dishes == [dish1_mock, dish2_mock]

"""
Given I have a menu, I can remove dishes from the menu (use mock classes)
and these updates are reflected in the list of dishes property
"""

def test_add_dishes_and_remove_dishes_from_menu():
    dish1_mock = Mock()
    dish2_mock = Mock()
    menu = Menu()
    menu.add(dish1_mock)
    menu.add(dish2_mock)
    menu.remove(dish1_mock)
    assert menu.dishes == [dish2_mock]

"""
Given I have a menu
I can view that menu in a formatted structure
(use mock classes)
"""

def test_view_formatted_menu():
    dish1_mock = Mock()
    dish2_mock = Mock()
    dish1_mock.format_item.return_value = "Pizza: £10.00"
    dish2_mock.format_item.return_value = "Pasta: £5.50"
    menu = Menu()
    menu.add(dish1_mock)
    menu.add(dish2_mock)
    assert menu.view_menu() == "Pizza: £10.00\nPasta: £5.50\n"

"""
Given I have a menu, I can check if a certain
dish is on the menu
"""

def test_check_and_confirm_if_dish_is_on_menu():
    dish1_mock = Mock()
    dish2_mock = Mock()
    dish3_mock = Mock()
    menu = Menu()
    menu.add(dish1_mock)
    menu.add(dish3_mock)
    assert menu.check_dish(dish1_mock) == True
    assert menu.check_dish(dish2_mock) == False