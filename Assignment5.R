#1a
x<-c(2,3,5,7,8)
y<-c(14,20,32,42,44)
cor(x,y)
cor.test(x,y)


#1b
x<-c(2,3,5,7,8)
y<-c(14,20,32,42,44)
#cor(x,y)
z<-lm(y~x)
#1c
t<-data.frame(x=6)
predict(z,t)
plot(x,y,abline(lm(y~x)),xlab="age",ylab="weight")



#2a
x<-c(8,7,6,4,2,1)
y<-c(15,19,25,23,34,40)
z<-lm(x~y)
z
t<-data.frame(y=2)
predict(z,t)

plot(x,y,abline(lm(y~x)))

#2b

x<-c(8,7,6,4,2,1)
y<-c(15,19,25,23,34,40)
z<-lm(y~x)
z
t<-data.frame(x=5)
predict(z,t)

plot(x,y,abline(z))

#3

x<-c(6,4,8,5,3.5)
y<-c(6.5,4.5,7,5,4)
z<-lm(y~x)
z
t<-data.frame(x=7.5)
predict(z,t)
plot(x,y,abline(z))

#4

x<-c(186,189,190,192,193,193,198,201,203,205)
y<-c(85,85,86,90,87,91,93,103,100,101)

z<-lm(y~x)
z
t<-data.frame(x=208)
predict(z,t)
plot(x,y,abline(z))

#5
x<-c(6,7,8,9,10)
y<-c(4,3,3,2,1)

z<-lm(y~x)
z

t<-data.frame(x=8)
predict(z,t)
plot(x,y,abline(z))

#6a

x <- 1:6
sample(x, 3000, replace = TRUE)

#6b

runif(27, min=30, max=70)

#6c
0=tail
1=tails
x <- 0:1
sample(x, 1000, replace = TRUE)

#7a

x<-rnorm(100, mean=0, sd=30)
#hist(x)
m=mean(x)
s=sd(x)
y<-dnorm(x, m=0, s)
round(y,2)
plot(x,y)

#7b

z<-pnorm(x,mean=0,sd=s)
plot(x,z)

#7c

f<-qnorm(0.2,mean=0,sd=30)
f

#7d

q<-qnorm(0.5,mean=mean(x),sd=sd(x))
q

#8a

x<-rnorm(100, mean=0, sd=15)
#hist(x)
m=mean(x)
s=sd(x)
y<-dnorm(x, m=0, s)
round(y,2)
plot(x,y)


#8b

x<-rnorm(100, mean=0, sd=45)
#hist(x)
m=mean(x)
s=sd(x)
y<-dnorm(x, m, s)
round(y,2)
plot(x,y)

#8c

x<-rnorm(100, mean=50, sd=15)
#hist(x)
m=mean(x)
s=sd(x)
y<-dnorm(x, m, s)
round(y,2)
plot(x,y)

#8d

x<-rnorm(100, mean=-50, sd=15)
#hist(x)
m=mean(x)
s=sd(x)
y<-dnorm(x, m, s)
round(y,2)
plot(x,y)


#9

x<-rnorm(5000, mean=20, sd=5)
hist(x)

#10a

1-pnorm(29,22,5)

#10b

pnorm(17,22,5)

#10c

pnorm(15,22,5)+(1-pnorm(25,22,5))

#11a

mu=30
sigma=2
a<-1/(sqrt(2*pi)*sigma)*exp(-((31 - mu)^2/(2*sigma^2))) 
a

#11b

dnorm(31,30,2)


#12

d<-mtcars$mpg
mean(d)
median(d)
sd(d)
var(d)
range(d)





