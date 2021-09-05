def thesaurus(em):
    dic = {}
    for i in em:
        key = i[0]
        if key in dic:
            dic[key].append(i)
        else:
            dic[key] = [i]
    return dic


employee_name = ['Андрей', 'Иван', 'Мария', 'Светлана', 'Александр', 'Илья', 'Софья']
result = thesaurus(employee_name)
print(result)
