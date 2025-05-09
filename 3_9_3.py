# Ввод последовательности чисел через пробел
numbers = input().split()

# Множество для хранения уже встреченных чисел
seen = set()

# Проверка каждого числа
for num in numbers:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)
