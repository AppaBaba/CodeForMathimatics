# Input Matrix A and B do addtion and subtraction

# Matrices modules are from numpy library
from numpy import array, add, subtract

def MatrixInput():
    row = int(input("Number of rows:"))
    col = int(input("Number of columns:"))
    print("Enter Matrix A:")
    val = list(map(int, input().split()))
    matrix = array(val).reshape(row,col)
    return matrix

# Input Matrix A and B
print("Input Matrix A")
MatrixA = MatrixInput()
print("input Matrix B")
MatrixB = MatrixInput()

# Add two matrices
print("Add Matrix A to Matrix B:")
MatrixC = add(MatrixA, MatrixB)
print(MatrixC)

# Subtract two matrices
print("Subtract Matrix B from Matrix A:")
MatrixC = subtract(MatrixA, MatrixB)
print(MatrixC)
