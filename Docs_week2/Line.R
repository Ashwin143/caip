# Create the data for the chart.
x <- c(7,12,28,3,41)
plot(x)

y <- c(14,7,6,19,3)


plot(x,y)

# Plot the  chart. 
plot(v,type = "o")

# Create the data for the chart.
v <- c(7,12,28,3,41)
t <- c(14,7,6,19,3)


# Plot the bar chart.
plot(v,type = "o", col = "red", xlab = "Month", ylab = "Rain fall",
     main = "Rain fall chart")

# Plot the bar chart.
plot(v,type = "s", col = "red", xlab = "Month", ylab = "Rain fall",
     main = "Rain fall chart")




# Create the data for the chart.
v <- c(7,12,28,3,41)
t <- c(14,7,6,19,3)


# Plot the bar chart.
plot(v,type = "o",col = "red", xlab = "Month", ylab = "Rain fall", 
     main = "Rain fall chart")

lines(t, type = "o", col = "blue")

# Save the file.
dev.off()
?plot

