from numpy import linspace, meshgrid
from pylab import figure, subplots, axhline, axvline, contour, title, show

# Standar Conic Hyperbola
# x^2/a^2 - y^2/b^2 = 1
# no offset

def axis():
    axhline(0, alpha=.2, c = 'c')
    axvline(0, alpha=.2, c = 'c')

def hahyperbola(a,b):
    htah = x**2/a**2 - y**2/b**2
    return htah

def vahyperbola(a,b):
    vtah = y**2/a**2 - x**2/b**2
    return vtah

def PlotHAHyperbola(a,b,c,t):
    axis()
    htah = hahyperbola(a,b)
    contour(x, y, htah, [1], colors=c)
    title(t)

def PlotVAHyperbola(a,b,c,t):
    axis()
    vtah = vahyperbola(a,b)
    contour(x, y, vtah, [1], colors=c)
    title(t)

x = linspace(-8, 8, 200)
y = linspace(-5, 5, 200)
x, y = meshgrid(x, y)



fig = figure()

ax = fig.add_subplot(2, 2, 1)

a = 2
b = 1
c = 'r'
t = 'Standar HT-Axis Hyperbola'
PlotHAHyperbola(a,b,c,t)

ax = fig.add_subplot(2, 2, 2)

a = 2
b = 3
c = 'g'
t = 'Standar HT-Axis Hyperbola'

PlotHAHyperbola(a,b,c,t)

ax = fig.add_subplot(2, 2, 3)

a = 2
b = 1
c = 'b'
t = 'Standar VT-Axis Hyperbola'
PlotVAHyperbola(a,b,c,t)

ax = fig.add_subplot(2, 2, 4)
a = 2
b = 4
c = 'm'
t = 'Standar VT-Axis Hyperbola'
PlotVAHyperbola(a,b,c,t)

show()
