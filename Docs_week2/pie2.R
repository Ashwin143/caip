# Create data for the graph.
  x <- c(21, 62, 10, 53)
  x
  pie(x)

labels <- c("London", "New York", "Singapore", "Mumbai")
labels
  pie(x, labels)

colors=c("red","green","blue","yellow")
colors
pie(x, labels, main = "City pie chart", col = colors)

# Add the legend to the chart.
legend("topleft", labels, cex = 1.0, fill = colors)

pie(x, labels, main = "City pie chart", col = rainbow(length(x)))

  dev.off()