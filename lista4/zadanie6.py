import numpy as np
a=np.array([[3.50,2.77,-0.76,1.80],
    [-1.80,2.68,3.44,-0.09],
    [0.27,5.07,6.90,1.61],
    [1.71,5.45,2.68,1.71]])

b=np.array([[7.31],[4.23],[13.85],[11.55]])
x=np.linalg.solve(a,b)
print("x = ")
print(x)
detA=np.linalg.det(a)
print("det[A] = "+str(detA))
Ax=np.dot(a,x)
print("Ax = ")
print(Ax)
