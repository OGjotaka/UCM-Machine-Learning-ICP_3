#CS 4710
#JJ Holbrook
#700514202
#ICP 3 Part A Question 4

'''
Write a NumPy program to create a new shape to an array without changing its data. Reshape 3x2:
[[l 2]
[3 4]
[5 6]]
Reshape 2x3:
[[l 2 3]
[4 5 6]]
'''
import numpy as np

# Original array
original_array = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])

# Reshape to 3x2
reshaped_3x2 = original_array.reshape(3, 2)
print("Reshaped to 3x2:")
print(reshaped_3x2)

# Reshape to 2x3
reshaped_2x3 = original_array.reshape(2, 3)
print("\nReshaped to 2x3:")
print(reshaped_2x3)

