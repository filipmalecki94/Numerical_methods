import numpy as np
from scipy.integrate import quad

def foo(x):
	return 1 / np.sqrt(1-np.power(np.sin(np.pi/2),2)*np.power(np.sin(x),2))

h15 = np.radians(15)#np.pi/12
h30 = np.radians(30)#np.pi/6
h45 = np.radians(45)#np.pi/4

print("h(15)=",quad(foo,0,h15)[0])
print("h(30)=",quad(foo,0,h30)[0])
print("h(45)=",quad(foo,0,h45)[0])