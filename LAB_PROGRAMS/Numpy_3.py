import numpy as np

matrix_A = np.array([[1, 2],[3, 4]])
matrix_B = np.array([[5, 6],[7, 8]])

matrix_sum = np.add(matrix_A, matrix_B)
print("Matrix Addition (A + B):")
print(matrix_sum)

matrix_product_elementwise = np.multiply(matrix_A,matrix_B)
print("\nElement-wise Matrix Multiplication(A * B):")
print(matrix_product_elementwise)

matrix_dot_product = np.dot(matrix_A, matrix_B)
print("\nMatrix Dot Product(A . B):")
print(matrix_dot_product)

matrix_transpose = np.transpose(matrix_A)
print("\nTranspose of Matrix A:")
print(matrix_transpose)

OUTPUT:
Matrix Addition (A + B):
[[ 6  8]
 [10 12]]

Element-wise Matrix Multiplication(A * B):
[[ 5 12]
 [21 32]]

Matrix Dot Product(A . B):
[[19 22]
 [43 50]]

Transpose of Matrix A:
[[1 3]
 [2 4]]

