import numpy as np

# L = np.array([[1.,0.,0.],
# 			  [1.,1.,0.],
# 			  [1.,5./3.,1.]])

# U = np.array([[1.,2.,4.],
# 			  [0.,3.,21.],
# 			  [0.,0.,0.]])

L = np.array([[2.,0.,0.],
			  [-1.,1.,0.],
			  [1.,-3.,1.]])

U = np.array([[2.,-1.,1.],
			  [0.,1.,-3.],
			  [0.,0.,1.]])

A = np.dot(L,U)
detA = np.linalg.det(A)
print("A\n",A)
print("detA=",detA)