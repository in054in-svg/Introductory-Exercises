from classes.creditcard import CreditCard
from classes.paypel import PayPal
from classes.apple_pay import ApplePay
from checkout import checkout
from classes.warrior import Warrior
from classes.mage import Mage
from attack import attack
from classes.square import Square
from classes.circle import Circle

for method in [CreditCard(), PayPal(), ApplePay()]:
    print(checkout(method, 100))
print('\n')   

conan = Warrior("Conan", 100)
merlin = Mage("Merlin", 60)
attack(conan, merlin)
attack(merlin, conan)
print(merlin.name, merlin.health)
print(conan.name, conan.health, '\n')


for shape in [Square(3), Circle(3)]:
    print(round(shape.area(), 2))