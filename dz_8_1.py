import re

email_parse = 'someone@geekbrains.ru'
pattern_1 = re.compile(r"\.")
point = pattern_1.findall(email_parse)
if not point:
    raise ValueError(f'wrong email: {email_parse}')
# print(point)
pattern = re.compile(r"@")
mail = pattern.split(email_parse)
# print(mail)
result_dict = {'username': mail[0], 'domain': mail[1]}
print(result_dict)
