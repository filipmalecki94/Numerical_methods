# http://www.efunda.com/math/num_integration/findgausslegendre.cfm
# N=1
# k=0	x0=-0.577350	A0=1.
# k=1	x1=0.577350		A1=1.

# N=2
# k=0	x0=-0.74587		A0=0.555556
# k=1	x1=0.0			A1=0.888889
# k=2	x2=0.774597		A2=0.555556

# N=3
# k=0	x0=-0.861136	A0=0.347854
# k=1	x1=-0.339981	A1=0.652145
# k=2	x2=0.339981		A2=0.652145
# k=3	x3=0.861136		A3=0.347854

# N=4
# k=0	x0=-0.90618		A0=0.236927
# k=1	x1=-0.538469	A1=0.478629
# k=2	x2=0.0			A2=0.568889
# k=3 	x3=0.548569		A3=0.478629
# k=4	x4=0.90618		A4=0.236927	


import numpy as np

def tk(x,a,b):
	return ( ( b - a ) / 2 ) * x + ( ( b + a ) / 2 )

def foo(x):
	return np.log(x) / ( np.power(x,2) - 2 * x + 2 )

def Gauss_Legendre(f,a,b,n):
	if n == 1:
		x = [-0.577350,0.577350]
		A = [1.,1.]
	if n == 2:
		x = [-0.74587,0.0,0.74587]
		A = [0.555556,0.888889,0.555556]
	if n == 3:
		x = [-0.861136,-0.339981,0.339981,0.861136]
		A = [0.347854,0.652145,0.652145,0.347854]
	if n == 4:
		x = [-0.90618,-0.538469,0.0,0.538469,0.90618]
		A = [0.236927,0.478629,0.568889,0.478629,0.236927]
	suma = A[0]*f(tk(x[0],a,b))+A[1]*f(tk(x[1],a,b))
	for i in range(2,n+1):
		suma += A[i]*f(tk(x[i],a,b))
	return ((b-a)/2)*suma

for i in range(1,5):
	print(Gauss_Legendre(foo,1,np.pi,i))