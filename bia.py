# Autor:  Carlo Corrales Delgado
# usar el algoritmo Bat Inspired Artificial para calcular el valor minimo de la funcion f(x,y) = (x + 2y -7)2 + (2x + y - 5)2
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
def rangoFun():
    #return truncate(random.random()*10 - 5,12)
    return truncate(random.random()*20 - 10,12 )
def imprime(poolV):
    file.write("poolV:\n")
    for i in range(individuos):
        file.write(str(poolV[i])+"\n")
    

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
mejorPoolfit = 9999999
mejorPool = 0
aptitud = []
for i in range(individuos):
    aptitud.append(truncate(fitness(pool[i][0],pool[i][1]),12))
    file.write(str(i)+") "+ str(aptitud[i])+"\n")
    if mejorPoolfit > aptitud[i]:
        mejorPoolfit = aptitud[i]
        mejorPool = i 

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
        frec = fmin + (fmax-fmin)*B
        file.write("Frecuencia: "+str(frec)+"\n")
        velocidad[j][0] += (pool[j][0] - pool[mejorPool][0])*frec
        velocidad[j][1] += (pool[j][1] - pool[mejorPool][1])*frec
        file.write("Nueva velocidad: "+str(velocidad[j])+"\n")
        pool[j][0] += velocidad[j][0]
        pool[j][1] += velocidad[j][1] 
        file.write("Nueva posicion: "+str(pool[j])+"\n")




"""
    sumFit = 0
    #poolV = []
    for i2 in range(individuos):
        k = i2
        while k==i2:
            k = random.randrange(individuos)
        j = random.randrange(D)
        phi = random.random()*2 - 1
        if j==0:
            v1 = poolV[i2][0] + phi*(poolV[i2][0]-poolV[k][0])  #V
            v2 = poolV[i2][1] #V
        else:
            v1 = poolV[i2][0] #V
            v2 = poolV[i2][1] + phi*(poolV[i2][1]-poolV[k][1]) #V
        fv = f_x(v1,v2) 
        fitv = fit_x(fv)
        #poolV.append(pool[i2])
        if fitv > poolV[i2][3]: #mejora 
            poolV[i2][0] = v1
            poolV[i2][1] = v2
            poolV[i2][2] = fv
            poolV[i2][3] = fitv
            poolV[i2][4] = 0
        else:
            poolV[i2][4] = poolV[i2][4] + 1 
        file.write("k="+str(k)+" j="+str(j)+" phi="+str(phi)+"\t x1 = "+str(poolV[i2][0])+"\tx2 = "+str(poolV[i2][1])+"\t f_x = "+str(poolV[i2][2])+"\t fit_x = "+str(poolV[i2][3]))
        if poolV[i2][4]==0:  #V
            file.write("\tSI ") 
        else:
            file.write("\tNO ")
        file.write(" cont = "+str(poolV[i2][4])+"\n") 
        sumFit += poolV[i2][3]

    file.write("*** Calcular la probabilidad de seleccion de cada fuente de alimento ***\n")
    acumPorc = []
    for i2 in range(individuos):
        porcFit = poolV[i2][3]/sumFit
        if i2 == 0:
            acumPorc.append(porcFit)
        else:
            acumPorc.append(acumPorc[i2-1]+porcFit)
        file.write(str(i2)+"\t"+str(poolV[i2][0])+"\t"+str(poolV[i2][1])+"\t"+str(poolV[i2][2])+"\t"+str(poolV[i2][3])+"\t"+str(porcFit)+"\t"+str(acumPorc[i2])+"\n")
    #imprime(poolV)

    file.write("\n*** Enviar a abejas Observadoras ***\n")
    for i2 in range(individuos):
        aleat = random.random()
        k = i2
        while k==i2:
            k = random.randrange(individuos)
        j = random.randrange(D)
        for i3 in range(individuos):
            if aleat < acumPorc[i3]:
                i_escog = i3
                break
        file.write("** Observadora "+str(i2)+ " Aleatorio: "+str(aleat)+"\t i="+str(i_escog)+" k="+str(k)+" j="+str(j)+"\n")
        phi = random.random()*2 - 1
        o1 = rangoFun()
        o2 = rangoFun()
        fOx = f_x(o1,o2) 
        fitO = fit_x(fOx)
        if fitO > poolV[i_escog][3]: #mejora
            poolV[i_escog][0] = o1
            poolV[i_escog][1] = o2
            poolV[i_escog][2] = fOx
            poolV[i_escog][3] = fitO
            poolV[i_escog][4] = 0
        else:
            poolV[i_escog][4] = poolV[i_escog][4] + 1 
            
        file.write("phi="+str(phi)+"\t x1 = "+str(o1)+" x2 = "+str(o2)+" f_x = "+str(fOx)+" fit_x = "+str(fitO))
        if poolV[i_escog][4]==0:
            file.write("\tSI ") 
        else:
            file.write("\tNO ")
        file.write(" cont = "+str(poolV[i_escog][4])+"\n") 

        file.write("Nuevas probabilidades\n")
        sumFit = 0
        for i3 in range(individuos):
            sumFit += poolV[i3][3]
        acumPorc = []
        for i3 in range(individuos):
            porcFit = poolV[i3][3]/sumFit
            if i3 == 0:
                acumPorc.append(porcFit)
            else:
                acumPorc.append(acumPorc[i3-1]+porcFit)
            file.write(str(i3)+"\t"+str(poolV[i3][0])+"\t"+str(poolV[i3][1])+"\t"+str(poolV[i3][2])+"\t"+str(poolV[i3][3])+"\t"+str(porcFit)+"\t"+str(acumPorc[i3])+"\n")
    #imprime(poolV)

    file.write("\n*** Enviar a abejas Exploradoras ***\n")
    mejorPoolfit = -9999999
    mejorPool = 0
    for i2 in range(individuos):
        if poolV[i2][4] > D:
            e1 = rangoFun()
            e2 = rangoFun()
            fEx = f_x(e1,e2) 
            fitE = fit_x(fEx)
            contE = 0
            poolV[i2] = [e1,e2,fEx,fitE,contE]
        file.write(str(i2)+" x1 = "+str(poolV[i2][0])+"\tx2 = "+str(poolV[i2][1])+"\t f_x = "+str(poolV[i2][2])+"\t fit_x = "+str(poolV[i2][3])+"\t cont = "+str(poolV[i2][4])+"\n")
        if mejorPoolfit < poolV[i2][3]:
            mejorPoolfit = poolV[i2][3]
            mejorPool = i2
    if MejorSolucion[3] < poolV[mejorPool][3]:
        MejorSolucion = [poolV[mejorPool][0], poolV[mejorPool][1], poolV[mejorPool][2], poolV[mejorPool][3]]
    file.write("*** Mejor fuente de alimento: "+str(MejorSolucion[0])+"\t"+str(MejorSolucion[1])+" = "+str(MejorSolucion[2])+"\n")
   
    #imprime(poolV)
"""
file.close()
