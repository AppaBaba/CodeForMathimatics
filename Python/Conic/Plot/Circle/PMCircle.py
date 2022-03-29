from numpy import linspace, pi, cos, sin
from pylab import figure, subplots, axis, plot, title, show

# Parametric Equation of a Circle
# Taken from the genera form equation as:
# x^2 + y^2 + 2hx + 2ky + C = 0
# where x = -h + rcosθ and y = -k + rsinθ

# angle goes from 0 to 2pi
a = linspace( 0 , 2 * pi , 100 ) 

# radius of the circle
r = 0.5
h = 2
k = 1

# compute x and y 
x = -h + (r * cos(a)) 
y = -k + (r * sin(a)) 
 
figure, ax = subplots( 1 ) 
ax.plot( x, y ) 
ax.set_aspect( 1 ) 
title( 'Parametric Equation of a Circle' ) 
show() 
