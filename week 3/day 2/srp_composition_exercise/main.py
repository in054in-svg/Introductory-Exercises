from classes.cart import Cart
from classes.checkout import Checkout
from classes.israeli_vat import IsraeliVat
from classes.tax_exempt import TaxExempt
from classes.car import Engine, Car
from classes.cpu import CPU
from classes.ram import RAM
from classes.disk import Disk
from classes.computer import Computer

cart = Cart()
cart.add("Pen", 5, 4)
cart.add("Bag", 60)
checkout = Checkout(cart, IsraeliVat())
print(checkout.total())
checkout = Checkout(cart, TaxExempt())
print(checkout.total(), '\n')


car = Car("Mazda", Engine(150))
print(car.start(), '\n')


pc = Computer(CPU(8, 3.2), RAM(8), Disk(512))
print(pc)
print("Can run the game?", pc.can_run(6, 16))
