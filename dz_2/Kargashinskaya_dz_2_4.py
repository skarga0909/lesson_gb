company_employee = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
                    'директор аэлита']
i = 0
for i in range(len(company_employee)):
    # print(company_employee[i])
    post = company_employee[i].split()
    # print(post)
    name = post.pop()
    print('Привет,', name.title())
