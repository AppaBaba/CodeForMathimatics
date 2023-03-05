# Preparing the data
# nonLinear Function qubic
p = function(x) x^3
# Random Generator
x = seq(1, 10, by = 1)
y = p(x) + runif(10)*50
# Create the data frame.
df = data.frame(x = x, y = y)
head(df)

# Fitting the model and prediction
qubic <- lm(y~poly(x,3,raw=TRUE), data=df)
#create a scatterplot of x vs. y
plot(df$x, df$y, pch=19, main = 'Qubic Curve Fitting',
     xlab='x', ylab='y', col = 'red')

x_axis <- seq(1, 10, length=10)
lines(x_axis, predict(qubic, data.frame(x=x_axis)), col='purple')

