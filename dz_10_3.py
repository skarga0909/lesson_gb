class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __str__(self):
        return f"{self.number}"

    def __sub__(self, other):
        if int(self.number - other.number) > 0:
            return Cell(self.number - other.number)
        else:
            print('Результат вычитания двух клеток меньше 0')

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __floordiv__(self, other):
        return Cell(self.number // other.number)

    def make_order(self, number):
        row = self.number // number
        row_1 = self.number % number
        print(('*' * number + '\n') * row + '*' * row_1)


cell_1 = Cell(3)
cell_2 = Cell(18)
addition = cell_1 + cell_2
print('addition:', addition)
subtraction = cell_1 - cell_2
print('subtraction:', subtraction)
multiplication = cell_1 * cell_2
print('multiplication:', multiplication)
division = cell_1 // cell_2
print('division:', division)
cell_2.make_order(3)
