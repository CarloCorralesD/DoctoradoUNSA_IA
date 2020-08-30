# Autor:  Carlo Corrales Delgado
# usar la estrategia Evolutiva 1+1 para calcular el valor minimo de la funcion f(x,y) = (x + 2y -7)2 + (2x + y - 5)2
# con restricciones -10 <= x <= 10      and     -10 <= y <= 10
import math
import sys
import random

pi = 3.14159
mu = 0 
lamb = 0.00002

def fitness(x,y):
    return (x + 2*y -7)**2 + (2*x + y - 5)**2
def fun(x,desv):
    return 1/(desv*math.sqrt(2*pi))*math.exp(-(x-mu)**2 / (2*desv**2))
def nroGaus(desv,prob):
    acu = 0
    x = -8
    while acu<prob and x<8:
        area = lamb*fun(x,desv)
        acu += area
        x += lamb
    return x
#####

file = open("unoMasuno.txt",'w')
file.write("Estrategias Evolutivas  1+1\n")
file.write("Parametros:\n")
file.write("- Cantidad de individuos: 1\n")
file.write("- Cantidad de genes por individuo: 2\n")
file.write("- Cantidad de iteraciones: 300\n")
iteraciones = 300 
desv = 0.2

#poblacion Inicial:
file.write("\nPoblacion inicial\n")
pool = [random.random()*20 - 10 , random.random()*20 - 10]
file.write("1) ["+str(pool[0])+" , "+str(pool[1])+"] ["+str(desv)+" , "+str(desv)+"]\n")

#calcular la aptitud para cada individuo:
file.write("\nCalcular la aptitud para cada individuo\n")
poolValFun = fitness(pool[0],pool[1])
file.write("1) "+str(pool)+"\t["+str(desv)+" , "+str(desv)+"] "+str(poolValFun)+"\n")
 

#iteraciones:
for i in range(iteraciones):
    file.write("\n**** Iteracion "+str(i)+" ****\n")
    poolValFun = fitness(pool[0],pool[1])
    file.write(str(i)+") "+str(pool)+"\t["+str(desv)+" , "+str(desv)+"]\t"+str(poolValFun)+"\n")
    nroAleat1 = random.random()
    nroGaus1 = nroGaus(desv,nroAleat1)
    file.write("Numero aleatorio: 1: "+str(nroAleat1)+"; Numero aleat Gaussiano: "+str(nroGaus1)+"\n")
    nroAleat2 = random.random()
    nroGaus2 = nroGaus(desv,nroAleat2)
    file.write("Numero aleatorio: 2: "+str(nroAleat2)+"; Numero aleat Gaussiano: "+str(nroGaus2)+"\n")
    nuevo = [pool[0]+nroGaus1 , pool[1]+nroGaus2]
    nuevoValFun = fitness(nuevo[0],nuevo[1])
    file.write(str(nuevo)+"\t"+str(nuevoValFun)+"\n")
    if nuevoValFun <= poolValFun:
        pool = nuevo
        desv = 1.5*desv
    else:
        desv = 1.5**(-1/4)*desv
file.close()
