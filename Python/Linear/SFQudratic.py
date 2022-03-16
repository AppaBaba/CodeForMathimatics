from numpy import linspace
from pylab import figure, subplots, axis, plot, title, show

# Standard Form
# y = ax^2 + bx + c
# 
# 
# 

def plotspec(ax):
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

def SFQudratic(a, b, c):
    y = a * x ** 2 + b * x + c
    return y

def SFQPlot(a, b, c, plotcolor, plotname):
    y = SFQudratic(a, b, c)
    plot(x,y, plotcolor)
    title(plotname)

# min and max x
xl = -5
xr =  5

# Limits of x with 100 spaced numbers
x = linspace(xl,xr,100)


# setting the axes at the centre
fig = figure()

# first function which is y =ax^2 + bx + c
ax = fig.add_subplot(2, 2, 1)
plotspec(ax)
a = 1
b = 1
c = -2
pc = 'r'
pn = 'y = x^2 + x - 2'
SFQPlot(a, b, c, pc, pn)

# second function which is y =ax^2 + bx + c
ax = fig.add_subplot(2, 2, 2)
plotspec(ax)
a = 4
b = 8
c = -16
pc = 'g'
pn = 'y = 4x^2 +8x - 16'
SFQPlot(a, b, c, pc, pn)

# third function which is y =ax^2 + bx + c
ax = fig.add_subplot(2, 2, 3)
plotspec(ax)
a = 2
b = 4
c = 8
pc = 'b'
pn = 'y = 2x^2 + 4x - 4'
SFQPlot(a, b, c, pc, pn)

# forth function which is y =ax^2 + bx + c
ax = fig.add_subplot(2, 2, 4)
plotspec(ax)
a = -4
b = 8
c =  16
pc = 'm'
pn = 'y = -4x^2 + 8 * x + 16'
SFQPlot(a, b, c, pc, pn)

# show the plot
show()
