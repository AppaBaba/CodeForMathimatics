from numpy import linspace
from matplotlib.pyplot import*

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

def Qudratic(a, b, c):
    y = a*x**2 + b*x + c
    return y

def QudraticPlot(a, b, c, plotcolor, plotname):
    y = Qudratic(a, b, c )
    plot(x,y, plotcolor, label = 'quadratic' )
    title(plotname)
    legend(loc = 2)
    xlim(-6,6)
    ylim(-60,60)

def Qubic(a, b, c, d):
    y = a*x**3 + b*x**2 + c*x + d
    return y

def QubicPlot(a, b, c, d, plotcolor, plotname):
    y = Qubic(a, b, c, d)
    plot(x,y, plotcolor, label = 'cubic')
    title(plotname)
    legend(loc = 2)
    xlim(-6.6)
    ylim(-30,30)

# min and max x
xl = -5
xr =  5

# Limits of x with 100 spaced numbers
x = linspace(xl,xr,100)

# setting the axes at the centre
fig = figure(figsize = (6,8))

# first function which is y =ax^2 + bx + c
ax = fig.add_subplot(4, 2, 1)
plotspec(ax)
a = 1
b = 1
c = -2
pc = 'r'
pn = 'y = x^2 + x - 2'
QudraticPlot(a, b, c, pc, pn)

# second function which is y =ax^2 + bx + c
ax = fig.add_subplot(4, 2, 2)
plotspec(ax)
a = 4
b = 8
c = -16
pc = 'g'
pn = 'y = 4x^2 +8x - 16'
QudraticPlot(a, b, c, pc, pn)

# third function which is y =ax^2 + bx + c
ax = fig.add_subplot(4, 2, 3)
plotspec(ax)
a = 2
b = 4
c = 8
pc = 'b'
pn = 'y = 2x^2 + 4x - 4'
QudraticPlot(a, b, c, pc, pn)

# forth function which is y =ax^2 + bx + c
ax = fig.add_subplot(4, 2, 4)
plotspec(ax)
a = -4
b = 8
c =  16
pc = 'm'
pn = 'y = -4x^2 + 8 * x + 16'
QudraticPlot(a, b, c, pc, pn)

ax = fig.add_subplot(4, 2, 5)
plotspec(ax)

# coeffinients    
a = 1
b = 0
c = 0
d = 3
pc = 'r'
pn = 'x^3 + 3'
QubicPlot(a, b, c, d, pc, pn)

ax = fig.add_subplot(4, 2, 6)
plotspec(ax)

# coeffinients    
a = -1 
b = 6
c = -12
d = 8
pc = 'g'
pn = '-x^3 + 6x^2 - 12x + 8'
QubicPlot(a, b, c, d, pc, pn)

ax = fig.add_subplot(4, 2, 7)
plotspec(ax)

# coeffinients    
a = 1
b = 3
c = 4
d = 4
pc = 'b'
pn = 'x^3 + 3x^2 + 4x + 4'
QubicPlot(a, b, c, d, pc, pn)

ax = fig.add_subplot(4, 2, 8)
plotspec(ax)

# coeffinients    
a = -9 
b = 6
c = -3
d = 10
pc = 'm'
pn = '-9x^3 + 6x^2 - 3x + 10'
QubicPlot(a, b, c, d, pc, pn)



suptitle('Nonlinear Polynormail Homework')

# show the plot
show()
