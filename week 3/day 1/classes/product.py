class Product:
    def __init__(self, name, price, quantity = 0):
        if price < 0:
            raise ValueError('error: price cannot be negative')
        self.name = name
        self.price = price
        self.quantity = quantity