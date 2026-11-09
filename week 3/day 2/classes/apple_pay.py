from classes.payment_method import PaymentMethod

class ApplePay(PaymentMethod):
    def pay(self, amount: float) -> str:
        return 'Paid with Apple pay 100'