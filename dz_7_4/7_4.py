import os

ROOT = os.path.dirname(__file__)
some_path = os.path.join(ROOT, 'some_data')

result = {0: 0, 10: 0, 100: 0, 1000: 0, 10000: 0, 100000: 0, 1000000: 0}
keys = [0, 10, 100, 1000, 10000, 100000, 1000000]

for root, dirs, files in os.walk(some_path):
    for file in files:
        size = os.stat(os.path.join(root, file)).st_size
        if size == 0:
            result[0] += 1
            continue
        for idx, key in enumerate(keys):
            if idx == len(keys) - 1:
                print(f'A very big file {file}')
                break
            if key < size <= keys[idx + 1]:
                result[keys[idx + 1]] += 1
                break
print(result)
