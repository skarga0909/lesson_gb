from sys import getsizeof
from time import perf_counter


def num_gen():
    for i in range(1, len(src)):
        if src[i] > src[i - 1]:
            yield src[i]
        i = i + 1


start = perf_counter()
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = num_gen()
print(result)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print('size gen: ', getsizeof(result))
print('time gen:', perf_counter() - start)
print()
print()

start = perf_counter()
result = set()
for i in range(1, len(src)):
    if src[i] > src[i - 1]:
        result.add(src[i])
        i = i + 1
print(result)
print('size set: ', getsizeof(result))
print('time set:', perf_counter() - start)
print()
print()

start = perf_counter()
result = []
for i in range(1, len(src)):
    if src[i] > src[i - 1]:
        result.append(src[i])
    i = i + 1
print(result)
print('size list: ', getsizeof(result))
print('time list: ', perf_counter() - start)
