#CS 4710
#JJ Holbrook
#700514202
#ICP 3 Part A Question 2

'''
Write a program to compute the eigenvalues and right eigenvectors of a given square array given below:
[[ 3 -2]
[ 1 O]]
'''
import numpy as np
from scipy import linalg

a = np.array([[3, -2],[1, 0]])
print(a)
'''
print(linalg.eigvals(a))
print("Eigenvalues = ", real.linalg.eigvals(a))]
'''
# Compute and print the eigenvalues
eigenvalues = linalg.eigvals(a)
print("Eigenvalues without isolating real parts:", eigenvalues)

# Isolate the real parts of the eigenvalues
real_parts = np.real(eigenvalues)
print("Eigenvalues with real parts isolated:", real_parts)
