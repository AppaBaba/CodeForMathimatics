from matplotlib.pyplot import subplot, legend, plot, grid, suptitle, show
from numpy import arange
from scipy.misc import derivative

def plotspec(ax):
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')

def f(x):
    return x**2
def d(x):
    return derivative(f, x)

# x-axis
x = arange(-2.0, 2.0, 0.01)

ax = subplot(1,1,1)
plotspec(ax)

y = f(x)
# plot f(x)
plot(x, y, color='g', label='f(x)')

yp = derivative(f, x)
# plot d/dx
plot(x, d(x), color='m', label='d/dx')

legend(loc='lower right')
grid(True)
suptitle('f(x) = x^2')

show()
