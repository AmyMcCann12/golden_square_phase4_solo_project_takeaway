class Menu():
    def __init__(self):
        self.dishes = []
        pass

    def add(self, dish):
        self.dishes.append(dish)
        # Parameters:
        #     dish: an instance of dish
        # Returns:
        #     No return
        # Side-effects: 
        #     Adds the dish to the dishes property of the self object

    def remove(self, dish):
        if dish not in self.dishes:
            raise Exception("Dish cannot be removed as it is not on the menu")
        self.dishes.remove(dish)
        # Parameters:
        #     dish: an instance of dish
        # Returns:
        #     No return
        # Side-effects: 
        #     Removes the dish from the dishes property of the self object


    def view_menu(self):
        formatted_menu = [dish.format_item() for dish in self.dishes]
        return formatted_menu
        # Parameters:
        #     None
        # Returns:
        #     a formatted list of dishes with their prices
        # Side-effects:
        #     None