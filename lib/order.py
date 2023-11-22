class Order():
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




