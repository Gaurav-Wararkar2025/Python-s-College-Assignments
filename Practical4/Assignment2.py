#Lab Assignment-2

"""
Develop a NumPy program to multiply a 5X3 matrix by a 3X2 matrix and create a product matrix, 
also print the product matrix. Take input data from user.
"""

import numpy as np

print("Enter elements for 5x3 Matrix:")
matrix1 = []
for i in range(5):
    row = list(map(int, input(f"Enter 3 elements for row {i+1}: ").split()))
    matrix1.append(row)

print("\nEnter elements for 3x2 Matrix:")
matrix2 = []
for i in range(3):
    row = list(map(int, input(f"Enter 2 elements for row {i+1}: ").split()))
    matrix2.append(row)

#It will Converts lists to NumPy arrays
matrix1 = np.array(matrix1)
matrix2 = np.array(matrix2)

# Matrix multiplication
product = np.dot(matrix1, matrix2)

print("\n5x3 Matrix:")
print(matrix1)

print("\n3x2 Matrix:")
print(matrix2)

print("\nProduct Matrix (5x2):")
print(product)
