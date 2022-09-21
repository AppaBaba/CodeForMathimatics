# Add two matrices using list comprehension

Ma = [[2, 7, 3], [3, 2, 6], [5, 4, 0]]

Mb = [[7, 2, 6], [6, 7, 3], [4, 5, 9]]

Mc = [[Ma[r][c] + Mb[r][c] for c in range(len(Ma[0]))] for r in range(len(Ma))]

for x in Mc:
   print(x)
