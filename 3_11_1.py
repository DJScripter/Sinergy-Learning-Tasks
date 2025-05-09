def factorial(n):
    """Вычисляет факториал числа n."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def factorial_and_list(n):
    """Принимает число n, вычисляет его факториал и возвращает список факториалов от факториала n до 1."""
    # Вычисляем факториал входного числа
    fact = factorial(n)
    
    # Создаем список факториалов от fact до 1
    result = []
    for i in range(fact, 0, -1):
        result.append(factorial(i))
    
    return result

# Пример использования
if __name__ == "__main__":
    number = 3
    print(factorial_and_list(number))  # Вывод: [720, 120, 24, 6, 2, 1]