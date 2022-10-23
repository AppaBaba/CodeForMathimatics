from numpy import linspace, meshgrid
from pylab import figure, subplots, axhline, axvline, contour, title, show

# Standar Conic Hyperbola
# (x -h)^2/a^2 - (y -k)^2/b^2 = 1
# with offset (h,k)

def axis():
    axhline(0, alpha=.2, c = 'c')
    axvline(0, alpha=.2, c = 'c')

def hahyperbola(a,b,h,k):
    htah = (x - h)**2/a**2 - (y - k)**2/b**2
    return htah

def vahyperbola(a,b,h,k):
    vtah = (y - k)**2/a**2 - (x - h)**2/b**2
    return vtah

def PlotHAHyperbola(a,b,h,k,c,t):
    axis()
    htah = hahyperbola(a,b,h,k)
    contour(x, y, htah, [1], colors=c)
    title(t)

def PlotVAHyperbola(a,b,h,k,c,t):
    axis()
    vtah = vahyperbola(a,b,h,k)
    contour(x, y, vtah, [1], colors=c)
    title(t)

x = linspace(-8, 8, 200)
y = linspace(-5, 5, 200)
x, y = meshgrid(x, y)



fig = figure()

ax = fig.add_subplot(2, 2, 1)

a = 2
b = 1
h = 0
k = 0
c = 'r'
t = 'Offset HT-Axis Hyperbola'
PlotHAHyperbola(a,b,h,k,c,t)

ax = fig.add_subplot(2, 2, 2)

a = 2
b = 1
h = 2
k = 1
c = 'g'
t = 'Offset HT-Axis Hyperbola'

PlotHAHyperbola(a,b,h,k,c,t)

ax = fig.add_subplot(2, 2, 3)

a = 2
b = 1
h = 0
k = 0
c = 'b'
t = 'Offset VT-Axis Hyperbola'
PlotVAHyperbola(a,b,h,k,c,t)

ax = fig.add_subplot(2, 2, 4)
a = 2
b = 1
h = 2
k = 1
c = 'm'
t = 'Offset VT-Axis Hyperbola'
PlotVAHyperbola(a,b,h,k,c,t)

show()
