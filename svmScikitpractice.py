import numpy as np
from sklearn.svm import SVC
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score , confusion_matrix

# Load the breast cancer dataset
data = load_breast_cancer()
X = data.data
y = data.target
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42,stratify=y)

# Models dictionary to store different SVM models
models = {
    'Linear SVM': SVC(kernel='linear', random_state=42),
    'Polynomial SVM': SVC(kernel='poly', degree=3, random_state=42),
    'RBF SVM': SVC(kernel='rbf', random_state=42)
}
results = {}
for name, model in models.items():
    # Train the model
    model.fit(X_train, y_train)
    # Make predictions on the test set
    y_pred = model.predict(X_test)
    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    results[name] = {
        'accuracy': accuracy,
        'confusion_matrix': conf_matrix
    }
# Print results for each model
for name, metrics in results.items():
    print(f"\n{name}:")
    print(f"Accuracy: {metrics['accuracy']:.2f}")
    print("Confusion Matrix:")
    print(metrics['confusion_matrix'])
