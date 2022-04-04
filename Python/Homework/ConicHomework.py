from numpy import linspace, meshgrid
from matplotlib.pyplot import*

# General Form of a Circle
# ax^2 + bxy + cy^2 + dx + ey + f = 0

def axis():
    axhline(0, alpha=.2, c = 'c')
    axvline(0, alpha=.2, c = 'c')

# Standar Form of a Circle
# (x-h)^2 + (y-k)^2 = r^2

def sCircle(r,h,k):
    sc = (x - h)**2/r**2 + (y - k)**2/r**2
    return sc

def CirclePlot(r,h,k,c,t):
    axis()
    sc=sCircle(r,h,k)
    contour(x,y,sc,[1],colors = c)
    gca().set_aspect('equal')
    title(t)
    
# Standar Conic Ellipe
# (x -h)^2/a^2 + (y -k)^2/b^2 = 1

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
    # gca().set_aspect('equal')
    title(t)

def PlotYAEllipe(a,b,h,k,c,t):
    axis()
    syae = syaellipe(a,b,h,k)
    contour(x, y, syae, [1], colors=c)
    # gca().set_aspect('equal')
    title(t)

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


def xanoparabola(a, h, k):
    xanop = (y - k)**2 - 4*a*(x - h)
    return xanop

def yanoparabola(a, h, k):
    yanop = (x - h)**2 - 4*a*(y - k)
    return yanop

def PlotXAParabola(a,h,k,c,t):
    axis()
    xanop = xanoparabola(a, h, k)
    contour(x, y, xanop, [0], colors = c)
    title(t)

def PlotYAParabola(a,h,k,c,t):
    axis()
    yanop = yanoparabola(a, h, k)
    contour(x, y, yanop, [0], colors = c)
    title(t)
    

x=linspace(-8,8,100)
y=linspace(-5,5,100)
[x,y]=meshgrid(x,y)


fig = figure(figsize = (6,8))

ax = fig.add_subplot(4, 2, 1)
r = 2
h = 1
k = 1
c = 'r'
t = 'Standar Form Circle'
CirclePlot(r,h,k,c,t)

ax = fig.add_subplot(4, 2, 2)
r = 2
h = -1 
k = -1
c = 'g'
t = 'Standar Form Circle'
CirclePlot(r,h,k,c,t)

ax = fig.add_subplot(4, 2, 3)
a = 5
b = 3
h = 2
k = 1
c = 'b'
t = 'Standar X-Axis Ellipe'
PlotXAEllipe(a,b,h,k,c,t)

ax = fig.add_subplot(4, 2, 4)
a = 4
b = 2
h = .5
k = .5
c = 'm'
t = 'Standar Y-Axis Ellipe'
PlotYAEllipe(a,b,h,k,c,t)

ax = fig.add_subplot(4, 2, 5)
a = 2
b = 1
h = 2
k = 1
c = 'r'
t = 'Offset HT-Axis Hyperbola'
PlotHAHyperbola(a,b,h,k,c,t)

ax = fig.add_subplot(4, 2, 6)
a = 2
b = 1
h = 2
k = 1
c = 'g'
t = 'Offset VT-Axis Hyperbola'
PlotVAHyperbola(a,b,h,k,c,t)

ax = fig.add_subplot(4, 2, 7)
a = .4
h = -1
k = 1
c = 'b'
t = 'X-Axis Parabola'
PlotXAParabola(a, h, k, c, t)


ax = fig.add_subplot(4, 2, 8)
a = .4
h = -1
k = -1
c = 'm'
t = 'Y-Axis Parabola'
PlotYAParabola(a, h, k, c, t)

suptitle('Conic Section Homework')

show()
