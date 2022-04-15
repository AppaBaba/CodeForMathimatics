from sympy import*

x = Symbol('x')
# Product Rule
# [f(x)g(x)]' = f'(x)g(x) + f(x)g'(x)
# or    [fg]' = f'g + fg'

# f(x) = exp(x) * cos(x)
fx = exp(x) * cos(x)
print('f(x) = exp(x) * cos(x)')
# f'(x) = f'(exp(x)g(cos(x) + f(exp)g'(cos(x)
print('d/dx exp(x) * cos(x) =', diff(fx))
