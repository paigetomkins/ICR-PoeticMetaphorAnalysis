import numpy as np
#numpy is a common open-source library used for calculations in Python

from numpy.linalg import norm
#.linalg refers to the linear algebra module of numpy, while norm is a specific function within linalg that deals with vectors and matrices

A = np.array([[1,2,2,],[3,2,2], [-2,1,-3]])
B = np.array([[4,2,4],[2,-2,5],[3,4,-4]])
print("A:\n", A)
print("B:\n", B)

cosine = np.sum(A*B, axis=1)/(norm(A, axis=1)*norm(B, axis=1))
print("Cosine Similarity:\n", cosine)
print("Cosine Similarity:\n", cosine)










