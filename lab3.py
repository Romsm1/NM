# создание матрицы
def create_matrix(rows, cols, random=True):
    #  создание матрицы rows x cols(строки на столбцы). если random=True, заполним матрицу случ числами, иначе введем элементы с клавиатуры
    if random:
        import random
        matrix = [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)] # заполнение случ числами от -10 до 10
    else:
        matrix = [] # список для хранения матрицы
        print(f"Введите элементы матрицы {rows}x{cols}: ")
        for i in range(rows):
            row = list(map(int, input(f"Строка {i + 1}: ").split()))
            if len(row) != cols: # проверка соответствует ли кол-во элементов кол-ву столбцов
                print("Неверное количество элементов в строке.")
                return None
            matrix.append(row) # добавление введенной строки в матрицу
    return matrix

# функция размерности вывода матрицы
def print_matrix_shape(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    print(f"Размерность матрицы: {rows}x{cols}")

# Функция для вывода матрицы
def print_matrix(matrix):
    print("Матрица: ")
    for row in matrix:
        print(' '.join(map(str, row)))

# Функция для транспонирования матрицы
def transpose_matrix(matrix):
    if not matrix or not matrix[0]:
        print("Матрица пустая или не определена.")
        return None
    # размеры матрицы
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    # заполняем матрицу
    for i in range(rows): # заполняем матрицу
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    print("Транспортированная матрица: ")
    print_matrix(transposed)
    return transposed

# Функция для умножения матрицы
def multiply_matrix_scalar(matrix, scalar):
    # умножение каждого элемента на скалярное число
    result = [[cell * scalar for cell in row] for row in matrix]
    print(f"Умножение матрицы на {scalar}: ")
    print_matrix(result)
    return result
