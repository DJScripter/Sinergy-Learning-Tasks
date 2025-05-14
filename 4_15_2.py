# Родительский класс
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"

# Класс Autobus наследуется от Transport
class Autobus(Transport):
    def seating_capacity(self, capacity=50): # Переопределяем метод с значением по умолчанию
        return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"

# Создаем объект автобуса
bus = Autobus("Renaul Logan", 120, 50000)

# Выводим результат
print(bus.seating_capacity())