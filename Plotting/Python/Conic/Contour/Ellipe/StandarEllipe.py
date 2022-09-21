from numpy import linspace, meshgrid
from pylab import figure, subplots, axhline, axvline, contour, title, show

# Standar Conic Ellipe
# (x -h)^2/a^2 + (y -k)^2/b^2 = 1

def axis():
    axhline(0, alpha=.2, c = 'c')
    axvline(0, alpha=.2, c = 'c')

def sxaellipe(a,b,h,k):
    sxae = (x - h)**2/a**2 + (y - k)**2/b**2
    return sxae

def syaellipe(a,b,h,k):
    syae = (x - h)**2/b**2 + (y - k)**2/a**2
    return syae

def PlotXAEllipe(a,b,h,k,c,t):
    axis()
    sxae = sxaellipe(a,b,h,k)
    contour(x, y, sxae, [1], colors=c)
    title(t)

def PlotYAEllipe(a,b,h,k,c,t):
    axis()
    syae = syaellipe(a,b,h,k)
    contour(x, y, syae, [1], colors=c)
    title(t)

x = linspace(-8, 8, 200)
y = linspace(-5, 5, 200)
x, y = meshgrid(x, y)



fig = figure()

ax = fig.add_subplot(2, 2, 1)

a = 5
b = 3
h = 0
k = 0
c = 'r'
t = 'Simple X-Axis Ellipe'
PlotXAEllipe(a,b,h,k,c,t)

ax = fig.add_subplot(2, 2, 2)

a = 5
b = 3
h = 2
k = 1
c = 'g'
t = 'Standar X-Axis Ellipe'

PlotXAEllipe(a,b,h,k,c,t)

ax = fig.add_subplot(2, 2, 3)

a = 5
b = 3
h = 0
k = 0
c = 'b'
t = 'Simple Y-Axis Ellipe'
PlotYAEllipe(a,b,h,k,c,t)

ax = fig.add_subplot(2, 2, 4)
a = 4
b = 2
h = .5
k = .5
c = 'm'
t = 'Standar Y-Axis Ellipe'
PlotYAEllipe(a,b,h,k,c,t)

show()
