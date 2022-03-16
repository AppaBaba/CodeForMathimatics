from numpy import linspace
from pylab import figure, plot, title, show

# Standard Form
# y = ax^3 + bx^2 + cx + d

def plotspec(ax):
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

def SFPolynormial(a, b, c, d):
    y = a*x**3 +b*x**2 + c * x + d
    return y    

def SFPPlot(a, b, c, d, plotcolor, plotname):
    y = SFPolynormial(a, b, c, d)
    plot(x,y, plotcolor)
    title(plotname)

# coeffinients    
a = 9 
b = 6
c = 3
d = 10

# min and max x
xl = -5
xr =  5 

# Limits of x with 100 spaced number
x = linspace(xl,xr,100)

fig = figure()
ax = fig.add_subplot(1, 1, 1)
plotspec(ax)
SFPPlot(a, b, c, d, 'r', 'Standar Form Polynomial')
show()
