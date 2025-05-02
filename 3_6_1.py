# Ввод количества чисел
N = int(input())

# Счетчик нулей
count = 0

# Цикл для ввода N чисел и подсчета нулей
for _ in range(N):
    num = int(input())
    if num == 0:
        count += 1

# Вывод результата
print(count)
