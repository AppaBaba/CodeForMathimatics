from numpy import linspace, meshgrid
from pylab import figure, subplots, axhline, axvline, contour, title, show

# Standar Conic Ellipe
# (x -h)^2/a^2 + (y -k)^2/b^2 = 1

def axes():
    axhline(0, alpha=.2, c = 'c')
    axvline(0, alpha=.2, c = 'c')

def scircle(a,b,h,k):
    sc = (x - h)**2/a**2 + (y - k)**2/b**2
    return sc

def PlotCircle(a,b,h,k,c,t):
    sc = scircle(a,b,h,k)
    contour(x, y, sc, [1], colors=c)
    title(t)

def sellipe(a,b,h,k):
    se = (x - h)**2/a**2 + (y - k)**2/b**2
    return se

def PlotEllipe(a,b,h,k,c,t):
    se = sellipe(a,b,h,k)
    contour(x, y, se, [1], colors=c)
    title(t)

x = linspace(-8, 8, 200)
y = linspace(-5, 5, 200)
x, y = meshgrid(x, y)



fig = figure()

ax = fig.add_subplot(2, 2, 1)

a = 4
b = a
h = 0
k = 0
c = 'r'
t = 'Simple Circle'

axes()
PlotCircle(a,b,h,k,c,t)


ax = fig.add_subplot(2, 2, 2)

a = 4
b = a
h = 1
k = 1
c = 'g'
t = 'Standar Circle'

axes()
PlotCircle(a,b,h,k,c,t)

ax = fig.add_subplot(2, 2, 3)

a = 5
b = 3
h = 0
k = 0
c = 'b'
t = 'Simple Ellipe'

axes()
PlotEllipe(a,b,h,k,c,t)

ax = fig.add_subplot(2, 2, 4)

a = 5
b = 3
h = 2
k = 1
c = 'm'
t = 'Standar Ellipe'

axes()
PlotEllipe(a,b,h,k,c,t)


show()
