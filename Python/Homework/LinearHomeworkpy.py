from matplotlib.pyplot import*
from numpy import linspace

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
fig = figure(figsize = (6,8))

# first line function which is y = mx + b
ax = fig.add_subplot(3, 2, 1)
plotspec(ax)
m = 1
b = 0
c = 'r'
t = 'y = x'
LinePlot(m, b, c, t)

# second line function which is y = mx + b
ax = fig.add_subplot(4, 2, 2)
plotspec(ax)
m = 1
b = 2
c = 'g'
t = 'y = x + 2'
LinePlot(m, b, c, t)

# third line function which is y = mx + b
ax = fig.add_subplot(4, 2, 3)
plotspec(ax)
m = 3
b = -4
c = 'b'
t = 'y = 3x - 4'
LinePlot(m, b, c, t)

# forth line function which is y = mx + b
ax = fig.add_subplot(4, 2, 4)
plotspec(ax)
m = -1
b = 0
c = 'm'
t = 'y = -x'
LinePlot(m, b, c, t)

# first line function which is y = mx + b
ax = fig.add_subplot(4, 2, 5)
plotspec(ax)
m = 4
b = 0
c = 'r'
t = 'y = 4x'
LinePlot(m, b, c, t)

# second line function which is y = mx + b
ax = fig.add_subplot(4, 2, 6)
plotspec(ax)
m = 4
b = 2
c = 'g'
t = 'y = 4x + 2'
LinePlot(m, b, c, t)

# third line function which is y = mx + b
ax = fig.add_subplot(4, 2, 7)
plotspec(ax)
m = 3
b = -4
c = 'b'
t = 'y = 3x - 4'
LinePlot(m, b, c, t)

# forth line function which is y = mx + b
ax = fig.add_subplot(4, 2, 8)
plotspec(ax)
m = -3
b = -1
c = 'm'
t = 'y = -3x - 1'
LinePlot(m, b, c, t)

suptitle('Linear Homework')

# show the plot
show()
