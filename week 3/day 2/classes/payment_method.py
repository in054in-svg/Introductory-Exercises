class PaymentMethod:
    def pay(self, amount: float) -> None:
        raise NotImplemented('every payment method must implement pay()')
    
    def fee(self, amount: float) -> str:
        return 0