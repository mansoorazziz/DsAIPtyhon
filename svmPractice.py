import numpy as np
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn import datasets

# Load the iris dataset

x,y = datasets.make_blobs(n_samples=100, centers=2, random_state=42, cluster_std=1.1)
# Create an SVM model
model = SVC(kernel='linear', C=10)
# Fit the model to the data
model.fit(x, y)

# Get the coefficients of the decision boundary
w = model.coef_[0]
b = model.intercept_[0]
#
# function to calculate the decision boundary
def decision_boundary(x):
    return (-w[0] * x - b) / w[1]
# create a range of x values for plotting
x_range = np.linspace(min(x[:, 0]) - 1, max(x[:, 0]) + 1, 100)
print(x_range)
