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

def plotQuad(qe, c, t):
    plot(x,qe, c, t)
    title(t)
    
# min and max x
xl = -5
xr =  5

# Limits of x with 100 spaced numbers
x = linspace(xl,xr,100)

qe1=x**2 + x - 2
c1 = 'r'
t1 = 'x^2 + x - 2'
qe2=4*x**2 - 8*x - 16
c2 = 'g'
t2 = '4x^2 - 8x - 16'
qe3=2*x**2 + 4*x + 8
c3 = 'b'
t3 = '2x^2 + 4x + 8'
qe4=-4*x**2 + 8*x + 16
c4 = 'm'
t4 = '-4x^2 + 8x + 16'

# setting the axes at the centre
fig = figure()

# first function which is y =ax^2 + bx + c
ax = fig.add_subplot(2, 2, 1)
plotspec(ax)
plotQuad(qe1, c1, t1)


# second function which is y =ax^2 + bx + c
ax = fig.add_subplot(2, 2, 2)
plotspec(ax)
plotQuad(qe2, c2, t2)

# third function which is y =ax^2 + bx + c
ax = fig.add_subplot(2, 2, 3)
plotspec(ax)
plotQuad(qe3, c3, t3)

# forth function which is y =ax^2 + bx + c
ax = fig.add_subplot(2, 2, 4)
plotspec(ax)
plotQuad(qe4, c4, t4)

# show the plot
show()
