from scipy.optimize import fsolve
import numpy as np
from matplotlib import pyplot as plt

def fun(zmienne):
    (x,y)=zmienne

    pierwsze_row=np.tan(x)-y-1
    drogie_row=np.cos(x)-3*np.sin(y)

    return[pierwsze_row,drogie_row]

def f(x):
    return np.tan(x)-1

def g(x):
    return np.arcsin(np.cos(x)/3)

rozw=fsolve(fun,[0,0])
print(rozw)


x = np.arange(0.0, 1.5, 0.001)
y1 = [ f(i) for i in x ]
y2 = [ g(i) for i in x ]

plt.plot(x, y1)
plt.plot(x, y2)

xp = [ 0.88159259 ]
yp = [ 0.21359471 ]

plt.plot(xp, yp, 'or')

plt.show()
