def odd_nums():
    for odd_to_15 in range(1, n + 1):
        if odd_to_15 % 2 == 1:
            yield odd_to_15


n = 15
odd_to_15 = odd_nums()
print((odd_to_15 for odd_to_15 in range(1, n + 1) if odd_to_15 % 2 == 1))
print(*(odd_to_15 for odd_to_15 in range(1, n + 1) if odd_to_15 % 2 == 1))
print(*[odd_to_15 for odd_to_15 in range(1, n + 1) if odd_to_15 % 2 == 1])
