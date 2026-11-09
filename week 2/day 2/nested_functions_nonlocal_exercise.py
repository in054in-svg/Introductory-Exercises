# תרגיל 2
def make_greeter(greeting):
    def the_name(name):
        return f"{greeting}, {name}"
    return the_name

hello = make_greeter("Hello")
shalom = make_greeter("Shalom")
print(hello("Dana"))
print(shalom("Avi"))


# תרגיל 4
def make_counter(step):
    counter = 0
    def counter_add():
        nonlocal counter
        counter += step
        return counter
    return counter_add

by_two = make_counter(2)
by_ten = make_counter(10)
print(by_two(), by_two())
print(by_ten())
print(by_two())