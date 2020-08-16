#1a
x <- dbinom(40,60,0.65)
x

#1b

x <- (1-pbinom(40,60,0.65))
x

#2b

x <- pbinom(19,60,0.5)
x

#2a

x1 <- dbinom(20,60,0.5)
x1

x2<- dbinom(25,60,0.5)
x2

x3 <- dbinom(30,60,0.5)
x3
t<- (x1+x2+x3)
t
#2c


x <- pbinom(30,60,prob=0.5)-pbinom(20,60,prob=0.5)
x


#3

x <- dpois(5, lambda=100)
x
x <- dpois(3, lambda=100)
x

#4

x<- rpois(2608, lambda=(10097/2608))
x
hist(x,main="The emission of alpha particles by polonium ")

#5a

z<-ppois(4,7)
z

#5b
z<-(1-ppois(10,7))
z

#5c

ppois(16,7)-ppois(3,7)
