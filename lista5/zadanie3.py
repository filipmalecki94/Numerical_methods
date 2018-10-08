import numpy

A = numpy.array([[1,3, -9, 6, 4],
				[2, -1, 6, 7, 1],
				[3, 2, -3, 15, 5],
				[8, -1, 1, 4, 2],
				[11, 1, -2, 18, 7]])
invA = numpy.linalg.inv(A)

print(invA)
print("no jakość jako tako")