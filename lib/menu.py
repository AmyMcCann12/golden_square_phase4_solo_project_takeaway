class Menu():
    def __init__(self):
        self.dishes = []
        pass

    def add(self, dish):
        self.dishes.append(dish)

    def remove(self, dish):
        self.dishes.remove(dish)

    def view_menu(self):
        formatted_menu = ""
        for item in self.dishes:
            formatted_menu += f"{item.format_item()}\n"
        return formatted_menu

    def check_dish(self, dish):
        return dish in self.dishes