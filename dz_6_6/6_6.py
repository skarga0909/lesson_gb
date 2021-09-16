# 5978.5 8914.3 7879.1 1573.7
with open('bakery.csv', 'r', encoding='utf-8') as f:
    bakery_str = f.read()
    bakery_list = bakery_str.split()

i = 1
for i in range(len(bakery_list)):
    print('python add_sale.py ', bakery_list[i])

num = input('Введите 2 числа через пробел: ')
num_1 = num.split()
number = list(num_1)

if len(number) > 1:
    start = int(number[0])

    finish = int(number[1])

    bakery_2 = bakery_list[start - 1:finish]

    for i in bakery_2:
        print(i)

if len(number) < 2:
    key = int(number[0])

    if key == 0:
        print('python show_sales.py')
        print(bakery_str)

    if key > 0 in range(len(bakery_list)):
        bakery_1 = bakery_list[key - 1:]
        for i in bakery_1:
            print(i)