class Cart:
    def __init__(self):
        self.items = []
    
    def add(self, name:str, price: float, quantity: int = 1) -> None:
        self.items.append((name, price, quantity))
        
    def subtotal(self) -> float:
        return sum(price * quantity for name, price, quantity in self.items)