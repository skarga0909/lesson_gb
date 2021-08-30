product_price = [57.8, 46.51, 97, 163.5, 149.03, 1205.6, 894.9, 999, 0.99, 35, 84.84, 234.56, 987.54, 123.89, 5]
product_price_format = []
i = 0
for el in product_price:
    rub = int(el)
    # print(rub)
    kop = float(el) - int(el)
    # print(kop)
    kop_1 = round(kop % 100, 2)
    # print(kop_1)
    kop_2 = int(kop_1 * 100)
    element = f'{rub:02d}' + ' руб.' + f'{kop_2:02d}' + ' коп.'
    product_price_format.append(element)
print(product_price_format)
print(id(product_price_format))
print()

print(product_price)
print(id(product_price))
print()

product_price.sort()
print(product_price)
print(id(product_price))
print()

product_price_new = sorted(product_price)
product_price_new.sort(reverse=True)
print(product_price_new)
print(id(product_price_new))
print()

print(sorted(product_price_new[:5]))
