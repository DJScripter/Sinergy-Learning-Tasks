# Создаем пустой словарь
pets = {}

# Запрашиваем данные через input()
name = input("Введите кличку питомца: ")
species = input("Введите вид питомца: ")
age = int(input("Введите возраст питомца: "))  # Преобразуем в int
owner = input("Введите имя владельца: ")

# Создаем вложенный словарь для питомца
pet_info = {
    "Вид питомца": species,
    "Возраст питомца": age,
    "Имя владельца": owner
}

# Добавляем информацию в словарь pets с ключом - именем питомца
pets[name] = pet_info

# Определяем правильную форму "год/года/лет"
if age % 10 == 1 and age % 100 != 11:
    age_string = "год"
elif age % 10 in [2, 3, 4] and age % 100 not in [12, 13, 14]:
    age_string = "года"
else:
    age_string = "лет"

# Выводим информацию о питомце, используя keys() и values()
for pet_name, info in pets.items():
    species = info["Вид питомца"]
    age = info["Возраст питомца"]
    owner = info["Имя владельца"]
    print(f'Это {species} по кличке "{pet_name}". Возраст: {age} {age_string}. Имя владельца: {owner}')