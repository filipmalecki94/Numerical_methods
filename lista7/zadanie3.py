from scipy.optimize import brenth
import math

def fun(t):
    u=2510
    M_0=2.8*(10**6)
    m_prim=13300
    g=9.81
    v=335
    return u*math.log(M_0/(M_0-m_prim*t))-(g*t)-v

rozw=brenth(fun,60,80)
print(rozw)
