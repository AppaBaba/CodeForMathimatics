from numpy import linspace, sqrt
from pylab import plot, title, show, gca

# (x-h)^2 + (y-k)^2 = r^2
# (y-k)^2 = r^2 - (x-h)^2
# (y-k) = sqrt(r^2 - (x-h)^2)^2)
#  y = k + sqrt(r^2 - (x-h)^2)^2)

# radius
r = 2
# center
h = 1
k = 2

x = linspace(-9, 9, 1000)
y = sqrt(r**2 - (x-h)**2)
plot(x, k + y,'b')
plot(x, k - y,'b')
gca().set_aspect('equal')
title("Standard Equation for a Circle")
show()
