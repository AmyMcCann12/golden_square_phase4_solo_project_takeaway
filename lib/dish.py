import math

class Dish():
    # User-facing properties:
    #   dish_name: string
    #   price: float (2dp)
    #   availability: int
    def __init__(self, dish_name, price, availability = 1):
        if dish_name == "" or type(dish_name) != str:
            raise Exception("Dish must be a string and cannot be an empty string")
        if price <= 0 or ("." in str(price) and len(str(price).split(".")[1]) > 2):
            raise Exception("Price must be a number greater than 0 and maximum 2 decimal places")
        self.dish_name = dish_name
        self.price = price
        self.availability = availability

    def format_item(self):
        print(self.price)
        if type(self.price) == int:
            return f"{self.dish_name}: £{self.price}.00"
        elif len(str(self.price).split(".")[1]) == 1:
            return f"{self.dish_name}: £{self.price}0"
        else:
            return f"{self.dish_name}: £{self.price}"

