
import numpy as np

learning_rate = 0.01
epochs = 10
x = np.array([1, 2, 3, 4, 5])
y = np.array([3,4,2,5,6])
m,b = 0.0, 0.0
n = len(x)

for epoch in range(epochs):
    y_pred = m*x + b
    cost = sum((y - y_pred) ** 2).mean()
    D_m = (-2/n) * sum(x * (y - y_pred))
    D_b = (-2/n) * sum(y - y_pred)
    m = m - learning_rate * D_m
    b = b - learning_rate * D_b
    print(f"Epoch {epoch+1}: m={m}, b={b}, cost={cost}")