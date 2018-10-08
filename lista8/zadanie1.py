import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x,a,b,c):
	return a*np.power(x,2)+np.power(x,1)*b+c

xdata = np.array([0.,3.,6.])
ydata = np.array([1.225,0.905,0.652])

popt, pcov = curve_fit(func, xdata, ydata)

a = popt[0]
b = popt[1]
c = popt[2]

print("("+str(a)+")"+"x^2+"+"("+str(b)+")"+"x+"+str(c))
plt.plot(xdata,ydata,'k',label='data')
xdata = np.arange(0, 6, 0.01)
plt.plot(xdata, func(xdata,*popt), 'g--',label='fit')

plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.show()