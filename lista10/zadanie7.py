import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from scipy.misc import derivative

def foo(x,a,b,c,d):
	return a*x*x*x+b*x*x+c*x+d



xdata = np.array([0.0,0.1,0.2,0.3,0.4])
ydata = [0.000000,0.078348,0.138910,0.192916,0.244981]

popt, pcov = curve_fit(foo, xdata, ydata)

def foo2(x):
	return popt[0]*x*x*x+popt[1]*x*x+popt[2]*x+popt[3]

print(derivative(foo2,0.2,dx=1e-6))


plt.plot(xdata,ydata,'g',label='data')

xdata = np.arange(0.0,0.4,0.00001)
plt.plot(xdata,foo(xdata,*popt),'g--',label='fit')
plt.plot(xdata,derivative(foo2,xdata,dx=1e-6),'k--',label='fit2')
plt.legend()
plt.grid()
plt.show()