from lib.dish import *
from lib.menu import *
from lib.order import *
from lib.receipt import *

pizza = Dish("Pizza", 10, 20)
pasta = Dish("Pasta", 7.50, 15)
chips = Dish("Chips",3.50, 10)
garlic_bread = Dish("Garlic Bread", 1.99, 7)
ice_cream = Dish("Ice Cream", 2.49, 3)
coffee = Dish("Coffee", 1.70, 4)

menu = Menu()
menu.add(pizza)
menu.add(chips)
print(menu.view_menu())

menu.add(pasta)
menu.add(garlic_bread)

print(menu.view_menu)

order = Order(menu, Receipt())
order.add_to_order(pasta)
order.add_to_order(pizza, 5)
order.add_to_order(pasta,4)
order.add_to_order(chips,10)
print(order.view_order())
order.remove_from_order(chips,5)
order.add_to_order(garlic_bread, 3)
print(order.view_order())

print(order.confirm_order())

