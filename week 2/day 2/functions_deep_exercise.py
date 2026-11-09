# תרגיל 2
def average(*numbers):
    if len(numbers) == 0:
        raise ValueError("need at least one number")
    return sum(numbers) / len(numbers)

print(average(80, 90))
print(average(70, 80, 90, 100))
try:
    average()
except ValueError as error:
    print("error:", error)


#  תרגיל 3
def format_profile(name, **details):
    profile = f'{name}: '
    for key, value in details.items():
        profile = f'{profile}{key}={value} '
    return profile

print(format_profile("Dana", age=24, city="Haifa"))
print(format_profile("Avi"))