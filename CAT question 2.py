#data extracted from histogram
data = [2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 9, 10, 12, 14]
 #mean
mean = sum(data) / len(data)
print("Mean =", sum(data), "÷", len(data), "=", mean)
 #median 
median = sorted(data)[len(data) // 2]
print("Median =", median)
 #mode 
mode = max(set(data))
print("Mode =", mode)
 #variance (sample variance)
variance = sum((x-mean)**2 for x in data ) / (len(data) - 1)
print("Variance =", variance)
 #standard deviation (sample standard deviation)
standard_deviation = variance**0.5
print("Standard Deviation =", standard_deviation)
#2
#In sample we divide by n-1 for variance, in population we divide by N.
# also The symbols for mean, variance, and standard deviation change
#3
# this sample is positively skewed because the mean is greater than the median.
# most data is to the left of the median. values 2-5 are more common than others
# effect on measure 
# Mean is pulled toward the outliers 12, 14,(makes it higher)
# Median is more resistant to outliers, (stays central)
# Mode reflects the most common values (the peak at 3)