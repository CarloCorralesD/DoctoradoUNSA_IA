# Autor:  Carlo Corrales Delgado
# usar el Particle Swarm Optimization para calcular el valor minimo de la funcion f(x,y) = (x + 2y -7)2 + (2x + y - 5)2
# con restricciones -10 <= x <= 10      and     -10 <= y <= 10

import math
import sys
import random

def fitness(x,y):
    return (x + 2*y -7)**2 + (2*x + y - 5)**2
    #return (x)**2 + (y)**2

def truncate(nro,dec):
    pos = pow(10.0,dec)
    return math.trunc(pos*nro)/pos

#####

file = open("pso.txt",'w')
file.write("Algoritmo Particle Swarm Optimization\n")
file.write("Parametros:\n")
file.write("- Tamano de la Poblacion: 6\n")
file.write("- Valores iniciales para v_i entre -1.0 y 1.0\n")
file.write("- w: nro aleatorio entre 0.0 y 1.0 para cada iteracion\n")
file.write("- rand_1, rand_2: nros aleatorios entre 0.0 y 1.0 para cada individuo\n")
file.write("- C_1, C_2 : 2.0\n")
file.write("- Cantidad de iteraciones: 100\n")
iteraciones = 100 
individuos = 6
C_1 = 2.0
C_2 = 2.0

#poblacion Inicial:
file.write("\n*** Cumulo de particulas inicial ***\n")
pool = []
velocPool = []
for i in range(individuos):
    pool.append([random.random()*20 - 10 , random.random()*20 - 10])
    #pool.append([truncate(random.random()*10 - 5,12) , truncate(random.random()*10 - 5,12)])
    velocPool.append([truncate(random.random()*2 - 1,12), truncate(random.random()*2 - 1,12)])
    file.write(str(i)+") x1 = "+str(pool[i][0])+"\tx2 = "+str(pool[i][1])+"\t v1 = "+str(velocPool[i][0])+"\t v2 = "+str(velocPool[i][1])+"\n")

#calcular fitness para cada individuo:
file.write("\n*** Fitness para cada individuo:\n")
poolValFun = []
mejorPool = []
for i in range(individuos):
    poolValFun.append(truncate(fitness(pool[i][0],pool[i][1]),12))
    file.write(str(i)+") "+str(poolValFun[i])+"\n")
    mejorPool.append([pool[i][0],pool[i][1],poolValFun[i]])

#mejores locales
file.write("\n*** Mejores locales:\n")
mejorFitness = 9999999
pos = 0
for i in range(individuos):
    if mejorFitness > poolValFun[i]:
        mejorFitness = poolValFun[i]
        pos = i
    file.write(str(i)+") x1 = "+str(mejorPool[i][0])+"\tx2 = "+str(mejorPool[i][1])+"\t fitness = "+str(mejorPool[i][2])+"\n") 
mejorGlobal =  [pool[pos][0], pool[pos][1], poolValFun[pos]]
file.write("\n*** Mejor Global : x1 = "+ str(mejorGlobal[0])+"\t x2 = "+str(mejorGlobal[1])+"\t fitness = "+str(mejorGlobal[2])+"\n")

#iteraciones:
for i in range(iteraciones):
    file.write("\n**** Iteracion "+str(i)+" ****\n")

    w = random.random()
    file.write("w: "+str(w)+"\n")
    rand_1 = random.random()
    rand_2 = random.random()
    file.write("rand_1: "+str(rand_1)+"\t rand_2: "+str(rand_2)+"\n")

    for i in range(individuos):
        nVelX = w*velocPool[i][0] + C_1*rand_1*(mejorPool[i][0] - pool[i][0]) + C_2*rand_2*(mejorGlobal[0]-pool[i][0])
        nVelY = w*velocPool[i][1] + C_1*rand_1*(mejorPool[i][1] - pool[i][1]) + C_2*rand_2*(mejorGlobal[1]-pool[i][1])
        velocPool[i] = [nVelX, nVelY]
        pool[i][0] += velocPool[i][0]
        pool[i][1] += velocPool[i][1]
        file.write(str(i)+")\t x1 = "+str(pool[i][0])+"\t x2 = "+str(pool[i][1])+"\t v1 = "+str(velocPool[i][0])+"\t v2 = "+str(velocPool[i][1])+"\n")

    #calcular fitness para cada individuo:
    file.write("\n*** Fitness para cada individuo:\n")
    for i in range(individuos):
        poolValFun[i] = truncate(fitness(pool[i][0],pool[i][1]),12)
        file.write(str(i)+") "+str(poolValFun[i])+"\n")
        if mejorPool[i][2] > poolValFun[i]:
            mejorPool[i] = [pool[i][0],pool[i][1],poolValFun[i]] 

    #mejores locales
    file.write("\n*** Mejores locales:\n")
    mejorFitness = 9999999
    pos = 0
    for i in range(individuos):
        if mejorFitness > mejorPool[i][2]:
            mejorFitness = mejorPool[i][2]
            pos = i
        file.write(str(i)+") x1 = "+str(mejorPool[i][0])+"\tx2 = "+str(mejorPool[i][1])+"\t fitness = "+str(mejorPool[i][2])+"\n") 
    mejorGlobal =  [mejorPool[pos][0], mejorPool[pos][1], mejorPool[pos][2]]
    file.write("\n*** Mejor Global : x1 = "+ str(mejorGlobal[0])+"\t x2 = "+str(mejorGlobal[1])+"\t fitness = "+str(mejorGlobal[2])+"\n")


file.close()
