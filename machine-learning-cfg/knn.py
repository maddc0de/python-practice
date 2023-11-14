import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier


x = [4, 5, 10, 4, 3, 11, 14 , 8, 10, 12]

y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

# classification for each data point
classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]

# create a scatter plot using matlibplot which the two features on the axis and the colour representing the class
plt.scatter(x, y, c=classes)

# zip the data so that the data points are set as pairs
data = list(zip(x, y))

# instantiate the model
knn = KNeighborsClassifier(n_neighbors=5)

# fit the model with the data
# this means passing the data with correct class labels into the model
knn.fit(data, classes)

# create a new data point
new_x = 8
new_y = 21
new_point = [(new_x, new_y)]

# ask the model to make a prediction for the class of the new datapoint
prediction = knn.predict(new_point)

# add the new point with its class onto the previously generated 
# append new_x to  x, new_y to y, and prediction to classes
plt.scatter(x + [new_x], y + [new_y], c=classes + [prediction[0]])
plt.text(x=new_x-1.7, y=new_y-0.7, s=f"New point! Class: {prediction[0]}")
plt.show()