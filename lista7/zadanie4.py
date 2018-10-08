from scipy.optimize import brenth
import math

def fun(T):
    R=8.31441
    T_0=4.44418
    G=-10**5
    return -R*T*math.log((T/T_0)**3.2)-G
    
rozw=brenth(fun,1,1000000)
print(rozw)
