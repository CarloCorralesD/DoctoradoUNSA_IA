""" from statistics import fmean as mean
from random import choices

data = [41, 50, 29, 37, 81, 30, 73, 63, 20, 35, 68, 22, 60, 31, 95]
means = sorted(mean(choices(data, k=len(data))) for i in range(100))
#print(means)
print('The sample mean of '+str(mean(data))+' has a .90 confidence interval from '+str(means[5])+' to '+str(means[94]))
 """

# usar un AG para calcular el valor minimo de la funcion x2 - 250x - 125
#import numpy as np
import random

def minimo():
    min=9999999
    minI=0
    for i in range(512):
        f = fitness(i)
        if f<min:
            min=f
            minI = i
    return ("el minimo es "+str(min)+" y el minX es "+str(minI))

def binario(x):
    bin = ''
    for i in range(9):
    #while x>0:
        bin = str(x%2)+bin
        x = int(x/2) 
    return bin

def decimal(b):
    d = 0
    for i in range(9):
        d = d*2 + int(b[i])
    return d

def fitness(x):
    return x*x - 250*x - 25

#print(binario(511))
#print(np.random.normal())
#print(fitness(1))
#print("aleatorio 0-10: "+str(random.randrange(10)))

file = open("minimizar.txt",'w')
file.write("Parametros:\n")
file.write("Funcion: x2 - 250x - 25,   rango: 0<=x<=511, "+ minimo()+"\n")
file.write("- Cantidad de individuos: 10\n")
file.write("- Cantidad de genes por individuo: 9\n")
file.write("- Seleccion por torneo (2)\n")
file.write("- Probabilidad de cruzamiento: 0.7\n")
file.write("- Cruzamiento de un punto (punto 3)\n")
file.write("- Probabilidad de mutacion: 0.05\n")
file.write("- Mutacion Bit Flip\n")
file.write("- Cantidad de iteraciones: 500\n\n")

#poblacion Inicial:
pool = []
file.write("Poblacion inicial\n")
for i in range(10):
    pool.append(binario(random.randrange(511))) 
    file.write(str(i)+") "+pool[i]+"\n")

#calcular la aptitud para cada individuo:
poolDec = []
poolValFun = []
file.write("Calcular la aptitud para cada individuo\n")
for i in range(10):
    poolDec.append(decimal(pool[i]))
    poolValFun.append(fitness(poolDec[i]))
    file.write(str(i)+") "+pool[i]+"\t"+str(poolDec[i])+"\t"+str(poolValFun[i])+"\n")

