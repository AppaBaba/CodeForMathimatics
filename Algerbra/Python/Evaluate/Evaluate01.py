from sympy import *
x = Symbol('x')
expr = x
res = expr.subs({x:x-1})
print(res)
# x - 1
