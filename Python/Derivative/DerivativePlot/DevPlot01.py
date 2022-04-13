from matplotlib.pyplot import plot, legend, grid, suptitle, show
from scipy.misc import derivative
from numpy import linspace

# f(x)
def f(x):
	return x**3
# d/dx 
def d(x):
	return derivative(f, x)

# x-axis
y = linspace(-4, 4)

# plot f(x)
plot(y, f(y), color='g', label='F(x)')
# plot d/dx
plot(y, d(y), color='m', label='d/dx')

# plot format
legend(loc='lower right')
grid(True)
suptitle('f(x) = x^3')
show()
