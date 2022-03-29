from numpy import linspace, meshgrid
from pylab import figure, subplots, axhline, axvline, contour, show

def axis():
    axhline(0, alpha=.2, c = 'c')
    axvline(0, alpha=.2, c = 'c')

def scircle(a,b,h,k):
    sc = (x - h)**2/a**2 + (y - k)**2/b**2
    return sc

def sellipe(a,b,h,k):
    se = (x - h)**2/a**2 + (y - k)**2/b**2
    return se

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
contour(x, y, xap, [0], colors='b')

ax = fig.add_subplot(2, 2, 2)

a = .4
axis()
yap = yaparabola(a)
contour(x, y, yap, [0], colors='b')

ax = fig.add_subplot(2, 2, 3)

a = -.4
axis()
xap = xaparabola(a)
contour(x, y, xap, [0], colors='b')

ax = fig.add_subplot(2, 2, 4)
a = -.4
axis()
yap = yaparabola(a)
contour(x, y, yap, [0], colors='b')

show()
