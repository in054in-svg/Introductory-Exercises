# תרגיל 1
VAT_RATE = 0.17
def add_vat(amount):
    return round(amount * (1 + VAT_RATE), 2)

def apply_discount(amount, percent):
    return amount * ((100 - percent) / 100)