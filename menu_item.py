class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_total_price(self, get_count):
        total_price = get_count * self.price
        if get_count >= 3:
            total_price *= 0.8
        return total_price


class Food(MenuItem):
    def __init__(self, name, price, netto):
        self.netto = netto
        super().__init__(name, price)


class Drink(MenuItem):
    def __init__(self, name, price, volume):
        self.volume = volume
        super().__init__(name, price)
