from numpy import linspace
from pylab import figure, subplots, axis, plot, scatter, text, show

x = linspace(-5,5,100)
fig = figure()
ax = fig.add_subplot()
ax.set_title('Points on a Coordinate Plane')
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

p1 = [1, 2]
p2 = [3, 4]
p3 = [3, 2]
      
x1 = [1, 3, 3, 4]
y1 = [2, 4, 2, 3]
scatter(x1, y1)
text(p1[0]-0.8, p1[1]+0.25, p1)
text(p2[0]-0.8, p2[1]+0.25, p2)

text(1.3,1.1,'Points plotted(x,y)')

show()
