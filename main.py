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



print("Решение системы X: ", 


def matrix(A2, b):
    res = []
    for row in A2:
        res.append(int(sum(row[i] * b[i] for i in range(len(b)))))
    return res


def inverse_matrix(A2, b):
    a_inv = np.linalg.inv(np.array(A2))
    output = matrix(a_inv, b)
    print(output)
    return output

inverted_matrix("Решение системы Х: ", matrix1, matrix3)