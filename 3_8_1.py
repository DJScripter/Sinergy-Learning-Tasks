# Считываем количество чисел
N = int(input())

# Создаем пустой список для чисел
numbers = []

# Считываем N чисел и добавляем их в список
for _ in range(N): # Переменная не нужна тут, поэтому заменяем на _
    num = int(input())
    numbers.append(num)

# Переворачиваем список
numbers.reverse()
# Или можно использовать срез, например numbers = numbers[::-1]

# Выводим количество чисел и перевернутый массив
print(N)
for num in numbers:
    print(num)
