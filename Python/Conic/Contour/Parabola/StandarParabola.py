from numpy import linspace, meshgrid
from pylab import figure, subplots, axhline, axvline, contour, show

# Standar Parabola Form
# vertex at the origin
#

def axis():
    axhline(0, alpha=.2, c = 'c')
    axvline(0, alpha=.2, c = 'c')

def xaparabola(a):
    xap = y**2 - 4*a*x
    return xap

def yaparabola(a):
    yap = x**2 - 4*a*y
    return yap

x = linspace(-8, 8, 200)
y = linspace(-5, 5, 200)
x, y = meshgrid(x, y)

fig = figure()

ax = fig.add_subplot(2, 2, 1)

a = .4
axis()
xap = xaparabola(a)
contour(x, y, xap, [0], colors='r')

ax = fig.add_subplot(2, 2, 2)

a = .4
axis()
yap = yaparabola(a)
contour(x, y, yap, [0], colors='g')

ax = fig.add_subplot(2, 2, 3)

a = -.4
axis()
xap = xaparabola(a)
contour(x, y, xap, [0], colors='b')

ax = fig.add_subplot(2, 2, 4)
a = -.4
axis()
yap = yaparabola(a)
contour(x, y, yap, [0], colors='m')

show()
