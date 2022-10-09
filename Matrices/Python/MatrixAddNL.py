# Program MatrixAddNL
# Add two matrices
# using nested loop

MatrixA = [[2,7,3],
           [4 ,5,6],
           [7 ,8,9]]

MatrixB = [[7,2,6],
           [5,4,3],
           [2,1,0]]

MatrixC = [[0,0,0],
           [0,0,0],
           [0,0,0]]

for row in range(len(MatrixA)):
   for col in range(len(MatrixA[0])):
       MatrixC[row][col] = MatrixA[row][col] + MatrixB[row][col]

for m in MatrixC:
   print(m)
