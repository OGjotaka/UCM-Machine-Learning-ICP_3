#CS 4710
#JJ Holbrook
#700514202
#ICP 3 Part A Question 3

'''
Compute the sum of the diagonal element of a given array
[[O 1 2]
[3 4 5]]
'''
import numpy as np

def main():
    a = np.array([[0,1, 2],[3, 4, 5]])
    print(a)
    print(calc_diag_sum(a))

def calc_diag_sum(my_array):
    diagonal_sum_list = []
    num_rows = my_array.shape[0]
    num_columns = my_array.shape[1]
    for i in range(num_rows):
        row_number = i
        for j in range(num_columns):
            column_number = j
            if row_number == column_number:
                diagonal_sum_list.append(my_array[i, j])
    diag_sum = sum(diagonal_sum_list)
    return diag_sum

main()

