import numpy
import scipy
import sympy
import fractions
import os
from scipy import linalg
A = numpy.array([[1., 1., 1., 1., 1.],
	[1., 1., 1., 1., 1.],
	[1., 1., 1., 1., 1.],
	[1., 1., 1., 1., 1.],
	[1., 1., 1., 1., 1.]])

b = numpy.mat('[5;4;3;2;1]')

for i in range(0,5):
	for j in range(0,5):
		A[i][j] = 1/(i+j+1)
Am = numpy.asmatrix(A)

#1
#x = numpy.linalg.solve(Am,b)
LU, P = linalg.lu_factor(Am)
x = linalg.lu_solve((LU,P),b)
#2
r=b-numpy.dot(Am,x)
print("A=\n",Am)
print("x=\n",x)
#print("deltax=\n",deltax)
print("r=",r)

print(numpy.linalg.norm(r,numpy.inf),numpy.linalg.norm(numpy.dot(Am,x),numpy.inf)*numpy.finfo(float).eps)	
count = 0
while numpy.linalg.norm(r,numpy.inf) <= numpy.linalg.norm(b,numpy.inf)*numpy.finfo(float).eps:
	deltax = numpy.linalg.solve(Am,r)
	x = x + deltax
	r = b-numpy.dot(Am,x)
	count +=1
	print("x=\n",x + deltax)
	print("deltax=\n",deltax)
	print("r=",r)
	print(numpy.linalg.norm(r,numpy.inf),numpy.linalg.norm(numpy.dot(Am,x),numpy.inf)*numpy.finfo(float).eps)
