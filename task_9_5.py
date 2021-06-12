class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Инструмент рисования: {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Инструмент рисования: {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Инструмент рисования: {self.title}')


draws = Pen('ручка')
draws.draw()
draws = Pencil('курандаш')
draws.draw()
draws = Handle('маркер')
draws.draw()
