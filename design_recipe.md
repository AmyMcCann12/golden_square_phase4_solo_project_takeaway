## 1. Describe the problem:

As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

## Use the twilio-python package to implement this next one. You will need to use mocks too.

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

## Fair warning: if you push your Twilio API Key to a public GitHub repository, anyone will be able to see and use it. What are the security implications of that? How will you keep that information out of your repository?

## 2. Design the Class System

See image design_class_system
![Alt text](image.png)

## class Dish():
    User-facing properties:
       dish_name: string
       price: float (2dp)
       availability: int
    def __init__(self, dish_name, price, availability = 1):
        Properties:
            dish_name: string
            price: number (max 2dp)
            availability: int (default is 1)

    def format_item(self):
        Properties:
            None
        Return:
            returns a formatted version of the dish_name and price
            dish_name: £price
        Side-effects:
            None

    def increase_availability(self, increase):
        Properties:
            increase: int (amount to increase availability by)
        Return:
            No return
        Side-effects:
            self.availability property is updated
    
    def decrease_availability(self, reduction):
        Properties:
            reduction: int (amount to reduce availability by)
        Return:
            No return
        Side-effects:
            self.availability property is updated

## class Menu():
    def __init__(self):
        pass

    def add(self, dish):
        # Parameters:
        #    dish: an instance of dish
        # Returns:
        #    No return
        # Side-effects: 
        #   Adds the dish to the dishes property of the self object

    def remove(self, dish):
        # Parameters:
        #     dish: an instance of dish
        # Returns:
        #     No return
        # Side-effects: 
        #     Removes the dish from the dishes property of the self object


    def view_menu(self):
        # Parameters:
        #     None
        # Returns:
        #     a formatted list of dishes with their prices
        # Side-effects:
        #     None
        pass
    
    def check_dish(self, dish):
        # Parameters:
        #   dish: an instance of dish
        # Returns:
        #   Boolean: true if the dish is on the menu, false otherwise
        # Side-effects:
        #      None



## class Order():
    def __init__(self, menu):
        pass

    def add_to_order(self, dish, quantity = 1):
        # Parameters:
        #   dish: an instance of the dish
        #   quantity: int (how many to add to order), default is 1
        # Returns:
        #   No return
        # Side-effects:
        #   Adds the dish (and quantity) to the order property of the self object
        #   only if the dish is on the menu and the given quanityt is available
        pass

    def remove_from_order(self, dish, quantity = 1):
        # Parameters:
        #   dish: an instance of the dish
        #   quantity: int (how many to remove from order), default is 1
        # Returns:
        #   No return
        # Side-effects:
        #   Removes the dish from the order property of the self object
        pass

    def view_order(self):
        # Parameters:
        #   None
        # Returns:
        #   a formatted list of dish names 
        #       e.g 1 x Pasta, 2 x Pizza, 1 x Garlic Bread
        # Side-effects:
        #   None
        pass

    def clear_order(self):
        # Parameters:
        #   None
        # Returns:
        #   None
        # Side-effects:
        #   Empties the order property
        pass

    def confirm_order(self):
        # Parameters:
        #   None
        # Returns:
        #   formatted receipt
        # Side-effects:
        #   Deducts the quantity of items from the availability properties
        #   of the item class
        #   Creates an instance of the receipt class
        pass

## class Receipt():
    def __init__(self, order):
        # Parameters:
        #   order: an instance of the order class
        pass

    def order_total(self):
        # Parameters:
        #   none
        # Returns:
        #   Total cost of the order
        # Side Effects:
        #   None
        pass
    

    def get_receipt(self):
        # Parameters:
        #   none
        # Returns:
        #   an itemised list with the grand total
        # Side Effects:
        #   None
        pass



