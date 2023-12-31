class Receipt():
    def __init__(self):
        pass

    def add_order(self, order):
        self.order = order

    def order_total(self):
        total = 0
        for item in self.order.order_list:
            total += item[0].price * item[1]
        return total

    def get_receipt(self):
        order_confirmation = f"Order Confirmation:\n{self.order.view_order()}Total Order: {self.order.order_list[0][0].format_price(self.order_total())}"
        return order_confirmation