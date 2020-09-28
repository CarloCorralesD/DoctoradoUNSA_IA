# Autor:  Carlo Corrales Delgado
# usar el algoritmo Bat Inspired Artificial para calcular el valor minimo de la funcion f(x,y) = (x + 2y -7)2 + (2x + y - 5)2
# con restricciones -10 <= x <= 10      and     -10 <= y <= 10

import math
import sys
import random

def fitness(x,y):
    return (x + 2*y -7)**2 + (2*x + y - 5)**2
def truncate(nro,dec):
    pos = pow(10.0,dec)
    return math.trunc(pos*nro)/pos
def rangoFun():
    return truncate(random.random()*20 - 10,12 )
    
#####

file = open("bia.txt",'w')
file.write("Algoritmo Bat Inspired Artificial\n")
file.write("Parametros:\n")
file.write("- Tamano de la Poblacion: 10\n")
file.write("- alfa: 0.99\n")
file.write("- gamma: 2.411\n")
file.write("- Sonoridad(A): 0.5026\n")
file.write("- Pulso (r): 0.4205\n")
file.write("- Beta (B): Entre 0 y 1\n")
file.write("- fmin: 0.0\n")
file.write("- fmax: 0.5\n")
file.write("- Epsilon (e): Entre -1 y 1\n")
file.write("- Cantidad de iteraciones: 500\n")
iteraciones = 500 
individuos = 10
alfa = 0.99
gamma = 2.411
A = 0.5026 #Sonoridad
r = 0.4205 #Pulso 
fmin = 0.0
fmax = 0.5
e = random.random()*2 -1 #Epsilon: Entre -1 y 1

#Localizacion Inicial de murcielagos:
file.write("\n*** Localizacion Inicial de murcielagos ***\n")
pool = []
for i in range(individuos):
    x1 = rangoFun()
    x2 = rangoFun()
    pool.append([x1 , x2])
    file.write(str(i)+") x1 = "+str(pool[i][0])+"\tx2 = "+str(pool[i][1])+"\n") 

#Aptitud de cada murcielago:
file.write("\nAptitud de cada murcielago:\n")
mejorPoolfit = 99999999
mejorPool = 0
mejorPoolXY = [-10,10]
aptitud = []
for i in range(individuos):
    aptitud.append(truncate(fitness(pool[i][0],pool[i][1]),12))
    file.write(str(i)+") De "+str(pool[i])+": "+ str(aptitud[i])+"\n")
    if mejorPoolfit > aptitud[i]:
        mejorPoolfit = aptitud[i]
        mejorPool = i 
        mejorPoolXY = [pool[i][0],pool[i][1]]

#Velocidad de los murcielagos iniciales:
file.write("\nVelocidad de los murcielagos iniciales:\n")
velocidad = []
for i in range(individuos):
    velocidad.append([0.0, 0.0])
    file.write(str(i)+") "+str(velocidad[i])+"\n")

file.write("\nMejor murcielago inicial:\n")
file.write(str(pool[mejorPool])+"\n")
file.write("Mejor fitness:\n")
file.write(str(mejorPoolfit)+ "\n")

#iteraciones:
for i in range(iteraciones):
    file.write("\n**** Iteracion "+str(i)+" ****\n")
    for j in range(individuos):
        file.write("\n*** Murcielago "+ str(j)+"  ***\n")
        B = random.random() #Beta: Entre 0 y 1
        file.write("Beta: "+str(B)+"\n")
        frec = fmin + (fmin-fmax)*B  #existia bug
        file.write("Frecuencia: "+str(frec)+"\n")
        velocidad[j][0] += (pool[j][0] - pool[mejorPool][0])*frec
        velocidad[j][1] += (pool[j][1] - pool[mejorPool][1])*frec
        file.write("Nueva velocidad: "+str(velocidad[j])+"\n")
        xnew = pool[j]
        xnew[0] += velocidad[j][0]
        xnew[1] += velocidad[j][1] 
        file.write("Nueva posicion: "+str(xnew)+"\n")  

        aleat = random.random()
        if aleat > r:
            file.write("SI ingresa a pulse rate\n")
            epsilon1 = random.random()*2 -1
            epsilon2 = random.random()*2 -1
            file.write("epsilon1 : "+str(epsilon1)+"\n")
            file.write("epsilon2 : "+str(epsilon2)+"\n")
            xnew = [mejorPoolXY[0] + epsilon1*A, mejorPoolXY[1] + epsilon2*A]
            file.write("Nueva solucion: "+str(xnew)+"\n")
        else:
            file.write("NO ingresa a pulse rate\n")
        #evaluar al murcielago
        xnewfit = truncate(fitness(xnew[0],xnew[1]),12)
        file.write("De "+str(xnew)+" Fitness: "+str(xnewfit)+"\n") 
         
        aleat = random.random()
        if aleat < A and xnewfit < aptitud[j]:
            pool[j] = xnew  #Aqui recien el nuevo reemplaza al anterior
            aptitud[j] = xnewfit
            A *= alfa 
            r *= (1-math.exp(-gamma)) 
            file.write("SI se actualiza la posicion del murcielago "+str(j)+"\t r = "+str(r)+" A = "+str(A)+"\n")
        else:
            file.write("NO se actualiza la posicion del murcielago "+str(j)+"\n")
            #pool[j] = xnew  #no habia esto, y ahora resulta que es necesario???
            aptitud[j] = truncate(fitness(pool[j][0],pool[j][1]),12)
        #ranking para hallar la mejor solucion de la poblacion de murcielagos
        seActualizo = False
        for k in range(individuos):
            if mejorPoolfit > aptitud[k]:
                mejorPoolfit = aptitud[k]
                mejorPool = k 
                mejorPoolXY = [pool[k][0],pool[k][1]]
                file.write("SI se actualiza el minimo global.  Fitness = "+str(mejorPoolfit)+"\n")
                seActualizo = True
        if not seActualizo:
            file.write("NO se actualizo el minimo global.\n")

    #el mejor murcielago
    file.write("\n")
    #for j in range(individuos):
    #    file.write("Murcielago "+str(j)+": "+str(pool[j])+" Aptitud: "+str(aptitud[j])+"\n")
    file.write("\nMejor Fitness = "+str(mejorPoolfit)+"\n")
    file.write("x[0] = "+str(mejorPoolXY[0])+"\n")
    file.write("x[1] = "+str(mejorPoolXY[1])+"\n")

file.close()
