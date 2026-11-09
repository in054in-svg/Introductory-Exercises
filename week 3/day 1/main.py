from classes.product import Product
from classes.student import Student

# תרגיל 2
pen = Product("Pen", 5)
print(pen.name, pen.price, pen.quantity)
try:
    Product("Bad", -10)
except ValueError as error:
    print("error:", error)



# תרגיל 3
dana = Student("Dana")
print(dana.average())
dana.add_grade(90)
dana.add_grade(75)
print(dana.average())
print(dana)
