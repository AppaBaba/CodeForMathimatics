from numpy import linspace
from pylab import figure, subplots, axis, plot, title, show

# generl linear euation
# y = ax + b
# slope y-intercept equation
# y mx + b
# m is called the slope
# b is defined as the y-intercept
# y-intercept the point the line crosses Y-axis 

def plotspec(ax):
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

def Line(m, b):
    y = m * x + b
    return y

def LinePlot(m, b, c, t):
    y = Line(m, b)
    plot(x,y, c)
    title(t)

# min and max x
xl = -5
xr =  5

# Limits of x with 100 spaced number
x = linspace(xl,xr,100)


# setting the axes at the centre
fig = figure()

# first line function which is y = mx + b
ax = fig.add_subplot(2, 2, 1)
plotspec(ax)
m = 1
b = 0
c = 'r'
t = 'x = y'
LinePlot(m, b, c, t)

# second line function which is y = mx + b
ax = fig.add_subplot(2, 2, 2)
plotspec(ax)
m = 1
b = 2
c = 'g'
t = 'y = x + 2'
LinePlot(m, b, c, t)

# third line function which is y = mx + b
ax = fig.add_subplot(2, 2, 3)
plotspec(ax)
m = 3
b = -4
c = 'b'
t = 'y = 3x - 4'
LinePlot(m, b, c, t)

# forth line function which is y = mx + b
ax = fig.add_subplot(2, 2, 4)
plotspec(ax)
m = -1
b = -0
c = 'm'
t = 'y = -1 * x'
LinePlot(m, b, c, t)

# show the plot
show()
