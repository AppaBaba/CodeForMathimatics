# Program MatrixMul
# multiply Matrix A and B
# using nested loops

MatrixA = [[1,2,3],
           [4 ,5,6],
           [7 ,8,9]]

MatrixB = [[5,6,7,8],
           [1,2,3,4],
           [9,1,2,3]]

MatrixC = [[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]

for Arow in range(len(MatrixA)):
   for Acol in range(len(MatrixA[0])):
       for Brow in range(len(MatrixB)):
           MatrixC[Arow][Acol] += MatrixA[Arow][Brow] * MatrixB[Brow][Acol]

for m in MatrixC:
   print(m)
