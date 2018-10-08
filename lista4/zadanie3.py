import numpy as np

L = np.array([[1.,0.,0.],
			  [3./2.,1.,0.],
			  [1./2.,11./13.,1.]])

U = np.array([[2.,-3.,-1.],
			  [0.,13./2.,-7./2.],
			  [0.,0.,32./13.]])

b = np.array([[1.],
			  [-1.],
			  [2.]])

y = np.linalg.solve(L,b)
x = np.linalg.solve(U,y)

print("x=\n",x)