from sympy import *
x = Symbol('x')
y = Symbol('y')
ex2 = (x + y) * (x - y)
print('Expression 2:', ex2)
exp = expand(ex2)
print('Expanstion :', exp)
