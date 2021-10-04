class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def parsing(cls):
        p = data.date
        s = p.split('-')
        d = int(s[0])
        m = int(s[1])
        y = int(s[2])
        print(d, m, y)
        print(type(d), type(m), type(y))

    @staticmethod
    def check():
        p = data.date
        s = p.split('-')
        d = int(s[0])
        m = int(s[1])
        y = int(s[2])
        if d > 31:
            print(d, 'Дата должна быть меньше 31')
        if m > 12:
            print(m, 'Месяц должен быть меньше 12')
        if y > 2021:
            print(y, 'Год должен быть меньше 2021')


data = Date('18-10-2024')
print(type(data.date))
data.parsing()
data.check()
