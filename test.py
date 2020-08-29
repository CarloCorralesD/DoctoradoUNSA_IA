import math
import sys

pi = 3.14159
mu = 0 
lamb = 0.00002

def fun(x,desv):
    return 1/(desv*math.sqrt(2*pi))*math.exp(-(x-mu)**2 / (2*desv**2))
def nroGaus(desv,prob):
    acu = 0
    x = -8
    while acu<prob or x>8:
        area = lamb*fun(x,desv)
        acu += area
        x += lamb
    return x

print(nroGaus(float(sys.argv[2]),float(sys.argv[1])))