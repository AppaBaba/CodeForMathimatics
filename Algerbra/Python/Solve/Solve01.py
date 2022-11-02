from sympy import symbols, Eq, solve

# Is there a suloution for this system of equations?
# x + y = 8
# x - y = 8

x, y = symbols("x y")
eq1 = Eq((x + y), 8)
eq2 = Eq((x - y), 8)
print("Equation 1:", eq1)
print("Equation 2:", eq2)
sol = solve((eq1, eq2), (x, y))
print("Solution:", sol)
