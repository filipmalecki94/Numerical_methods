import numpy as np

def f1(x):
	return np.power(x,3)-2*x

def f2(x):
	return np.sin(x)

def f3(x):
	return np.exp(x)

def Df1(f,x,h):
	return (f(x+h)-f(x))/h

def Dc2(f,x,h):
	return (f(x+h)-f(x-h))/(2*h)

def Dc4(f,x,h):
	return np.power(2,2)*Dc2(f,x,h)-Dc2(f,x,2*h)

x1 = 1
df1 = 1
x2 = np.pi/3
df2 = 1/2
x3 = 0
df3 = 1

h = 0.1
print("\nf1")
print("h\tdf1-Df1\t\t\tdf1-Dc2\t\t\tdf1-Dc4")
for i in range(0,3):
	print(str(h)+"\t"+str(df1-Df1(f1,x1,h))+"\t"+str(df1-Dc2(f1,x1,h))+"\t"+str(df1-Dc4(f1,x1,h)))
	h /= 10
h = 0.1
print("\nf2")
print("h\tdf2-Df1\t\t\tdf2-Dc2\t\t\tdf2-Dc4")
for i in range(0,3):
	print(str(h)+"\t"+str(df2-Df1(f2,x2,h))+"\t"+str(df2-Dc2(f2,x2,h))+"\t"+str(df2-Dc4(f2,x2,h)))
	h /= 10
h = 0.1
print("\nf3")
print("h\tdf3-Df1\t\t\tdf3-Dc2\t\t\tdf3-Dc4")
for i in range(0,3):
	print(str(h)+"\t"+str(df3-Df1(f3,x3,h))+"\t"+str(df3-Dc2(f3,x3,h))+"\t"+str(df3-Dc4(f3,x3,h)))
	h /= 10
