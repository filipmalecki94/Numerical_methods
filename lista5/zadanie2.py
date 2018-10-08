import numpy
import scipy

A = numpy.mat('[2 -1 0 0 0 0;-1 2 -1 0 0 0;0 -1 2 -1 0 0;0 0 -1 2 -1 0;0 0 0 -1 2 -1;0 0 0 0 -1 5]')
invA = numpy.linalg.inv(A)
print("A^-1=\n",invA)
print("No nie jest trójdiagonalna")