import math
from uncertainties import ufloat

L = ufloat(0.446, 1/1000)
R = ufloat(124.75/2000, 0.05/1000)
g = ufloat(9.81, 0.01)
r = ufloat(0.0016814, 0.002/1000)
dydx = ufloat(1.5289, 1.5289*5/100)

G = (4*L*R*g)/(math.pi*r**4*dydx)
print(G)