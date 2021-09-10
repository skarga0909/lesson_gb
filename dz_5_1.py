def odd_nums():
    for odd_to_15 in range(1, n + 1):
        if odd_to_15 % 2 == 1:
            yield odd_to_15


n = 15
odd_to_15 = odd_nums()
print('odd_nums (15)= ', odd_nums)
for i in range(9):
    print('next(odd_to_15)', next(odd_to_15))
