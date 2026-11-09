def checkout(method, amount) -> str:
    return f'{method.pay(amount)} | fee: {method.fee(amount)}'