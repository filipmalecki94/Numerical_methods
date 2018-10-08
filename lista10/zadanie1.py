from scipy.integrate import quad

def integrand(x,p):
	return x/p
m = 2000
a = 4.7
temp1 = quad(integrand,0,1.0, args=a)
a = 12.2
temp2 = quad(integrand,1.0,1.8, args=a)
a = 19.0
temp3 = quad(integrand,1.8,2.4, args=a)
a = 31.8
temp4 = quad(integrand,2.4,3.5, args=a)
a = 40.1
temp5 = quad(integrand,3.5,4.4, args=a)
a = 43.8
temp6 = quad(integrand,4.4,5.1, args=a)
a = 43.2
temp7 = quad(integrand,5.1,6.0, args=a)

t =  (temp1[0]+temp2[0]+temp3[0]+temp4[0]+temp5[0]+temp6[0]+temp7[0])
print(t)
