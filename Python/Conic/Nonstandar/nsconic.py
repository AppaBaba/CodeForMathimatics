from numpy import linspace, meshgrid
from pylab import figure, subplots, axhline, axvline, contour,title, show

def conictype(a,b,c):
    if b**2 - 4*a*c < 0 & a == c :
        ct = 'circle'
    elif b**2 - 4*a*c < 0 & a != c :
        ct = 'Non Standard Ellipe'
    elif b**2 - 4*a*c == 0 :
        ct = 'Non Standard parabola'
    elif b**2 - 4*a*c > 0 :
        ct = 'Non Standard hyperbola'
    else:
        ct = 'no conic section'
    return ct

def axes():
    axhline(0, alpha=.2, c = 'c')
    axvline(0, alpha=.2, c = 'c')

def nsconic(a,b,c,d,e,f):
    cs = a*x**2 + b*x*y + c*y**2 + d*x + e*y + f
    return cs

def PlotNSConic(a,b,c,d,e,f,s):
    axes()
    ct = conictype(a,b,c)
    cs = nsconic(a,b,c,d,e,f)
    contour(x, y, cs, [0], colors = s)
    title(ct)
    

x = linspace(-9, 9, 200)
y = linspace(-5, 5, 200)
x, y = meshgrid(x, y)

fig = figure()

ax = fig.add_subplot(2, 2, 1)

a = 2
b = -3
c = 2
d = 6
e = -5
f = -5
s = 'r'

PlotNSConic(a,b,c,d,e,f,s)

ax = fig.add_subplot(2, 2, 2)

a = 1
b = -2
c = 1
d = 3
e = 3
f = -9
s = 'g'

PlotNSConic(a,b,c,d,e,f,s)

ax = fig.add_subplot(2, 2, 3)

a = 1
b = -3
c = 1
d = 1
e = 1
f = 2

PlotNSConic(a,b,c,d,e,f,s)

show()
