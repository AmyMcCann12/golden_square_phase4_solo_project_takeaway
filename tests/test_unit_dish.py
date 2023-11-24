from lib.dish import *
import pytest

"""
When a dish instance is created
it has a dish_name property,
price property and availability property
"""

def test_dish_properties_assigned():
    dish = Dish("Pizza", 10, 5)
    assert dish.dish_name == "Pizza"
    assert dish.price == 10
    assert dish.availability == 5

"""
Given a dish instance with no availability inputted, 
availability property defaults to 1
"""

def test_availability_default_one():
    dish = Dish("Pizza", 5)
    assert dish.availability == 1

"""
Given a dish instance with and empty string dish_name
Catch an error
"""

def test_empty_string_dish_name_catches_error():
    with pytest.raises(Exception) as e:
        dish = Dish("", 5, 10)
    assert str(e.value) == "Dish must be a string and cannot be an empty string"

"""
Given a dish instance where dish name is not a str
Catch an error
"""

def test_dish_name_not_string_catches_error():
    with pytest.raises(Exception) as e:
        dish = Dish(["dish1"], 5, 10)
    assert str(e.value) == "Dish must be a string and cannot be an empty string"

"""
Given a dish instance with invalid price
Catch an error
"""

def test_price_is_negative():
    with pytest.raises(Exception) as e:
        dish = Dish("Pizza", -5, 10)
    assert str(e.value) == "Price must be a number greater than 0 and maximum 2 decimal places"

def test_price_is_zero():
    with pytest.raises(Exception) as e:
        dish = Dish("Pizza", 0, 10)
    assert str(e.value) == "Price must be a number greater than 0 and maximum 2 decimal places"

def test_price_is_greater_than_two_dp():
    with pytest.raises(Exception) as e:
        dish = Dish("Pizza", 2.345, 1)
    assert str(e.value) == "Price must be a number greater than 0 and maximum 2 decimal places"

"""
Given a dish instance
I can see a formatted version of the dish
"dish_name: £price"
"""

def test_format_dish_item():
    dish = Dish("Pizza", 2.50, 5)
    assert dish.format_item() == "Pizza: £2.50"

"""
Given a dish instance,
I can increase its availability
"""

def test_increase_dish_availabilty():
    dish = Dish("Pizza", 2.4, 10)
    dish.increase_availability(5)
    assert dish.availability == 15

"""
Given a dish instance,
I can reduce its availability
"""

def test_reduce_dish_availability():
    dish = Dish("Pasta", 5, 4)
    dish.decrease_availability(2)
    assert dish.availability == 2