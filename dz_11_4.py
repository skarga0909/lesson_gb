class OfficeEquipment:
    def __init__(self, article, name, model, price, balance):
        self.article = article
        self.name = name
        self.model = model
        self.price = price
        self.balance = balance


class Printer(OfficeEquipment):
    def __init__(self, article, name, model, price, balance, color):
        super().__init__(article, name, model, price, balance)
        self.article = article
        self.name = name
        self.price = price
        self.model = model
        self.balance = balance
        self.color = color


class Scanner(OfficeEquipment):
    def __init__(self, article, name, model, price, balance, matrix):
        super().__init__(article, name, model, price, balance)
        self.article = article
        self.name = name
        self.price = price
        self.model = model
        self.balance = balance
        self.matrix = matrix


class Xerox(OfficeEquipment):
    def __init__(self, article, name, model, price, balance, resolution):
        super().__init__(article, name, model, price, balance)
        self.article = article
        self.name = name
        self.price = price
        self.model = model
        self.balance = balance
        self.resolution = resolution
