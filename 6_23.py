import random
import time
import os

# Создаем игровое поле
width = 10  # Ширина поля
height = 10  # Высота поля
field = []
for i in range(height):
    row = ["🌿" for j in range(width)]  # Заполняем поле травой
    field.append(row)

# Задаем начальные параметры
helicopter = {"x": 0, "y": 0, "water": 0, "lives": 3, "tanks": 1}  # Вертолет: позиция, вода, жизни, резервуары
score = 0  # Очки
trees = []  # Список деревьев
fires = []  # Список горящих деревьев
river = []  # Список клеток с рекой
shop = {"x": width-1, "y": height-1}  # Магазин в углу
hospital = {"x": 0, "y": height-1}  # Госпиталь в углу

# Функция для проверки, что клетка на поле
def is_valid(x, y):
    return 0 <= x < width and 0 <= y < height

# Генерируем реку
def generate_river():
    for i in range(height):
        if random.randint(0, 2) == 0:  # Случайно добавляем воду
            field[i][width//2] = "🌊"
            river.append((width//2, i))

# Генерируем деревья
def generate_trees():
    for i in range(5):  # Добавляем 5 деревьев
        x = random.randint(0, width-1)
        y = random.randint(0, height-1)
        if is_valid(x, y) and field[y][x] == "🌿":
            field[y][x] = "🌳"
            trees.append((x, y))

# Генерируем пожар
def generate_fire():
    if trees:  # Если есть деревья
        tree = random.choice(trees)
        x, y = tree
        if field[y][x] == "🌳":  # Если дерево не горит
            field[y][x] = "🔥"
            fires.append((x, y))

# Показываем поле
def draw_field():
    os.system("cls" if os.name == "nt" else "clear")  # Очищаем экран
    for y in range(height):
        for x in range(width):
            if x == helicopter["x"] and y == helicopter["y"]:
                print("🚁", end=" ")
            elif x == shop["x"] and y == shop["y"]:
                print("🏪", end=" ")
            elif x == hospital["x"] and y == hospital["y"]:
                print("🏥", end=" ")
            else:
                print(field[y][x], end=" ")
        print()
    print("Очки:", score, "Жизни:", helicopter["lives"], "Вода:", helicopter["water"])

# Движение вертолета
def move_helicopter(direction):
    new_x, new_y = helicopter["x"], helicopter["y"]
    if direction == "w" and is_valid(new_x, new_y-1):
        new_y -= 1
    elif direction == "s" and is_valid(new_x, new_y+1):
        new_y += 1
    elif direction == "a" and is_valid(new_x-1, new_y):
        new_x -= 1
    elif direction == "d" and is_valid(new_x+1, new_y):
        new_x += 1
    helicopter["x"], helicopter["y"] = new_x, new_y

# Главная функция игры
def main():
    global score
    generate_river()  # Создаем реку
    generate_trees()  # Создаем деревья
    field[shop["y"]][shop["x"]] = "🏪"  # Ставим магазин
    field[hospital["y"]][hospital["x"]] = "🏥"  # Ставим госпиталь

    while helicopter["lives"] > 0:
        draw_field()  # Показываем поле
        action = input("Действие (w/a/s/d - двигаться, f - тушить, b - купить танк, h - госпиталь): ")

        # Двигаем вертолет
        if action in ["w", "a", "s", "d"]:
            move_helicopter(action)

        # Проверяем, где вертолет
        x, y = helicopter["x"], helicopter["y"]
        if (x, y) in river and helicopter["water"] < helicopter["tanks"]:
            helicopter["water"] += 1  # Берем воду
            print("Взяли воду!")

        # Тушим пожар
        if action == "f" and helicopter["water"] > 0:
            for fx, fy in fires:
                if abs(x - fx) <= 1 and abs(y - fy) <= 1:  # Если рядом с огнем
                    field[fy][fx] = "🌿"  # Тушим
                    fires.remove((fx, fy))
                    trees.remove((fx, fy))
                    helicopter["water"] -= 1
                    score += 10  # Добавляем очки
                    print("Потушено!")
                    break

        # Покупаем танк в магазине
        if action == "b" and x == shop["x"] and y == shop["y"] and score >= 20:
            helicopter["tanks"] += 1
            score -= 20
            print("Куплен новый танк!")

        # Лечимся в госпитале
        if action == "h" and x == hospital["x"] and y == hospital["y"] and score >= 15:
            helicopter["lives"] += 1
            score -= 15
            print("Здоровье восстановлено!")

        # Обновляем игру
        if random.randint(0, 5) == 0:  # Случайно создаем новое дерево
            generate_trees()
        if random.randint(0, 3) == 0:  # Случайно зажигаем пожар
            generate_fire()

        # Проверяем пожары
        for fx, fy in fires[:]:
            if random.randint(0, 2) == 0:  # Пожар сгорает
                field[fy][fx] = "🌫️"
                fires.remove((fx, fy))
                trees.remove((fx, fy))
                score -= 5  # Теряем очки
                helicopter["lives"] -= 1  # Теряем жизнь
                print("Дерево сгорело!")

        time.sleep(0.5)  # Ждем полсекунды

    print("Игра окончена! Очки:", score)

# Запускаем игру
main()
