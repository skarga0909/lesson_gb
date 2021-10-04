class ComplexNumbers:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return other + self.number

    def __mul__(self, other):
        return other * self.number


num_1 = ComplexNumbers(8)
num_2 = ComplexNumbers(76)
res_1 = num_1 + num_2
print(res_1)
res_2 = num_1 * num_2
print(res_2)
