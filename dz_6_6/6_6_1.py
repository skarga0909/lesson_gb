# 5978.5 8914.3 7879.1 1573.7
summers = input("Введите суммы продаж булочной, разделенные пробелом: ").split()
# print("Введенный суммы:", summers)
sum_str = '\n'.join(summers)

with open('bakery.csv', 'w', encoding='utf-8') as f:
    f.writelines(sum_str)