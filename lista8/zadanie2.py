import numpy as np
from scipy import interpolate as int
import matplotlib.pyplot as plt


#zmieniamy na logarytmy
re=[0.2, 2., 20., 200., 2000., 20000.]
cd=[103., 13.9, 2.72, 0.8, 0.401, 0.433]
re_nowe_wartosci=[5., 50., 5000.]

tck=int.splrep(re, cd, s=0)
cd_nowe_wartosci_1=int.splev(re_nowe_wartosci, tck, der=0)
s=int.UnivariateSpline(re, cd)
cd_nowe_wartosci_2=int.UnivariateSpline.__call__(s, re_nowe_wartosci)

print(cd_nowe_wartosci_1)
print(cd_nowe_wartosci_2)