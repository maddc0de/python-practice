# import the matplotlib library
import matplotlib.pyplot as plt

# the first input feature for each data point
x = [4, 5, 10, 4, 3, 11, 14 , 8, 10, 12]

# the second input feature for each data point
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

# functions that belong to a library can be accessed by using library.function
# create a scatter plot using matlibplot which the two features on the axis
plt.scatter(x, y)

# show the scatter plot
plt.show()