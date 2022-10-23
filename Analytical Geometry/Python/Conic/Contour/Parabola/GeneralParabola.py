from numpy import linspace, meshgrid
from pylab import figure, subplots, axhline, axvline, contour, title, show

# General equation of a parabola
# y=ax^2 + bx + c
# vertex equation of a parabola
# y=a(x-h)^2 + k


def axis():
    axhline(0, alpha=.2, c = 'c')
    axvline(0, alpha=.2, c = 'c')

def pyparabola(a,b,c):
    py = -y + a*x**2 + b*x + c
    return py

def PlotYAParabola(a,b,c,s,t):
    axis()
    YAP = pyparabola(a,b,c)
    contour(x, y, YAP, [0], colors = s)
    title(t)
    
def pxparabola(a,b,c):
    px = -x + a*y**2 + b*y + c
    return px

def PlotXAParabola(a,b,c,s,t):
    axis()
    XAP = pxparabola(a,b,c)
    contour(x, y, XAP, [0], colors = s)
    title(t)

x = linspace(-5, 5, 200)
y = linspace(-5, 5, 200)
x, y = meshgrid(x, y)

fig = figure()

ax = fig.add_subplot(2, 2, 1)

a = 1
b = -2
c = -3
s = 'r'
t = 'Standar Y-Axis Parabola'
PlotYAParabola(a,b,c,s,t)

ax = fig.add_subplot(2, 2, 2)

a = 1
b = -2
c = -2
s = 'g'
t = 'Standar X-Axis Parabola'
PlotXAParabola(a,b,c,s,t)

ax = fig.add_subplot(2, 2, 3)

a = -2
b = 3
c = 2
s = 'b'
t = 'Standar Y-Axis Parabola'
PlotYAParabola(a,b,c,s,t)

ax = fig.add_subplot(2, 2, 4)
a = -2
b = 3
c = 2
s = 'm'
t = 'Standar X-Axis parabola'
PlotXAParabola(a,b,c,s,t)

show()
