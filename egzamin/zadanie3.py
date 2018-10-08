from scipy import optimize
import numpy as np
from matplotlib import pyplot as plt



def f(x):
	return np.cos(x)-(3*np.sin(np.tan(x)-1))

x = np.arange(0.0,1.51,0.0001)
y = [f(i) for i in x]


a = 0
b = 1.
m_brent=optimize.brenth(f,a,b)
print(m_brent)
a = 1.
b = 1.4
m_brent=optimize.brenth(f,a,b)
print(m_brent)
a = 1.4
b = 1.45
m_brent=optimize.brenth(f,a,b)
print(m_brent)
a =1.45
b = 1.48
m_brent=optimize.brenth(f,a,b)
print(m_brent)
a = 1.48
b = 1.5
m_brent=optimize.brenth(f,a,b)
print(m_brent)
plt.plot(x,y)
plt.grid()
plt.show()