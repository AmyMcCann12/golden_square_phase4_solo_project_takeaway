class Menu():
    def __init__(self):
        self.dishes = []
        pass

    def add(self, dish):
        self.dishes.append(dish)

    def remove(self, dish):
        if dish not in self.dishes:
            raise Exception("Dish cannot be removed as it is not on the menu")
        self.dishes.remove(dish)

    def view_menu(self):
        formatted_menu = [dish.format_item() for dish in self.dishes]
        return formatted_menu

    def check_dish(self, dish):
        return dish in self.dishes