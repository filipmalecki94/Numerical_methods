import numpy as np
from scipy.integrate import quad


def f(x):
    return 1/(3*(x**(4/3)+1))

def alpha(s,k):
	return (s-np.absolute(k-1))/(k-np.absolute(k-1))

for k in range(0,6):
	a = quad(alpha,0,1,args=k)
	

def integration_trapeze(f, a, b, n):
    step=(b-a)/n
    suma=(f(a)+f(b))/2
    x=a+step
    while x<(b-0.00001):
        suma += f(x)
        x +=step
    calka=step*suma      
    return calka

y=integration_trapeze(f, 0, 1, 6)
print(y)
