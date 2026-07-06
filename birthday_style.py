from datetime import date

# --- Вспомогательные функции для отрисовки цифр звёздочками (как на табло) ---
DIGIT_PATTERNS = {
    '0': [
        " *** ",
        "*   *",
        "*   *",
        "*   *",
        " *** "
    ],
    '1': [
        "  *  ",
        " **  ",
        "  *  ",
        "  *  ",
        " *** "
    ],
    '2': [
        " *** ",
        "    *",
        " *** ",
        "*    ",
        " *** "
    ],
    '3': [
        " *** ",
        "    *",
        " *** ",
        "    *",
        " *** "
    ],
    '4': [
        "*   *",
        "*   *",
        " *** ",
        "    *",
        "    *"
    ],
    '5': [
        " *** ",
        "*    ",
        " *** ",
        "    *",
        " *** "
    ],
    '6': [
        " *** ",
        "*    ",
        " *** ",
        "*   *",
        " *** "
    ],
    '7': [
        " *** ",
        "    *",
        "    *",
        "    *",
        "    *"
    ],
    '8': [
        " *** ",
        "*   *",
        " *** ",
        "*   *",
        " *** "
    ],
    '9': [
        " *** ",
        "*   *",
        " *** ",
        "    *",
        " *** "
    ]
}

def draw_number(num_str: str) -> list[str]:
    """
    Рисует число (строку из цифр) звёздочками.
    Возвращает список строк (по одной на каждую строку рисунка).
    """
    lines = [""] * 5  # у нас 5 строк на каждую цифру
    for ch in num_str:
        pattern = DIGIT_PATTERNS.get(ch, "     ")  # если вдруг не цифра — пробел
        for i in range(5):
            if lines[i]:
                lines[i] += " "  # разделитель между цифрами
            lines[i] += pattern[i]
    return lines

# --- Основные функции задачи ---

def get_day_of_week(day: int, month: int, year: int) -> str:
    """Определяет день недели для заданной даты."""
    d = date(year, month, day)
    # weekday(): 0=понедельник, 6=воскресенье
    days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
    return days[d.weekday()]

def is_leap_year(year: int) -> bool:
    """Проверяет, високосный ли год."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_age(day: int, month: int, year: int) -> int:
    """Вычисляет возраст пользователя на сегодня."""
    today = date.today()
    age = today.year - year
    # Если день рождения ещё не наступил в этом году, уменьшаем возраст на 1
    if (month, day) > (today.month, today.day):
        age -= 1
    return age

def main():
    # 1. Запрос данных у пользователя
    while True:
        try:
            day = int(input("Введите день рождения (дд): "))
            if not (1 <= day <= 31):
                print("День должен быть от 1 до 31.")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите целое число.")

    while True:
        try:
            month = int(input("Введите месяц рождения (мм): "))
            if not (1 <= month <= 12):
                print("Месяц должен быть от 1 до 12.")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите целое число.")

    while True:
        try:
            year = int(input("Введите год рождения (гггг): "))
            # Простая проверка разумности года
            if year < 1900 or year > date.today().year:
                print(f"Год должен быть между 1900 и {date.today().year}.")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите целое число.")

    # Проверка корректности даты (чтобы не было 31 февраля и т.п.)
    try:
        date(year, month, day)
    except ValueError:
        print("Введена некорректная дата (например, 31 февраля). Запустите программу заново.")
        return

    # 2. Вычисления
    day_of_week = get_day_of_week(day, month, year)
    leap = is_leap_year(year)
    age = calculate_age(day, month, year)

    print("\n--- Результаты ---")
    print(f"День недели: {day_of_week}")
    print(f"Год был високосным: {'да' if leap else 'нет'}")
    print(f"Ваш возраст: {age} лет")

    # 3. Стилистическое преобразование даты в формат дд мм гггг звёздочками
    formatted_date = f"{day:02d} {month:02d} {year:04d}"
    # Убираем пробелы из строки, чтобы рисовать только цифры, а пробелы добавим вручную
    digits_only = formatted_date.replace(" ", "")
    drawn_lines = draw_number(digits_only)

    # Теперь нужно вставить пробелы между дд, мм, гггг.
    # Проще всего: рисуем отдельно дд, отдельно мм, отдельно гггг и склеиваем по строкам.
    dd = f"{day:02d}"
    mm = f"{month:02d}"
    yyyy = f"{year:04d}"

    dd_lines = draw_number(dd)
    mm_lines = draw_number(mm)
    yyyy_lines = draw_number(yyyy)

    print("\nДата рождения в стиле электронного табло:")
    for i in range(5):
        # Между блоками добавляем разделитель (например, несколько пробелов)
        line = dd_lines[i] + "   " + mm_lines[i] + "   " + yyyy_lines[i]
        print(line)

if __name__ == "__main__":
    main()
