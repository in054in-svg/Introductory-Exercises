from classes.payment_method import PaymentMethod

class CreditCard(PaymentMethod):
    def pay(self, amount: float) -> str:
        return 'Charging card 100'
    
    def fee(self, amount: float) -> str:
        return 0.02 * amount