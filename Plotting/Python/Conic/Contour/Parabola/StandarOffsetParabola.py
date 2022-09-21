from numpy import linspace, meshgrid
from pylab import figure, subplots, axhline, axvline, contour, show

# Standar Parabola Form
# vertex not at the origin
#

def axis():
    axhline(0, alpha=.2, c = 'c')
    axvline(0, alpha=.2, c = 'c')

def xanoparabola(a, h, k):
    xanop = (y - k)**2 - 4*a*(x - h)
    return xanop

def yanoparabola(a, h, k):
    yanop = (x - h)**2 - 4*a*(y - k)
    return yanop

x = linspace(-8, 8, 200)
y = linspace(-5, 5, 200)
x, y = meshgrid(x, y)

fig = figure()

ax = fig.add_subplot(2, 2, 1)
a = .4
h = -1
k = 1
axis()
xanop = xanoparabola(a, h, k)
contour(x, y, xanop, [0], colors='r')

ax = fig.add_subplot(2, 2, 2)
a = .4
h = -1
k = -1
axis()
yanop = yanoparabola(a, h, k)
contour(x, y, yanop, [0], colors='g')

ax = fig.add_subplot(2, 2, 3)
a = -.4
h = 1
k = 1
axis()
xanop = xanoparabola(a, h, k)
contour(x, y, xanop, [0], colors='b')

ax = fig.add_subplot(2, 2, 4)
a = -.4
h = 1
k = 1
axis()
yanop = yanoparabola(a, h, k)
contour(x, y, yanop, [0], colors='m')

show()
