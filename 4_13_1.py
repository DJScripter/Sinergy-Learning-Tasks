import random

def generate_matrix(rows, cols, min_val=-200, max_val=200):
    """Генерирует матрицу размером rows x cols со случайными целыми числами."""
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

def add_matrices(matrix1, matrix2):
    """Складывает две матрицы, возвращает результат или None, если размеры не совпадают."""
    # Проверка совместимости матриц
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return None
    
    # Сложение матриц
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]
    return result

def print_matrix(matrix, title="Матрица"):
    """Выводит матрицу с заголовком."""
    print(f"\n{title}:")
    for row in matrix:
        print(row)

# Заданные матрицы
matrix_1 = [
    [0, -2, -1, -6, -6, 0, -9, -8, -30, -9],
    [5, 12, 4, -16, -4, -9, -16, -15, 1, -26],
    [13, 39, 14, 23, -4, 40, 32, 6, -8, 23],
    [13, -8, 34, 49, 30, 18, 47, 11, -24, 11],
    [21, 73, 71, 61, -1, 79, -34, 22, 69, 67],
    [75, 25, 25, 39, 100, -12, -21, 81, -10, 87],
    [81, 63, 102, 104, 53, -44, 71, -36, -36, -9],
    [7, 98, 26, -3, 128, 94, 18, -26, 14, 21],
    [65, 128, 80, 124, 27, -32, 73, 59, 19, 34],
    [43, 111, 38, 149, 5, 112, 79, 53, 15, 92]
]

matrix_2 = [
    [0, 4, 6, 11, 15, 6, 9, 26, 15, 21],
    [-5, 4, -15, -9, -4, 2, -8, 19, -4, -1],
    [-2, -39, -19, 14, 22, 5, -34, 15, 16, -9],
    [-22, -52, 11, -11, -3, 16, -11, -6, -32, -2],
    [-61, -47, -5, -58, 16, -13, 28, -36, -64, 2],
    [-29, 23, 19, 2, -14, -87, 7, -88, 39, 7],
    [-6, 18, -97, 26, -64, 0, -72, -34, -68, -92],
    [-120, -117, -72, -129, -139, 16, -61, 36, -137, -29],
    [-112, -83, 7, -119, -132, -129, -143, -154, -23, -34],
    [32, -67, -75, -92, 15, -163, 18, 31, -162, -16]
]

# Сложение заданных матриц
result = add_matrices(matrix_1, matrix_2)
print_matrix(matrix_1, "Матрица 1")
print_matrix(matrix_2, "Матрица 2")
if result:
    print_matrix(result, "Сумма матриц")
else:
    print("\nМатрицы не могут быть сложены: разные размеры.")

# Генерация и сложение матриц произвольных размеров
print("\nПример с сгенерированными матрицами 4x3:")
rows, cols = 4, 3
gen_matrix1 = generate_matrix(rows, cols)
gen_matrix2 = generate_matrix(rows, cols)
gen_result = add_matrices(gen_matrix1, gen_matrix2)

print_matrix(gen_matrix1, f"Сгенерированная матрица 1 ({rows}x{cols})")
print_matrix(gen_matrix2, f"Сгенерированная матрица 2 ({rows}x{cols})")
if gen_result:
    print_matrix(gen_result, "Сумма сгенерированных матриц")
else:
    print("\nСгенерированные матрицы не могут быть сложены: разные размеры.")

# Пример с матрицами другого размера
print("\nПример с матрицами 10x10:")
rows, cols = 10, 10
gen_matrix3 = generate_matrix(rows, cols)
gen_matrix4 = generate_matrix(rows, cols)
gen_result2 = add_matrices(gen_matrix3, gen_matrix4)

print_matrix(gen_matrix3, f"Сгенерированная матрица 3 ({rows}x{cols})")
print_matrix(gen_matrix4, f"Сгенерированная матрица 4 ({rows}x{cols})")
if gen_result2:
    print_matrix(gen_result2, "Сумма сгенерированных матриц 10x10")
else:
    print("\nСгенерированные матрицы не могут быть сложены: разные размеры.")