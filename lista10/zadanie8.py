import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from scipy.misc import derivative

def foo(x,a,b,c,d):
	return a*x*x*x+b*x*x+c*x+d

xdata = np.array([-2.2,-0.3,0.8,1.9])
ydata = np.array([15.180,10.962,1.920,-2.040])


popt, pcov = curve_fit(foo, xdata, ydata)

def foo2(x):
	return popt[0]*x*x*x+popt[1]*x*x+popt[2]*x+popt[3]

print(derivative(foo2,0.0,dx=1e-6))
print(derivative(foo2,0.0,dx=1e-6,n=2))


plt.plot(xdata,ydata,'g',label='data')
xdata=np.arange(-2.2,1.9,0.01)
plt.plot(xdata,foo2(xdata),'g--',label='fit')
plt.plot(xdata,derivative(foo2,xdata,dx=1e-6),'k--',label='df')
plt.plot(xdata,derivative(foo2,xdata,dx=1e-6,n=2),'k',label='df')
plt.grid()
plt.legend()
plt.show()