# Add and subtract two matrices
# with the numpy lib

from numpy import array, add, subtract

MatrixA = array([[1, 3, 4], [8, 5, 6]])
MatrixB = array([[8, 6, 9], [9, 0, 6]])

# Add two matrices
print("Add Matrix A to Matrix B:")
MatrixC = add(MatrixA, MatrixB)
print(MatrixC)

# Subtract two matrices
print("Subtract Matrix B from Matrix A:")
MatrixC = subtract(MatrixA, MatrixB)
print(MatrixC)
