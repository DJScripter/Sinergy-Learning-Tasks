import collections

# Пример словаря с питомцами
pets = {
    1: {'name': 'Мурзик', 'species': 'Кот', 'age': 5},
    2: {'name': 'Бобик', 'species': 'Собака', 'age': 3},
    3: {'name': 'Хома', 'species': 'Хомяк', 'age': 1}
}

def get_pet(ID):
    """Возвращает информацию о питомце по ID или False, если питомец не найден."""
    return pets[ID] if ID in pets.keys() else False

def get_suffix(age):
    """Возвращает правильный суффикс ('год', 'года', 'лет') в зависимости от возраста."""
    if age % 10 == 1 and age % 100 != 11:
        return 'год'
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return 'года'
    else:
        return 'лет'

def pets_list():
    """Выводит информацию о всех питомцах в словаре pets."""
    if not pets:
        print("Список питомцев пуст.")
        return
    
    for ID, info in pets.items():
        suffix = get_suffix(info['age'])
        print(f"ID: {ID}, Имя: {info['name']}, Вид: {info['species']}, Возраст: {info['age']} {suffix}")

def create():
    """Добавляет нового питомца в словарь pets с новым ID."""
    # Получаем последний ID
    last_id = collections.deque(pets, maxlen=1)[0] if pets else 0
    new_id = last_id + 1
    
    # Запрашиваем данные о новом питомце
    name = input("Введите имя питомца: ")
    species = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    
    # Добавляем нового питомца в словарь
    pets[new_id] = {'name': name, 'species': species, 'age': age}
    print(f"Питомец с ID {new_id} успешно добавлен.")

# Пример использования
if __name__ == "__main__":
    # Вывод списка питомцев
    print("Список всех питомцев:")
    pets_list()
    
    # Получение информации о питомце по ID
    print("\nПоиск питомца с ID 2:")
    pet = get_pet(2)
    if pet:
        print(f"Найден питомец: Имя: {pet['name']}, Вид: {pet['species']}, Возраст: {pet['age']} {get_suffix(pet['age'])}")
    else:
        print("Питомец не найден.")
    
    # Поиск несуществующего питомца
    print("\nПоиск питомца с ID 999:")
    pet = get_pet(999)
    if pet:
        print(f"Найден питомец: Имя: {pet['name']}, Вид: {pet['species']}, Возраст: {pet['age']} {get_suffix(pet['age'])}")
    else:
        print("Питомец не найден.")
    
    # Добавление нового питомца
    print("\nДобавление нового питомца:")
    create()
    
    # Вывод обновленного списка
    print("\nОбновленный список питомцев:")
    pets_list()