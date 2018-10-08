import numpy as np

def foo(x):
	return np.cos(2*np.power(np.cos(x),-1))


def simpson(f, a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)

    for i in range(1, n, 2):
        s += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        s += 2 * f(a + i * h)
    return s * h / 3

w3 = simpson(foo,-1.,1.,3)
print(w3)
w5 = simpson(foo,-1.,1.,5)
print(w5)
w7 = simpson(foo,-1.,1.,7)
print(w7)
# for i in range(1,100):
# 	w = simpson(foo,-1.,1.,i)
# 	print(i,w)
