import numpy as np

x=np.array([[1,1,1],
		   [3,9,27],
		   [4,16,64]])
b=np.array([[25],[21],[-8]])
a=np.linalg.solve(x,b)

print("a_0 = [10]")
for licznik in range(0,3):
    print("a_"+str(licznik+1)+" = "+str(a[licznik]))

def f(x):
	return 10.0+34*x-9*x*x+0.*x*x*x

print(f(4.))