import numpy
import scipy

A = numpy.mat('[0 0 2 1 2;0 1 0 2 -1;1 2 0 -2 0;0 0 0 -1 1;0 1 -1 1 -1]')
b = numpy.mat('[1;1;-4;-2;-1]')
result = numpy.linalg.solve(A,b)

print(result)