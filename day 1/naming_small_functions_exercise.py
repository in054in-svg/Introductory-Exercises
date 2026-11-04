# # תרגיל 1
# LIMIT_OF_RESULT = 500
# DISCOUNT_VALUE = 50


# def price_calculation(price: float, discount: float) -> float:
#     total = price * discount
    
#     return discount_calculation(total)


# def discount_calculation(total_price: float) -> float:
#     if total_price > LIMIT_OF_RESULT:
#         total_price -= DISCOUNT_VALUE

#     return total_price

# print(price_calculation(120, 5))
# print(price_calculation(30, 2))


# # תרגיל 2
# # total_price (a variable)
# # number_of_students (a variable)
# # max_grade (a variable)
# # VAT_RATE (a constant that never changes)
# # get_average (a function)


# # תרגיל 3
# def calculate_average(grades: list) -> float:
#     total = 0
#     for g in grades:
#         total = total + g
#     avg = total / len(grades)
#     return avg


# def is_passing(grades_avg: float) -> bool:
#     return grades_avg >= 55


# def print_report(name: str, avg: float, status: bool) -> None:
#     if status:
#         print(name + ': average', avg, '- passed')
#     else:
#         print(name + ': average', avg, '- failed')


# avg = calculate_average()
# report('Dana', [80, 85])
# report('Avi', [50, 46])


# # תרגיל 4
# MINIMUM_PRICE_FOR_FREE_DELIVERY = 200
# DELIVERY_PRICE = 30
# def add_delivery_cost(total):
#     if total < MINIMUM_PRICE_FOR_FREE_DELIVERY:
#         total = total + DELIVERY_PRICE
#     return total
# print(add_delivery_cost(150))
# print(add_delivery_cost(250))


# # תרגיל 5
# def is_valid_password(password: str) -> bool:
#     return len(password) >= 8 and 