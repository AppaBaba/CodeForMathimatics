from matplotlib.pyplot import subplot, plot, legend, grid, suptitle, show
from scipy.misc import derivative
from numpy import linspace

def plotspec(ax):
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')

# f(x)
def f(x):
	return x**5
# d/dx
def d(x):
	return derivative(f, x)

# x-axis
y = linspace(-10, 10)
ax = subplot(1,1,1)
plotspec(ax)
# plot f(x)
plot(y, f(y), color='g', label='f(x)')
# plot d/dx
plot(y, d(y), color='m', label='d/dx')

# plot format
legend(loc='lower right')
grid(True)
suptitle('f(x) = x^5')
show()
