# Ввод пятизначного числа
number = int(input("Введите пятизначное целое число: "))

# Проверка, что число пятизначное
if 10000 <= number <= 99999:
    # Извлечение цифр
    units = number % 10  # Единицы
    tens = (number // 10) % 10  # Десятки
    hundreds = (number // 100) % 10  # Сотни
    thousands = (number // 1000) % 10  # Тысячи
    ten_thousands = number // 10000  # Десятки тысяч
    
    # Вычисление: (тens ** units) * hundreds / (ten_thousands - thousands)
    result = (tens ** units) * hundreds / (ten_thousands - thousands)
    
    # Вывод результата
    print(f"Результат: {result}")
else:
    print("Ошибка: Введите пятизначное число!")
