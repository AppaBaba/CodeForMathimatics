from sympy import*

x = Symbol('x')
# Power Rule
# f'(x^n) = nx^(n-1)
# f(x) = x^3
fx = x**3
print ('f(x) = x^3')
# f'(x) = 3x^(3-1) = 3x^2
print('d/dx 3x^3 =', diff(fx))
