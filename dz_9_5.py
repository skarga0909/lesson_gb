class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(self.title, ': Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(self.title, ': Запуск отрисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        print(self.title, ': Запуск отрисовки карандашом')


class Handle(Stationery):
    def draw(self):
        print(self.title, ': Запуск отрисовки маркером')


s = Stationery('stationery')
s.draw()
pen = Pen('pen')
pen.draw()
pencil = Pencil('pencil')
pencil.draw()
handle = Handle('handle')
handle.draw()
