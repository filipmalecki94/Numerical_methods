import numpy as np
x=np.array([[1,1,1,1],
    [3,9,27,81],
    [5,25,125,625],
    [6,36,216,1296]])
b=np.array([[2],[4],[3],[-1]])
a=np.linalg.solve(x,b)

print("a_0 = [-1]")
for licznik in range(0,4):
    print("a_"+str(licznik+1)+" = "+str(a[licznik]))

def f(x):
	return -1.0+2.68333333*x-0.875*x*x+0.21666667*x*x*x-0.025*x*x*x*x

print(f(5))