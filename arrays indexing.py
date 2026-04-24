# Indexing and Slicing in NumPy arrays
import  numpy as np


# Creating a 2D array and accessing its elements using indexing
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a[0,0]) # 1
print(a[1,2]) # 6

# Using negative indexing to access elements from the end of the array
print(a[-1, -2]) # 8
print(a[-3,-1]) # 3

# Slicing a 2D array to extract a subarray 0:2 means from index 0 to index 1 (not including index 2)
print(a[0:2, 0:2]) # [[1 2]
                            #  [4 5]]
print(a[::2, ::2]) # [[1 3]
                            #  [7 9]]

# Using slicing to extract a specific row or column 
slicearr = a[0,:2] # [[1 2]
print(slicearr)

rng = np.random.default_rng(42) # Create a random number generator with a specific seed for reproducibility
flips = rng.integers(0, 2, size=1000) # Create a 1000-element array of random integers (0 or 1)
print(np.sum(flips)) # Count the number of heads (1s) in the array

