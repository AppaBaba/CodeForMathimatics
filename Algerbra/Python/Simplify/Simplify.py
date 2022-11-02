from sympy import Symbol, simplify
x = Symbol('x')
y = Symbol('y')
ex3 = (x**2 - y**2)/(x + y)
print(ex3)
simp = simplify(ex3)
print(simp)
# x - y
