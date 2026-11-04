# תרגיל 4
# תופיע שגיאה כי השם המבנה נדרס והפך לרשימה שלא יכולה להיקרא ולקבל ערכים TypeError
# ההסבר הוא שפייתון בודק קודם כל במשתנים מקומיים ורק אחרי זה במובנים
# קוד מתוקן:
new_list = [1, 2, 3]
numbers = list(range(5))


# תרגיל 5
cart = []

def add(cart, price):
    return cart + [price]

def total_of_cart(cart):
    return sum(cart)