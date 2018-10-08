import numpy as np
from scipy import interpolate as int
from matplotlib import pyplot as plt

x = [7.99,8.09,8.19,8.7,9.2,10.,12.,15.,20.]
y = [0.,0.0000276,0.4375,0.169183,0.469428,0.94374,0.998636,0.999919,0.999994]
xnew = [10.8,13.2]

s = int.UnivariateSpline(x,y)
ynew = int.UnivariateSpline.__call__(s,xnew)
print(ynew)

plt.plot(x,y,'d')
plt.grid()
plt.show()