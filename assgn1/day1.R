#1

paste("label", 1:30)

#2a

R <- c(2.27,1.98,1.69,1.88,1.64,2.14)
r<- R^2
H <- c(8.28,8.04,9.06,8.70,7.58,8.34)
vol<-1/3*r*h*3.14
vol

#2b

roundvol <- round(vol,digits=2)
roundvol
#2c

minvol<-min(roundvol)
minvol
maxvol<-max(roundvol)
maxvol


#3a

x<-round(runif(250,0,999),2)
x
#3b
y<-900
z <- which(x > y) 
x[z]
  
#3c
s<-sort(x[z], decreasing = FALSE)
s

#4a

w <- c(87,58,65,100)
g <- c(180,165,160,193)
f<- (g^2)/10000
f
bmi<-w/f
bmi

#4b

w1<-25
z <- which(bmi > w1) 

bmi[c(z)]

#4c

mb<-mean(bmi)
mb

#5

x<-round(runif(10,0,50),2)
x

#5a

p1<-mean(x)
p1

#5b
p2<-median(x)
p2

#6

category <- factor (c("a", "b", "c", "b", "c", "b", "a", "c", "c"))
summary(category) 

#7



mark<-list(10,12,13,14,15)
student<-list("ashwin","1","m",mark=mark)
names(student)<-c("name","rollno","gender","marklist")
student

#7a


mark<-list(10,12,13,14,15)
vector <- unlist(mark)
v<-mean(vector)
v

#7b

rollno<-list(1)

mark<-list(10,12,13,14,15)
student<-list("ashwin",rollno=rollno,"m",mark=mark)
names(student)<-c("name","rollno","gender","marklist")
student

#7c
mark<-list(10,12,13,14,15)
mark[5] <- 20
mark

#8

a<-rbind(c(1,1,3),c(5,2,6),c(-2,-1,-3))
a
a %*% a%*%a

#9

x <- c(10,-10,10)
b<-matrix(x, 15, 3,byrow=TRUE)
b


x <- c(10,-10,10)
b<-matrix(x, 3, 3,byrow=TRUE)
b
t(b)

calc<-b %*% t(b)
calc

#10

emp <- data.frame(
   Age = c (25,31,23), 
   Height = c(177,163,190),
   Weight = c(57,69,83), 
   Sex=c("F","F","M"))
row.names(emp) <- c("Alex","lilly","Mark")
emp

#11

emp1 <- data.frame(
    
   Working=c("Yes","No","No"))
row.names(emp) <- c("Alex","Lilly","Mark")
emp1

#adding column to dataframe
emp$Working<- c("Yes","No","No")
emp


#11a

emp <- data.frame(
   Age = c (25,31,23), 
   Height = c(177,163,190),
   Weight = c(57,69,83), 
   Sex=c("F","F","M"))
row.names(emp) <- c("Alex","lilly","Mark")
emp


lapply(emp, class)


#11b

mean(emp$Height)

#11c
emp <- data.frame(
   Age = c (25,31,23), 
   Height = c(177,163,190),
   Weight = c(57,69,83), 
   Sex=c("F","F","M"))
row.names(emp) <- c("Alex","lilly","Mark")

emp1 <- data.frame(
    
   Working=c("Yes","No","No"))
row.names(emp) <- c("Alex","Lilly","Mark")


#adding column to dataframe
emp$Working<- c("Yes","No","No")



z<-c(round(((emp$Weight)/(((emp$Height)/100)^2)),2))

emp$bmi<- z
emp

#12

array(1:20,c(2,3,3))

#13a


z<-data.frame(mpg=c(mtcars$mpg),cyl=c(mtcars$cyl),hp=c(mtcars$hp))
row.names(z)<-rownames(mtcars)
z

#13b

z<-data.frame(mpg=c(mtcars$mpg),cyl=c(mtcars$cyl),hp=c(mtcars$hp))
row.names(z)<-rownames(mtcars)


l<-rbind(head(z,5),tail(z,5))
l
