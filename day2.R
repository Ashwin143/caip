#1

#link:https://www.kaggle.com/rikdifos/credit-card-approval-prediction/data

#data <- read.csv("D:/ML/CAIP/creditcardpre.csv")
#head(data,6)

#2a

x <- c(7, 3, 4, 6)
labels <- c("Comedy", "Action", "Romance", "Science Fiction")
png(file = "movie.png")
pie(x)

#2b

x <- c(7, 3, 4, 6)
labels <- c("Comedy", "Action", "Romance", "Science Fiction")
png(file = "movie.png")
pie(x,main = "movie pie chart")

#2c

x <- c(7, 3, 4, 6)
labels <- c("Comedy", "Action", "Romance", "Science Fiction")
png(file = "movie.png")
pie(x,labels,main = "movie pie chart")

#3

x <- c(7, 3, 4, 6)
labels <- c("Comedy", "Action", "Romance", "Science Fiction")


png(file = "barchart_movie.png")

barplot(x,names.arg=labels,xlab="labels",ylab="Number",
main="movie bar chart")

#4

colors = c("green","orange","brown")
months <- c("Mar","Apr","May","Jun")
regions <- c("a","b","c")
Values <- matrix(c(7, 3, 4, 6), nrow = 3, ncol = 4, byrow = TRUE)
png(file = "barchart_stacked.png")
barplot(Values, main = "total revenue", names.arg = months, xlab = "quater", ylab = "sales", col = colors)
legend("topleft", regions, cex = 1.3, fill = colors)

#5

hist(mtcars$mpg, xlab=rownames(mtcars),ylab = "mpg",,main = "Motor Trend Car Road Tests")

#6a and #6b

plot.new()
plot.window(xlim=c(0,1), ylim=c(5,10))
abline(a=6, b=3)
axis(1)
axis(2)
title(main="The Overall Title")
title(xlab="An x-axis label")
title(ylab="A y-axis label")
box()

#6c
x <- c(1,2,3,4,5)
y <- c(2,3,4,5,6)
plot(x, y, type = "S")

b<-max(y)
abline(h=b)

#6d


#7
drugA <- c(16, 20, 27, 40, 60)
drugB<-c(15, 18, 25, 31, 40)

plot(v,type = "o",col = "red", main = "drug usage")
lines(t, type = "o", col = "blue")

