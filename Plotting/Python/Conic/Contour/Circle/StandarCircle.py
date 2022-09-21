from numpy import linspace, meshgrid
from pylab import figure, subplots, axhline, axvline, contour, gca, title, show

# General Form of a Circle
# ax^2 + bxy + cy^2 + dx + ey + f = 0

# Standar Form of a Circle
# (x-h)^2 + (y-k)^2 = r^2

def axes():
    axhline(0, alpha=.2, c = 'c')
    axvline(0, alpha=.2, c = 'c')

# Standar form of a Circle
def sCircle(r,h,k):
    sc = (x - h)**2/r**2 + (y - k)**2/r**2
    return sc

def CirclePlot(r,h,k,c,t):
    axes()
    sc=sCircle(r,h,k)
    contour(x,y,sc,[1],colors = c)
    gca().set_aspect('equal')
    title(t)

xx=linspace(-4,4,100)
yy=linspace(-4,4,100)
[x,y]=meshgrid(xx,yy)


fig = figure()

ax = fig.add_subplot(2, 2, 1)
r = 1
h = 0
k = 0
c = 'r'
t = 'Unit Circle'
CirclePlot(r,h,k,c,t)

ax = fig.add_subplot(2, 2, 2)
r =1
h = 1
k = 2
c = 'g'
t = 'Unit Circle Relocate'
CirclePlot(r,h,k,c,t)

ax = fig.add_subplot(2, 2, 3)
r = 2
h = 1
k = 1
c = 'b'
t = 'Standar Form Circle'
CirclePlot(r,h,k,c,t)

ax = fig.add_subplot(2, 2, 4)
r = 2
h = -1 
k = -1
c = 'm'
t = 'Standar Form Circle'
CirclePlot(r,h,k,c,t)

show()
