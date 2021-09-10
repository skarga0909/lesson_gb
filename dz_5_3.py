def students_gen():
    i = 0
    for student in tutors[0:len(klasses)]:
        list_students = (student, klasses[i])
        yield list_students
        i = i + 1
    for student in tutors[len(klasses):]:
        list_students = (student, None)
        yield list_students


list_students = students_gen()
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Станислав', 'Андрей']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б']

print(students_gen())
for el in range(len(tutors)):
    print(next(list_students))
print(next(list_students))
