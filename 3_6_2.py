# Ввод числа X
X = int(input())

# Счетчик делителей
count = 0

# Проверка делителей от 1 до sqrt(X)
i = 1
while i * i <= X:
    if X % i == 0:
        # i - делитель
        count += 1
        # Если X/i != i, то X/i тоже делитель
        if X // i != i:
            count += 1
    i += 1

# Вывод результата
print(count)
