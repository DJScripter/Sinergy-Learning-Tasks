class CashRegister:
    def __init__(self):
        # Начинаем с пустой кассы
        self.money = 0

    def top_up(self, x):
        # Добавляем деньги в кассу
        self.money = self.money + x

    def count_1000(self):
        # Считаем, сколько тысяч в кассе
        return self.money // 1000

    def take_away(self, x):
        # Проверяем, хватает ли денег
        if x > self.money:
            print("Ошибка: не хватает денег")
        else:
            # Забираем деньги из кассы
            self.money = self.money - x


# Проверяем, как работает касса
kassa = CashRegister()
kassa.top_up(5500)  # Кладем 5500 в кассу
print(kassa.money)  # Показываем, сколько денег
print(kassa.count_1000())  # Показываем, сколько тысяч
kassa.take_away(2000)  # Забираем 2000
print(kassa.money)  # Показываем, сколько осталось
print(kassa.count_1000())  # Показываем, сколько тысяч осталось
kassa.take_away(4000)  # Пробуем забрать слишком много