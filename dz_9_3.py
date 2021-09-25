class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

    _income_ = {"wage": 30000, "bonus": 10000}


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        dict = self._income_
        wage = int(dict['wage'])
        bonus = int(dict['bonus'])
        result = wage + bonus
        print(self.position, result)


worker_1 = Position('Ivan', 'Petrov', 'Silver')
worker_1.get_full_name()
worker_1.get_total_income()
print()
worker_2 = Position('Andrey', 'Sidorov', 'Porter')
worker_2.get_full_name()
worker_2.get_total_income()
