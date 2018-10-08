from scipy import optimize
import numpy as np

def f(x):
    return np.cos(x)-(3*np.sin(np.tan(x)-1))

a = 0.
b = 1.5

def pochodna_f(x):
	return -1-1/(np.cos(x)**2)

def newton(x,n=100):
	iteracje = 0
	for i in range(n):
		iteracje+=1
		if pochodna_f(x) == 0:
			return ["Wynik: ",x,"Iteracje: ",iteracje]
		x = x - f(x)/pochodna_f(x)
	return ["Wynik: ",x,"Iteracje: ",iteracje]


def secant(x0,x1,n):
	iteracje = 0
	for i in range(n):
		iteracje+=1
		if f(x1)-f(x0) == 0:
			return ["Wynik: ",x1,"Iteracje: ",iteracje]
		x_temp = x1 - (f(x1)*(x1-x0)*1.0)/(f(x1)-f(x0))
		x0 = x1
		x1 = x_temp
		#print(x1)

	return ["Wynik: ",x1,"Iteracje: ",iteracje]


print("Metoda Brenta")
m_brent=optimize.brenth(f,a,b,full_output=True)
print(m_brent)

print("\n Metoda Bisekscji")
m_bisekcja=optimize.bisect(f,a,b,full_output=True)
print(m_bisekcja)

print("\n Metoda Siecznych")
m_sieczne=secant(a,b,100)
print(m_sieczne)
