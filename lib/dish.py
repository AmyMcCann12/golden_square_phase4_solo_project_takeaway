import math

class Dish():
    def __init__(self, dish_name, price, availability = 1):
        if dish_name == "" or type(dish_name) != str:
            raise Exception("Dish must be a string and cannot be an empty string")
        if price <= 0 or ("." in str(price) and len(str(price).split(".")[1]) > 2):
            raise Exception("Price must be a number greater than 0 and maximum 2 decimal places")
        self.dish_name = dish_name
        self.price = price
        self.availability = availability

    def format_price(self,number):
        if type(number) == int:
            return f"£{number}.00"
        elif len(str(number).split(".")[1]) == 1:
            return f"£{number}0"
        else:
            return f"£{number}"

    def format_item(self):
        return f"{self.dish_name}: {self.format_price(self.price)}"

    
    def increase_availability(self, increase):
        self.availability += increase
    
    def decrease_availability(self,reduction):
        self.availability -= reduction
