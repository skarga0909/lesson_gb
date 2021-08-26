list_1 = []
list_2 = []
list_3 = []
list_4 = []
idx = 1
while idx <= 1000:
    if idx % 2:
        list_1.append(idx ** 3)
    idx += 1

print(list_1)

for number in list_1:
    summer_1 = 0
    while number // 10 != 0:
        summer_1 = summer_1 + number % 10
        number = number // 10
    summer = summer_1 + number % 10
    list_2.append(summer)
    if summer % 7 == 0:
        list_3.append(summer)
print(list_2)
print(list_3)

for ix in range(len(list_3)):
    list_3[ix] = list_3[ix] + 17
    ix = ix + 1
print(list_3)

for numb in list_3:
    while numb // 10 != 0:
        sum_1 = numb % 10
        numb = numb // 10
    sum = sum_1 + numb
    list_4.append(sum)
print(list_4)

list_5 = []
for nb in range(len(list_4)):
    if list_4[nb] % 7 == 0:
        list_5.append(list_4[nb])
print(list_5)
