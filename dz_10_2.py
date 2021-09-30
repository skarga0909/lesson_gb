class Clothes:
    def __init__(self, name=" "):
        self.name = name


class Coat(Clothes):
    def __init__(self, v):
        super().__init__()
        self.v = v

    @property
    def expenses(self):
        exp_1 = self.v / 6.5 + 0.5
        return exp_1


class Suit(Clothes):
    def __init__(self, h):
        super().__init__()
        self.h = h

    @property
    def expenses(self):
        exp_2 = 2 * self.h + 0.3
        return exp_2


o = Coat(50)
f = Suit(180)
res_1 = o.expenses
res_2 = f.expenses
res = res_1 + res_2
print(res)
