# תרגיל 1
# פונקציות א' ו- ד' טהורות
# פונקציה ב' לא טהורה יש פלט
# mutation פונקציה ג' לא טהורה יש


# תרגיל 2
def add_price(total, price):
    return total + price

total = 0
total = add_price(total, 10)
total = add_price(total, 10)
print(total)
print(add_price(0, 10))
print(add_price(0, 10))


# תרגיל 5
def top_three(numbers):
    sort_list = sorted(numbers, reverse=True)
    return [sort_list[0], sort_list[1], sort_list[2]]

scores = [70, 95, 88, 60, 99]
print(top_three(scores))
print(scores)

