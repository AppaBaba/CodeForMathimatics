from numpy import linspace, pi, sin, cos
from pylab import polar, yticks, title, show
 
theta = linspace(0, pi, 100)
r = sin(theta)
polar(theta, r)
# Change tick labels here
yticks([1, 2, 3], ["a", "b", "c"])
title('Polar Equation for a Circle')
show()
