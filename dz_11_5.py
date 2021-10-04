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

    @staticmethod
    def input_printer():
        print('Printer:', printer_product.__dict__)


class Scanner(OfficeEquipment):
    def __init__(self, article, name, model, price, balance, matrix):
        super().__init__(article, name, model, price, balance)
        self.article = article
        self.name = name
        self.price = price
        self.model = model
        self.balance = balance
        self.matrix = matrix

    @staticmethod
    def input_scanner():
        print('Scanner:', scanner_product.__dict__)


class Xerox(OfficeEquipment):
    def __init__(self, article, name, model, price, balance, resolution):
        super().__init__(article, name, model, price, balance)
        self.article = article
        self.name = name
        self.price = price
        self.model = model
        self.balance = balance
        self.resolution = resolution

    @staticmethod
    def input_xerox():
        print('Xerox', xerox_product.__dict__)


# создание объекта класса Принтер и запись его в словарь
a_p = input('Input article printer: ')
n_p = input('Input name printer: ')
m_p = input('Input model printer: ')
p_p = input('Input price printer: ')
b_p = input('Input balance printer: ')
c_p = input('Input color printer: ')
printer_product = Printer(a_p, n_p, m_p, p_p, b_p, c_p)
Printer.input_printer()

# создание объекта класса Сканер и запись его в словарь
a_s = input('Input article scanner: ')
n_s = input('Input name scanner: ')
m_s = input('Input model scanner: ')
p_s = input('Input price scanner: ')
b_s = input('Input balance scanner: ')
c_s = input('Input color scanner: ')
scanner_product = Scanner(a_s, n_s, m_s, p_s, b_s, c_s)
Scanner.input_scanner()

# создание объекта класса Ксерокс и запись его в словарь
a_x = input('Input article xerox: ')
n_x = input('Input name xerox: ')
m_x = input('Input model xerox: ')
p_x = input('Input price xerox: ')
b_x = input('Input balance xerox: ')
c_x = input('Input color xerox: ')
xerox_product = Xerox(a_x, n_x, m_x, p_x, b_x, c_x)
Xerox.input_xerox()
