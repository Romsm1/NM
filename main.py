import numpy as np
def determinant_3x3(matrix):
    return (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
            matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
            matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))


A1 = [[3, -2, 4],
     [3, 4, -2],
     [2, -1, -1]
     ]

print("Определитель матрицы 3х3: ", determinant_3x3(A1))


def determinant_2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


B = [[3, -2],
     [3, 4]
     ]

print("Определитель матрицы 2х2: ", determinant_2x2(B))



A2 = np.array([[3, -2, 4],
     [3, 4, -2],
     [2, -1, -1]])

b = np.array([21, 9, 10])

A_inv = np.linalg.inv(A2)

X =


print("Решение системы X: ", X)


