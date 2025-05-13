class Turtle:
    def __init__(self, x, y, s):
        # Задаем начальные координаты и шаг черепашки
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        # Двигаемся вверх, увеличиваем y
        self.y = self.y + self.s

    def go_down(self):
        # Двигаемся вниз, уменьшаем y
        self.y = self.y - self.s

    def go_left(self):
        # Двигаемся влево, уменьшаем x
        self.x = self.x - self.s

    def go_right(self):
        # Двигаемся вправо, увеличиваем x
        self.x = self.x + self.s

    def evolve(self):
        # Увеличиваем шаг на 1
        self.s = self.s + 1

    def degrade(self):
        # Уменьшаем шаг на 1, проверяем, чтобы не стало 0
        if self.s <= 1:
            print("Ошибка: шаг не может быть меньше 1")
        else:
            self.s = self.s - 1

    def count_moves(self, x2, y2):
        # Считаем, сколько шагов нужно до точки (x2, y2)
        dx = x2 - self.x
        dy = y2 - self.y
        moves_x = dx // self.s
        if dx % self.s != 0:
            moves_x = moves_x + 1
        moves_y = dy // self.s
        if dy % self.s != 0:
            moves_y = moves_y + 1
        return moves_x + moves_y


# Проверяем, как работает черепашка
t = Turtle(0, 0, 2)  # Черепашка в (0,0) с шагом 2
t.go_up()  # Двигаемся вверх
print(t.x, t.y)  # Показываем координаты
t.go_right()  # Двигаемся вправо
print(t.x, t.y)  # Показываем координаты
t.evolve()  # Увеличиваем шаг
print(t.s)  # Показываем шаг
t.degrade()  # Уменьшаем шаг
print(t.s)  # Показываем шаг
t.degrade()  # Пробуем уменьшить шаг еще раз
print(t.count_moves(5, 3))  # Считаем шаги до (5,3)