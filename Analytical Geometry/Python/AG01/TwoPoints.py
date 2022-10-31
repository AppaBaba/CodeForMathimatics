from numpy import linspace
from pylab import figure, subplots, axis, plot, scatter, text, title, show

x = linspace(-5,5,100)
fig = figure()
ax = fig.add_subplot()
ax.set_title(' Two Points')
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
x1 = [p1[0], p2[0]]
y1 = [p1[1], p2[1]]
scatter(x1, y1)
text(p1[0]-0.8, p1[1]+0.25, p1)
text(p2[0]-0.8, p2[1]+0.25, p2)

text(1.3,1.1,' what is the Distance?' )
text(1.3,.6,' What is the Slope?' )
text(1.3,0.1,' What is the Mid-Point?' )

show()
