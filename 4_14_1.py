def print_list_recursive(lst, index=0):
    """Рекурсивно выводит элементы списка от первого до последнего."""
    # Базовый случай: если индекс равен длине списка
    if index == len(lst):
        print("Конец списка")
        return
    
    # Вывод текущего элемента
    print(lst[index])
    
    # Рекурсивный вызов для следующего индекса
    print_list_recursive(lst, index + 1)

# Исходный список
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# Вызов функции
print_list_recursive(my_list)