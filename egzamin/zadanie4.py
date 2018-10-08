import numpy as np
from scipy.integrate import quad

def f(x):
	return np.exp(-(np.power(x,2)/2))/(np.sqrt(1-np.power(x,2)))

print(quad(f,-1,1))