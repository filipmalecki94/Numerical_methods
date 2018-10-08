import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x,a,b,c,d):
	return a*np.power(x,3)+b*np.power(x,2)+c*np.power(x,1)+d

xdata = np.array([0.,21.1,37.8,54.4,71.1,87.8,100])
ydata = np.array([1.79,1.13,0.696,0.519,0.338,0.321,0.296])

popt, pcov = curve_fit(func, xdata, ydata)

a = popt[0]
b = popt[1]
c = popt[2]
d = popt[3]

print("("+str(a)+")"+"x^3+"+"("+str(b)+")"+"x^2+"+"("+str(c)+")"+"x+"+str(d))
plt.plot(xdata,ydata,'p',label='data')
xdata = np.arange(0, 100, 0.01)
plt.plot(xdata, func(xdata,*popt), 'g--',label='fit')

plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.show()