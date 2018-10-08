import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy
from scipy.optimize import least_squares

def func(x, a, b):
	return a * np.exp(b * x)

xdata=np.array([1.2, 2.8, 4.3, 5.4, 6.8, 7.9])
ydata=np.array([7.5, 16.1, 38.9, 67., 146.6, 266.2])

popt, pcov = curve_fit(func, xdata, ydata)
print(popt)

plt.plot(xdata, ydata, 'p', label='data')
xdata = np.arange(1.2,8.0,0.01)
plt.plot(xdata, func(xdata, *popt), 'r--',label='fit')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()