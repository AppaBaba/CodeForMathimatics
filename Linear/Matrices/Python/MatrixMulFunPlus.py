def MatrixInput(rows, cols):
        Mat = [[int(input()) for c in range (cols)] for r in range(rows)]
        return Mat
def MatrixPrint(Mat):
        for row in Mat:
                for col in row:
                        print(col, end = " ")
                print()

def MatrixMul(MatA, MatB):
        MatC = [ [ 0 for i in range(Acols) ] for j in range(Brows) ]
        if(Brows != Acols):
                print("Soultion not possible")
                return MatC
        for Arow in range(len(MatA)):
                for Acol in range(len(MatA[0])):
                        for Brow in range(len(MatB)):
                                MatC[Arow][Acol] += MatA[Arow][Brow] * MatB[Brow][Acol]
        return MatC
        
        
Arows = int(input("Number of rows for Matrix A:"))
Acols = int(input("Number of columns for matrix A:"))
print("Input elements for matrix A:")
MatrixA = MatrixInput(Arows, Acols)
Brows = int(input("Number of rows for matrix B:"))
Bcols = int(input("Number of columns for matrix B:"))
print("Input elements for matrix A:")
MatrixB = MatrixInput(Brows, Bcols)
print("Matrix A:")
MatrixPrint(MatrixA)
print("Matrix B:")
MatrixPrint(MatrixB)
MatrixC = MatrixMul(MatrixA, MatrixB)
print("MatrixA * MatrixB = ")
MatrixPrint(MatrixC)
