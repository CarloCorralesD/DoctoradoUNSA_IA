# Autor:  Carlo Corrales Delgado
# usar el Algoritmo del Sistema de Hormigas para calcular TSP

import math
import sys
import random

def fitness(x,y):
    return (x + 2*y -7)**2 + (2*x + y - 5)**2
def truncate(nro,dec):
    pos = pow(10.0,dec)
    return math.trunc(pos*nro)/pos

#####

file = open("antSystem.txt",'w')
file.write("Algoritmo Ant System\n")
file.write("Parametros:\n")
file.write("- Cantidad de hormigas: 10\n")
file.write("- Una Ciudad inicial igual para todas las hormigas\n")
file.write("- Ciudad inicial: D\n")
file.write("- Valores de Alpha, Beta, Rho y Q: alp = 1, bet = 1, p = 0.01, Q = 1\n")
file.write("- Cantidad de iteraciones: 100\n")
iteraciones = 100 
alp = 1
bet = 1
individuos = 10
ciudades = 10
p = 0.01
Q = 1

distancia = [[],[12],[3,9],[23,18,89],[1,3,56,87],[5,41,21,46,55],[23,45,12,75,22,21],
[56,5,48,17,86,76,11],[12,41,14,50,14,54,57,63],[11,27,29,42,33,81,48,24,9]]
for i in range(ciudades):
    distancia[i].append(0)
    for j in range(i+1,ciudades):
        distancia[i].append(distancia[j][i])
file.write("\nMatriz de distancias:\n")
for i in range(ciudades):
    file.write(str(distancia[i])+"\n")

#matriz de visibilidad:
file.write("\nmatriz de visibilidad\n")
visibilidad = []
for i in range(ciudades):
    vis = []
    for j in range(ciudades):
        if i==j:
            vis.append(0)
        else:
            visnro = truncate(1.0/distancia[i][j],5)
            vis.append(visnro)
    visibilidad.append(vis)

for i in range(ciudades):
    file.write(str(visibilidad[i])+"\n")

"""
pool = []
desvPool = []
for i in range(mu):
    pool.append([random.random()*20 - 10 , random.random()*20 - 10])
    desvPool.append([desv,desv])
    file.write(str(i)+") "+str(pool[i])+"\t"+str(desvPool[i])+"\n")

#calcular la aptitud para cada individuo:
file.write("\nCalcular la aptitud para cada individuo\n")
poolValFun = []
individ = []
for i in range(mu):
    poolValFun.append(fitness(pool[i][0],pool[i][1]))
    file.write(str(i)+") "+str(pool[i])+"\t"+str(desvPool[i])+"\t"+str(poolValFun[i])+"\n")
    individ.append([pool[i][0],pool[i][1],desvPool[i][0],desvPool[i][1],poolValFun[i]])

#iteraciones:
for i in range(iteraciones):
    file.write("\n**** Iteracion "+str(i)+" ****\n")
"""