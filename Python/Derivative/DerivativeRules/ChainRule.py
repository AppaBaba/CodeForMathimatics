from sympy import*

x = Symbol('x')
#Chain Rule
# cos(x^2) is a composite
# let f(x) = cos(x) and g(x) = x^2
# then cos(x^2) = f(g(x))
fx = cos(x**2)
print('f(x) = cos(x^2)')
# d/dx[f(g(x)) = f'(g(x))g'(x)
print('d/dx cos(x^2) =', diff(fx))
