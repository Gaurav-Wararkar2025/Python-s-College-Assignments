#Lab Assignment-1

"""
Perform the following operations using Numpy

b) Develop a Python program to generate two 3x3 matrices filled with random integers (1 to 9),
then perform matrix addition and matrix multiplication.

"""

import numpy as np

matrix1 = np.random.randint(1, 10, size=(3, 3))
matrix2 = np.random.randint(1, 10, size=(3, 3))

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

# Matrix Addition
addition = matrix1 + matrix2
print("\nMatrix Addition:")
print(addition)

# Matrix Multiplication
multiplication = np.dot(matrix1, matrix2)
print("\nMatrix Multiplication:")
print(multiplication)
