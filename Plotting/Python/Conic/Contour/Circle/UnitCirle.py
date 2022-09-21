from numpy import linspace, meshgrid
from pylab import figure, subplots, axhline, axvline, contour, gca, title, show

# General Form of a Circle
# ax^2 + bxy + cy^2 + dx + ey + f = 0

# Standar Form of a Circle
# (x-h)^2 + (y-k)^2 = r^2

def axes():
    axhline(0, alpha=.2, c = 'c')
    axvline(0, alpha=.2, c = 'c')

# A Simple Unit Circle
def uCircle():
    uc = x**2 + y**2
    return uc

# Relocate Unit Circle
def rCircle(h,k):
    rc = (x - h)**2 + (y - k)**2
    return rc

# Standar form of a Circle
def sCircle(r,h,k):
    sc = (x - h)**2/r**2 + (y - k)**2/r**2
    return sc

xx=linspace(-4,4,100)
yy=linspace(-4,4,100)
[x,y]=meshgrid(xx,yy)


fig = figure()

ax = fig.add_subplot(2, 2, 1)
axes()
uc=uCircle()
contour(x,y,uc,[1])
gca().set_aspect('equal')
title("Simple Circle")

h = 1
k = 2
ax = fig.add_subplot(2, 2, 2)
axes()
rc=rCircle(h,k)
contour(x,y,rc,[1])
gca().set_aspect('equal')
title("Relocate Circle")

r = 2
h = 1
k = 1
ax = fig.add_subplot(2, 2, 3)
axes()
sc=sCircle(r,h,k)
contour(x,y,sc,[1])
gca().set_aspect('equal')
title("Standar Form Circle")

r = 2
h = -1
k = -1
ax = fig.add_subplot(2, 2, 4)
axes()
sc=sCircle(r,h,k)
contour(x,y,sc,[1])
gca().set_aspect('equal')
title("Standar Form Circle")

show()
