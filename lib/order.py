from lib.receipt import *

class Order():
    def __init__(self, menu):
        self.menu = menu
        self.order_list = []
        self.status = "Pending"
        self.receipt = None

    def add_to_order(self, dish, quantity = 1):
        if not self.menu.check_dish(dish):
            raise Exception("Dish is not on the menu")
        if self.check_dish_on_order(dish):
            for item in self.order_list:
                if item[0] == dish:
                    if item[1] + quantity > dish.availability:
                        raise Exception(f"We only have {dish.availability} {dish.dish_name} available, you already have {item[1]} on your order and you are trying to add an additional {quantity}, please reduce the quantity you are trying to add.")
                    item[1] += quantity
        else:
            if dish.availability < quantity:
                raise Exception(f"We only have {dish.availability} {dish.dish_name} available, please reduce the quantity for your order.")
            self.order_list.append([dish, quantity])

    def remove_from_order(self, dish, quantity = 1):
        dish_to_update = [dish for dish in self.order_list]
        if quantity == dish_to_update[0][1]:
            self.order_list.remove([dish, quantity])
        else:
            dish_to_update[0][1] -= quantity

    def check_dish_on_order(self,dish):
        return [item[0] for item in self.order_list if item[0] == dish] != []

    def view_order(self):
        formatted_order = ""
        for item in self.order_list:
            formatted_order += (f"{item[1]} x {item[0].dish_name}: {item[0].format_price(item[1] * item[0].price)}\n")
        return formatted_order

    def clear_order(self):
        self.order_list = []

    def confirm_order(self):
        self.status = "Confirmed"
        for item in self.order_list:
            item[0].decrease_availability(item[1])
        self.receipt = Receipt(self)
        return self.receipt.get_receipt()



