from classes.payment_method import PaymentMethod

class PayPal(PaymentMethod):
    def pay(self, amount: float) -> str:
        return 'Redirecting to PayPal 100'