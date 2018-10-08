import numpy as np

A = np.array([[1.,2.,3.],
			  [2.,3.,4.],
			  [3.,4.,5.]])

A = np.array([[2.11,-0.80,1.72],
			 [-1.84,3.03,1.29],
			 [-1.57,5.25,4.30]])

A = np.array([[2.,-1.,0.],
			  [-1.,2.,-1.],
			  [0.,-1.,2.]])

# A = np.array([[4.,3.,-1.],
# 			  [7.,-2.,3.],
# 			  [5.,-18.,13.]])

invA = np.linalg.inv(A)
detA = np.linalg.det(A)
print("A\n",A)
print("detA=",detA)
print("invA\n",invA)

normA = np.linalg.norm(A,2)
normInvA= np.linalg.norm(invA,2)

print("norm A= ",normA)
print("norm invA= ",normInvA)

print("K=",normA * normInvA)

if detA == 0:
	print("Macierz osobliwa")
else:
	print("Macierz nieosobliwa")

if normA * normInvA > 10:
	print("Macierz źle uwarunkowana")
else:
	print("Macierz dobrze uwarunkowana")