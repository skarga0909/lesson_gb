import json


with open('users.csv', 'r') as f:
    users = f.read().splitlines()
    print(users)

with open('hobby.csv', 'r') as f:
    hobby = f.read().splitlines()
    print(hobby)

dict = {}

for i in range(len(users)):
    key = users[i]
    key = key.split(',')
    key = "".join(key)

    if i not in range(len(hobby)):
        value = 'None'
    else:
        value = hobby[i]

    dict[key] = value

print(dict)

with open('user_hobby_dict', 'w', encoding='utf-8') as f:
        json.dump(dict, f, ensure_ascii=False, indent=4)

with open('user_hobby_dict', 'r', encoding='utf-8') as f:
        dict = json.load(f)

print(dict)

if len(users) < len(hobby):
    print('Error 1')
    exit(1)