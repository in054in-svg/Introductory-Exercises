class Checkout:
    def __init__(self, cart, tax):
        self.cart = cart
        self.tax = tax
        
    def total(self) -> float:
        return self.tax.apply(self.cart.subtotal())