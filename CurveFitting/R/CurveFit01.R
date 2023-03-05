# Preparing the data
# Linear Function
p = function(x) x*2
# Random Generator
x = seq(1, 10, by = 1)
y = p(x) + runif(10)*3
# Create the data frame.
df = data.frame(x = x, y = y)
head(df)
# Fitting the model and prediction
linear <- lm(y~x, data=df)
#create a scatterplot of x vs. y
plot(df$x, df$y, pch=19,main = 'Linear Curve Fitting', 
     xlab='x', 
     ylab='y', 
     col = 'cyan')

x_axis <- seq(1, 10, length=10)
lines(x_axis, predict(linear, data.frame(x=x_axis)), col='red')
