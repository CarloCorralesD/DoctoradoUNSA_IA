# Autor:  Carlo Corrales Delgado
# usar un AG para calcular el valor minimo de la funcion x2 - 250x - 125

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


#iteraciones:
for i in range(500):
    file.write("\n**** Iteracion "+str(i)+" ****\n")
    file.write("Creacion de Mating Pool\n")
    matPool = []
    matPoolBin = []
    for j in range(10):
        sel1 = random.randrange(10)
        sel2 = sel1
        while sel2==sel1:
            sel2 = random.randrange(10)
        if poolValFun[sel1] < poolValFun[sel2]:  #funcion minimizar, se escoge el menor
            seleccion = sel1 
        else:
            seleccion = sel2
        matPool.append(seleccion)
        matPoolBin.append(pool[seleccion])
        file.write(str(sel1)+" - "+str(sel2)+" => "+ str(seleccion)+" => "+matPoolBin[j]+"\n")

    nuevos = []
    nue1=nue2=''
    for j in range(5):   
        file.write("\nSeleccion de padres\n")
        sel1 = random.randrange(10)
        sel2 = sel1
        while sel2==sel1:
            sel2 = random.randrange(10)
        file.write(str(sel1)+" - "+str(sel2)+" => "+str(matPool[sel1])+" - "+str(matPool[sel2])+" => "+matPoolBin[sel1]+" - "+matPoolBin[sel2]+"\n")
        hayCruzamiento = random.randrange(100)
        if hayCruzamiento <= 70:
            file.write("Cruzamiento\n")
            nue1 = matPoolBin[sel1][:3]+matPoolBin[sel2][3:]
            nue2 = matPoolBin[sel2][:3]+matPoolBin[sel1][3:]         
        else:
            file.write("Sin Cruzamiento\n")
            nue1 = matPoolBin[sel1]
            nue2 = matPoolBin[sel2]
        file.write(nue1+" - "+nue2+"\n")
        
        hayMutacion = random.randrange(100)
        if hayMutacion <= 5:
            file.write("Mutacion 1\n")
            pos = random.randrange(9)
            if nue1[pos]=='0':
                dig='1'
            else:
                dig='0'
            nue1 = nue1[:pos]+dig+nue1[pos+1:]
            file.write("Posicion "+str(pos)+" => "+nue1+"\n")
        else:
            file.write("Sin Mutacion 1\n")

        hayMutacion = random.randrange(100)
        if hayMutacion <= 5:
            file.write("Mutacion 2\n")
            pos = random.randrange(9)
            if nue2[pos]=='0':
                dig='1'
            else:
                dig='0'
            nue2 = nue2[:pos]+dig+nue2[pos+1:]
            file.write("Posicion "+str(pos)+" => "+nue2+"\n")
        else:
            file.write("Sin Mutacion 2\n")
        
        #ya tenemos a los 2 nuevos integrantes
        nuevos.append(nue1)
        nuevos.append(nue2)

    file.write("\nNueva poblacion\n")
    for j in range(10):
        file.write(str(j)+") "+nuevos[j]+"\n")
    
    #copiar los nuevos a las variables originales para que el ciclo se repita
    for i in range(10):
        pool[i] = nuevos[i] 

    #calcular el fitness:
    file.write("\nCalcular el Fitness\n")
    for i in range(10):
        poolDec[i] = decimal(pool[i])
        poolValFun[i] = fitness(poolDec[i])
        file.write(str(i)+") "+pool[i]+"\t"+str(poolDec[i])+"\t"+str(poolValFun[i])+"\n")

