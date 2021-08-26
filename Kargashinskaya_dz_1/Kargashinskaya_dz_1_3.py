list_1 = []
for i in range(100):
    list_1.append(i + 1)
    i = i + 1
# print(list_1)

for idx in range(len(list_1)):
    if list_1[idx] == 1:
        print(list_1[idx], 'процент')
    elif 1 < list_1[idx] < 5:
        print(list_1[idx], 'процента')
    elif 4 < list_1[idx] <= 20:
        print(list_1[idx], 'процентов')
    elif list_1[idx] > 20 and list_1[idx] % 10 == 1:
        print(list_1[idx], 'процент')
    elif list_1[idx] > 20 and list_1[idx] % 10 == 2 or list_1[idx] % 10 == 3 or list_1[idx] % 10 == 4:
        print(list_1[idx], 'процента')
    elif list_1[idx] > 20 and list_1[idx] % 10 == 5 or list_1[idx] % 10 == 6 or list_1[idx] % 10 == 7 or list_1[
        idx] % 10 == 8 or list_1[idx] % 10 == 9 or list_1[idx] % 10 == 10 or list_1[idx] % 10 == 0:
        print(list_1[idx], 'процентов')
