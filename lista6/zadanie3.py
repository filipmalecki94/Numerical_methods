import numpy as np
import scipy as sp
from scipy import linalg

dimension = 20

def MakeNMatrix(N):
  temp = []
  tempRow = []
  for i in range (0,N):
    for j in range(0,N):
      if j == i:
        tempRow.append(4.)
      elif j == i+1:
        tempRow.append(-1.)
      elif j == i-1:
        tempRow.append(-1.)
      elif j == N-1 and i == 0:
        tempRow.append(1.)
      elif j == 0 and i == N-1:
        tempRow.append(1.)
      else:
        tempRow.append(0.)
    temp.append(tempRow)
    tempRow=[]
  return np.asarray(temp)

A = MakeNMatrix(dimension)


def MakeNB(N):
  temp = []
  tempRow = []
  for i in range(0,N):
    if i == N-1:
      tempRow.append(100.)
    else:
      tempRow.append(0.)
    temp.append(tempRow)
    tempRow=[]
  return np.asarray(temp)

b = MakeNB(dimension)

P, L, U = linalg.lu(A)

invLb = np.dot(np.linalg.inv(L),b)

x = np.dot(np.linalg.inv(U),invLb)

# print("x=\n",x)

y = np.linalg.solve(L,b)
x1 = np.linalg.solve(U,y)

print("x=\n",x1)