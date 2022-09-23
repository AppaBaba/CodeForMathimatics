# Add two matrices using nested loop

MatrixA = [[2,7,3],
           [4 ,5,6],
           [7 ,8,9]]

MatrixB = [[7,2,6],
           [5,4,3],
           [2,1,0]]

MatrixC = [[0,0,0],
           [0,0,0],
           [0,0,0]]

# iterate rows
for r in range(len(MatrixA)):
   # iterate columns
   for c in range(len(MatrixA[0])):
       MatrixC[r][c] = MatrixA[r][c] + MatrixB[r][c]

for x in MatrixC:
   print(x)
