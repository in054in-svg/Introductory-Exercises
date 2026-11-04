from prices import add_vat, apply_discount
from helpers import shout
from temperature import c_to_f, describe

discount_price = apply_discount(200, 10)
vat_price = add_vat(discount_price)
print(f"""After discount: {discount_price}
With VAT: {vat_price}""")

print(shout("hi"))

cities = ["Eilat", "Haifa", "Jerusalem"]
temperatures = [35, 22, 9]
for i, city in enumerate(cities):
    t_c = temperatures[i]
    t_f = c_to_f(t_c)
    t_d = describe(t_c)
    print(f"{city}: {t_c} C / {t_f} F - {t_d}")
