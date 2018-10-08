from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

def rk4(f1, f2, x1_0, x2_0, t0, n):
    vx1 = [0] * (n + 1)
    vx2 = [0] * (n + 1)
    vt = [0] * (n + 1)
    h = 0.01
    vx1[0] = x1 = x1_0
    vx2[0] = x2 = x2_0
    vt[0] = t = t0
    for i in range(1, n + 1):
        k11 = h * f1(t, x1, x2)
        k21 = h * f2(t, x1, x2)
        k12 = h * f1(t, x1 + 0.5 * h, x2 + 0.5 * k11)
        k22 = h * f2(t, x1 + 0.5 * h, x2 + 0.5 * k21)
        k13 = h * f1(t, x1 + 0.5 * h, x2 + 0.5 * k12)
        k23 = h * f2(t, x1 + 0.5 * h, x2 + 0.5 * k22)
        k14 = h * f1(t, x1 + h, x2 + k13)
        k24 = h * f2(t, x1 + h, x2 + k23)

        vt[i] = t = t0 + i * h 
        vx1[i] = x1 = x1 + (k11 + k12 + k12 + k13 + k13 + k14) / 6.
        vx2[i] = x2 = x2 + (k21 + k22 + k22 + k23 + k23 + k24) / 2.
    return vx1, vx2, vt
 
def f1(t, x1, x2):
    return 0.5*np.cos(2./3.*t)-0.5*x1-np.sin(x2)

def f2(t, x1, x2):
    return x1

xdata = []
ydata = []

vx1, vx2, vt = rk4(f1, f2, 0, 0.01, 0, 100000)
for x1, x2, t in list(zip(vx1, vx2, vt))[::1]:
    xdata.append(x1)
    ydata.append(x2)

plt.plot(xdata,ydata)
plt.show()


 
