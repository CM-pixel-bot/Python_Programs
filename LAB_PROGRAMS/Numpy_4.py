import numpy as np


matrix_A = np.random.randint(1, 11, size=(3, 3))
matrix_B = np.random.randint(1, 11, size=(3, 3))

print("Matrix A:\n", matrix_A)
print("\nMatrix B:\n", matrix_B)


matrix_sub = np.subtract(matrix_A, matrix_B)
print("\nMatrix Subtraction (A - B):\n", matrix_sub)


elementwise_mul = np.multiply(matrix_A, matrix_B)
print("\nElement-wise Multiplication (A * B):\n", elementwise_mul)


elementwise_div = np.divide(matrix_A, matrix_B)
print("\nElement-wise Division (A / B):\n", elementwise_div.round(2))  # Rounded for readability

OUTPUT:
Matrix A:
[[ 7  3 10]
 [ 2  6  9]
 [ 1  8  5]]

Matrix B:
[[ 1  6  4]
 [ 3  5 10]
 [ 2  7  1]]

Matrix Subtraction (A - B):
[[ 6 -3  6]
 [-1  1 -1]
 [-1  1  4]]

Element-wise Multiplication (A * B):
[[ 7 18 40]
 [ 6 30 90]
 [ 2 56  5]]

Element-wise Division (A / B):
[[7.   0.5  2.5 ]
 [0.67 1.2  0.9 ]
 [0.5  1.14 5.  ]]

