from sympy import Symbol, expand, simplify, Eq, solve

# Define symbolic variables
x = Symbol('x')
y = Symbol('y')

# Algebraic Expressions
ex1 = x**3 + x*y - x**2 - 2*y + y**3
ex2 = (x + y) * (x - y)
ex3 = (x**2 - y**2)/(x + y)

# Evaluate
ev1 = ex1.subs({x:2, y:1})
ev2 = ex1.subs({x:1, y:2})
print('Expression 1:', ex1)
print('Evaluate for (2,1):',ev1)
print('Evaluate for (1,2):',ev2)

# Exspand
print('Expression 2:',ex2)
exp = expand(ex2)
print('Expanstion :', exp)

# Simplify
print('Expression 3:', ex3)
simp = simplify(ex3)
print('Simplify:', simp)

# Is there a suloution for this system of equations?
# x + y = 8
# x - y = 8

eq1 = Eq((x + y), 8)
eq2 = Eq((x - y), 8)
print("Equation 1:", eq1)
print("Equation 2:", eq2)
sol = solve((eq1, eq2), (x, y))
print("Solution:", sol)
