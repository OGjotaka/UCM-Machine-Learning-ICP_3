#CS 4710
#JJ Holbrook
#700514202
#ICP 3 Part A Question 1

'''
Using NumPy create random vector of size 15 having only Integers in the range 1-20.
1.	Reshape the array to 3 by 5
2.	Print array shape.
3.	Replace the max in each row by 0
Create a 2-dimensional array of size 4 x 3 (composed of 4-byte integer elements), also print the shape, type and data type of the array.
'''

import numpy as np

# Generate a random vector of size 15 with integers in the range 1-20
a = np.random.randint(1, 21, size=15)
print(a)
print(a.shape)

# Reshape the array to 3x5 no order
reshaped_array = a.reshape(3, 5)
print(reshaped_array)
print(reshaped_array.shape)
'''
# Reshape the array to 3x5 C order
order_C_reshape = a.reshape((3, 5), order='C')
print("C Reshape: \n", order_C_reshape)

# Reshape the array to 3x5 F order
order_F_reshape = a.reshape((3, 5), order='F')
print("F Reshape: \n", order_F_reshape)

# Reshape the array to 3x5 A order
order_A_reshape = a.reshape((3, 5), order='A')
print("A Reshape: \n", order_A_reshape)
'''
# Get the number of rows in the array
num_rows = reshaped_array.shape[0]

# Iterate over the rows of the array using a loop
for i in range(num_rows):
    row_i = reshaped_array[i]
    max_val = np.max(row_i)
    if max_val != 0:
        max_index = np.argmax(row_i)
        reshaped_array[i, max_index] = 0
    print("Row", i, ":", row_i)
