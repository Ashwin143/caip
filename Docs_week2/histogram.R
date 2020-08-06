# Create data for the graph.
v <-  c(9,13,21,8,36,22,12,41,31,33,19)
hist(v)

# Create the histogram.
hist(v,xlab = "Range",col = "yellow",border = "blue")


# Create data for the graph.
v <- c(9,13,21,8,36,22,12,41,31,33,19)

# Create the histogram.
hist(v,xlab = "Range",col = "green",border = "red", xlim = c(0,40), ylim = c(0,5))
?hist

# Save the file.
dev.off()