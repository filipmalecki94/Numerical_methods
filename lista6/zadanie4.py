import numpy as np
import scipy as sp
from scipy import linalg
from matplotlib import pyplot as plt

dimension = 20

def MakeNMatrix(N):
  temp = []
  tempRow = []
  diagonal = 0.025
  for i in range (0,N):
    for j in range(0,N):
      if j == i:
        tempRow.append(diagonal)
        diagonal += 0.025
      elif j >= i+1:
        tempRow.append(5)
      else:
        tempRow.append(0.)
    temp.append(tempRow)
    tempRow=[]
  return np.asarray(temp)

B = MakeNMatrix(dimension)

def MakeNB(N):
	temp = []
	tempRow = []
	for i in range(0,N):
		tempRow.append(1.)
	temp.append(tempRow)
	tempRow=[]
	return np.asarray(temp)

kList = np.arange(1, 101, 1.)

x0 = np.transpose(MakeNB(dimension))
normx0 = np.linalg.norm(x0,2)

newX = np.dot(B,x0)

xList = []
xList.append(newX)
for i in range(0,100):
	x = newX
	newX = np.dot(B,x)
	xList.append(newX)

etaList = []
normxKList = []
for i in range(0,100):
	normxK = np.linalg.norm(xList[i],2)
	normxKList.append(normxK)
	eta = normxK/normx0
	etaList.append(eta)


for i in range(0,100):
	print("k=",i+1,"\teta=",etaList[i])

plt.plot(kList, etaList)
plt.grid()
plt.show()

for i in range(0,100):
	if normxKList[i] < normx0:
		print("\nk=",i+1,"\nnorma x =",normxKList[i])
		break