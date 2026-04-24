# This code demonstrates various ways to create and manipulate arrays using the NumPy library in Python. 
# It includes examples of creating one-dimensional and two-dimensional arrays, 
# as well as using functions to generate arrays filled with specific values or patterns. 
# Additionally, it shows how to specify data types and convert between them.

import  numpy as np
import  matplotlib.pyplot as plt


# One-dimensional array
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr[0])

# Two-dimensional array with 2 rows and 3 columns of zeros
print(np.zeros((2, 3)))

# Two-dimensional array with 2 rows and 3 columns of ones
print(np.ones((2, 3)))

# Two-dimensional array with 2 rows and 3 columns filled with the value 7
print(np.full((2, 3), 7))

# Array of integers from 0 to 9 with a step of 2
print(np.arange(0, 10, 2))

# Array of 5 evenly spaced numbers between 0 and 1
print(np.linspace(0, 1, 5)) 

# Identity matrix of size 3x3
print(np.eye(3))

# Diagonal matrix with the values 1, 2, and 3 on the diagonal
print(np.diag([1, 2, 3]))

# Array with data type float
print(np.array([1, 2, 3],dtype=float))

# Fetch Array with data type int
arr2 = np.array([1.5, 2.5, 3.5])
print(arr2.astype(int))
