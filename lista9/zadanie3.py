import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x,a,b,c):
	return a*np.power(x,2)+x*b+c

def func2(x,a,b):
	return a*x+b

xdata = np.array([1.0,1.1,1.8,2.2,2.5,3.5,3.7,4.0])
ydata = np.array([6.008,5.257,9.549,11.098,15.722,27.13,28.828,33.772])

plt.plot(xdata,ydata,'p',label='data')

# liniowa
popt, pcov = curve_fit(func2, xdata, ydata)

a = popt[0]
b = popt[1]

print("("+str(a)+")"+"x+"+str(b))
plt.plot(xdata, func2(xdata,*popt), 'g--',label='fit liniowa')

# kwadratowa
popt, pcov = curve_fit(func, xdata, ydata)

a = popt[0]
b = popt[1]
c = popt[2]

xdata = np.arange(1.0,4.0,0.1)
print("("+str(a)+")"+"x^2+"+"("+str(b)+")"+"x+"+str(c))
plt.plot(xdata, func(xdata,*popt), 'r--',label='fit kwadratowa')

plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.show()