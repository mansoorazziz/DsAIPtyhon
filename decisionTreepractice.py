import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# load the iris dataset
iris = load_iris()
# titanic_data = titanic.load_titanic()

# show dimensions of the dataset
print(f"Dataset shape: {iris.data.shape}")
# print(f"Titanic dataset shape: {titanic_data.data.shape}")

x = iris.data
y = iris.target

feature_names = iris.feature_names
target_names = iris.target_names
# split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42, stratify=y)

# create a decision tree classifier
model = DecisionTreeClassifier(max_depth=3, criterion='entropy', random_state=42)
# fit the model to the training data
model.fit(x_train, y_train)


# visualize the decision tree
plt.figure(figsize=(12, 8))
plot_tree(model, feature_names=feature_names, class_names=target_names, filled=True,rounded=True)
plt.title("Decision Tree Visualization")
plt.tight_layout()
plt.show()

# make predictions on the test set
y_pred = model.predict(x_test)
# evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.3f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")  
print(confusion_matrix(y_test, y_pred))


