import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier

# Load the Breast Cancer dataset
cancer = load_breast_cancer()
X = cancer.data
y = cancer.target
feature_names = cancer.feature_names
target_names = cancer.target_names
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42,stratify=y)
# Train a Decision Tree Classifier
dt_classifier = RandomForestClassifier(n_estimators=100, random_state=42,bootstrap=True,n_jobs=-1,max_depth=None,criterion='entropy')
dt_classifier.fit(X_train, y_train)
# predict with Decision Tree Classifier
y_pred_dt = dt_classifier.predict(X_test)
# classification report for Decision Tree Classifier
print("Decision Tree Classifier Report:")
print(classification_report(y_test, y_pred_dt, target_names=target_names))
# confusion matrix for Decision Tree Classifier
print("Decision Tree Classifier Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_dt))

