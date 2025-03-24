import numpy as np


# ЗАДАНИЕ 1
def determinant_3x3(matrix):
    return (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
            matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
            matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))


A = np.array([[3, -2, 4],
              [3, 4, -2],
              [2, -1, -1]])

print("Определитель матрицы 3х3: ", determinant_3x3(A))


# ЗАДАНИЕ 2
def determinant_2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


B = [[3, -2],
     [3, 4]
     ]

print("Определитель матрицы 2х2: ", determinant_2x2(B))

# ЗАДАНИЕ 3
def solve_linear_system(A, b):
    # Вычисляем обратную матрицу A_inv
    A_inv = np.linalg.inv(A)
    # Умножаем обратную матрицу на вектор b
    X = np.dot(A_inv, b)
    return X


# Функция для умножения транспонированной матрицы на вектор
def multiply_transposed_matrix_by_vector(A, b):
    # Транспонируем матрицу A
    A_transposed = A.T
    # Умножаем транспонированную матрицу на вектор b
    result = np.dot(A_transposed, b)
    return result


# Определяем матрицу A и вектор b
A = np.array([[3, -2, 4],
              [3, 4, -2],
              [2, -1, -1]])

b = np.array([21, 9, 10])

solution = solve_linear_system(A, b)
print("Решение СЛАУ (X):", solution)
transposed_result = multiply_transposed_matrix_by_vector(A, b)
print("Результат умножения на b:", transposed_result)
