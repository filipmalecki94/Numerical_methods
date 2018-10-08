import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize

def f(x):
    return np.cosh(x)*np.cos(x)-1

x = np.arange(0, 5, 0.001)
y = [ f(i) for i in x ]

plt.plot(x, y)
plt.grid()
plt.show()

print(optimize.newton(f,4))
