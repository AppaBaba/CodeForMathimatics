# Preparing the data
# nonLinear qudratic function 
p = function(x) x^2
# Random Generator
x = seq(1, 10, by = 1)
y = p(x) + runif(10)*15
# Create the data frame.
df = data.frame(x = x, y = y)
head(df)

# Fitting the model and prediction
fit2 <- lm(y~poly(x,2,raw=TRUE), data=df)
#create a scatterplot of x vs. y
plot(df$x, df$y, pch=19, 
     main = 'Qudratic Curve Fitting',
     xlab='x', ylab='y', col = 'magenta')

x_axis <- seq(1, 10, length=10)
lines(x_axis, predict(fit2, data.frame(x=x_axis)), col='blue')
