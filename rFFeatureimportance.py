import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier

# Load the Breast Cancer dataset
cancer = load_breast_cancer()
X = cancer.data
y = cancer.target

# Create a Random Forest classifier with OOB scoring enabled
rf_classifier = RandomForestClassifier(n_estimators=100, oob_score=True, random_state=42)
rf_classifier.fit(X, y)

# Get the OOB accuracy estimate
oob_accuracy = rf_classifier.oob_score_
print(f"OOB Accuracy Estimate: {oob_accuracy:.4f}")