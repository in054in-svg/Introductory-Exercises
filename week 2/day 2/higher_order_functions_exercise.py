# תרגיל 1
def apply_to_all(numbers, action):
    return list(map(action, numbers))

def double(n):
    return n * 2

print(apply_to_all([1, 2, 3], double))
print(apply_to_all([1, 2, 3], lambda n: n * n))
print(apply_to_all([1.6, 2.4], round))


# תרגיל 2
prices = [20, 75, 120, 45, 90]

print(list(filter(lambda x: x > 50, prices)))
print(list(map(lambda x: x + 10 ,filter(lambda x: x > 50, prices))))