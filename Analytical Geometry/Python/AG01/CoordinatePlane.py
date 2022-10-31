from numpy import linspace
from pylab import figure, subplots, axis, plot, text, show

x = linspace(-5,5,100)
fig = figure()
ax = fig.add_subplot()
ax.set_title('Coordinate Plane')

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.set_xlim(-5,5)
ax.set_ylim(-5,5)

ax.set_xticks(linspace(-5,5,11))
ax.set_yticks(linspace(-5,5,11))
ax.set_aspect('equal')
ax.grid(True,ls=':')
text(1.3,2.5,'Quardrant I')
text(-3.7,2.5,'Quardrant II')
text(-3.7,-2.5,'Quardrant III')
text(1.3,-2.5,'Quardrant IV')
plot()
show()
