# Autor:  Carlo Corrales Delgado
# usar un AG para resolver el problema de vendedor viajero TSP
# con restricciones de 10 nodos

import random

def minimo():
    min=9999999
    minX=-10
    minY=-10
    for x in range(-10,10):
        for y in range(-10,10):
            f = fitness(x,y)
            if f<min:
                min=f
                minX = x
                minY = y
    return ("el minimo es "+str(min)+" y el minX,minY es "+str(minX)+","+str(minY))

def fitness(pool):
    dis = 0
    #print(pool)
    for i in range(10):
        orig = ord(pool[i])-65
        dest = ord(pool[(i+1)%10])-65
        dis = dis + distancias[orig][dest]
        #print(dis)
    return dis

distancias = [[0,1,3,23,11,5,83,21,28,45],[1,0,1,18,3,41,20,61,95,58],
            [3,1,0,1,56,21,43,17,83,16],[23,18,1,0,1,46,44,45,50,11],
            [11,3,56,1,0,1,93,38,78,41],[5,41,21,46,1,0,1,90,92,97],
            [83,20,43,44,93,1,0,1,74,29],[21,61,17,45,38,90,1,0,1,28],
            [28,95,83,50,78,92,74,1,0,1],[45,58,16,11,41,97,29,28,1,0]]
for i in range(10):
    for j in range(10):
        if distancias[i][j]!=distancias[j][i]:
            print("error en "+str(i)+","+str(j)) 
file = open("minimizarPermuta.txt",'w')
file.write("Problema TSP con n=10\n")
file.write("Parametros:\n")
file.write("- Cantidad de individuos: 100\n")
file.write("- Cantidad de genes por individuo: 10\n")
file.write("- Seleccion por Ruleta\n")
file.write("- Probabilidad de cruzamiento: 0.9\n")
file.write("- Cruzamiento PBX\n")
file.write("- Probabilidad de mutacion: 0.5\n")
file.write("- Mutacion de Intercambio\n")
file.write("- Cantidad de iteraciones: 2000\n\n")
iteraciones = 2000 
individuos = 100
probCruzamiento = 90
probMutacion = 50

#poblacion Inicial:
pool = []
file.write("Poblacion inicial\n")
for i in range(individuos):
    camino = 'ABCDEFGHIJ'
    newCamino = ''
    dec = 10
    for j in range(10):
        pos = random.randrange(dec)
        newCamino = newCamino+camino[pos]
        camino = camino[:pos]+camino[pos+1:]
        dec -=1
    #print(newCamino)
    pool.append(newCamino) 
    file.write(str(i)+") "+str(pool[i])+"\n")

#calcular la aptitud para cada individuo:
poolValFun = []
poolValInv = []
sumTot = 0
file.write("\nCalcular la aptitud para cada individuo\n")
for i in range(individuos):
    poolValFun.append(fitness(pool[i]))
    poolValInv.append(1.0/poolValFun[i])
    sumTot += poolValInv[i]
poolPorcent = []
for i in range(individuos):
    poolPorcent.append(poolValInv[i]/sumTot)
    file.write(str(i)+") "+str(pool[i])+"\t"+str(poolValFun[i])+"\t"+"%.8f" % poolValInv[i] +"\t %.8f" % poolPorcent[i] +"\n")
 

#iteraciones:
for i in range(iteraciones):
    file.write("\n**** Iteracion "+str(i)+" ****\n")
    file.write("Creacion de Mating Pool\n")
    matPool = []
    for j in range(individuos):
        nroAzar = random.random()
        seleccion = 0
        sumPorcent = poolPorcent[0]
        #print("nroAzar: "+str(nroAzar))
        while nroAzar > sumPorcent:
            seleccion +=1
            sumPorcent += poolPorcent[seleccion]
            #print("sumPorcent "+str(seleccion)+": "+str(sumPorcent))
        matPool.append(pool[seleccion]) 
        file.write("%.8f" % nroAzar +" => "+str(seleccion)+" => "+str(matPool[j])+"\n")

    nuevos = []
    for j in range(individuos/2):   
        file.write("\nSeleccion de padres\n")
        sel1 = random.randrange(individuos)
        sel2 = sel1
        while sel2==sel1:
            sel2 = random.randrange(individuos)
        file.write(str(sel1)+" - "+str(sel2)+" => "+str(matPool[sel1])+" - "+str(matPool[sel2])+"\n")
        
        hayCruzamiento = random.randrange(100)
        if hayCruzamiento <= probCruzamiento:
            file.write("Cruzamiento\n")
            cuantos = random.randrange(1,10)
            posiciones = []
            for k in range(cuantos):
                g = random.randrange(1,10)
                if g not in posiciones:
                    posiciones.append(g)
            posiciones.sort()
            file.write(str(posiciones)+"\n")
            nue1 = matPool[sel1]
            nue2 = matPool[sel2] 
            #print("nue1 Orig: "+nue1)
            #print("nue2 Orig: "+nue2)
            camino1 = ['A','B','C','D','E','F','G','H','I','J']
            camino2 = ['A','B','C','D','E','F','G','H','I','J']
            #print(posiciones)
            for k in range(len(posiciones)):
                letraAelim1 = matPool[sel2][posiciones[k]]
                letraAelim2 = matPool[sel1][posiciones[k]]
                nue1 = nue1[:posiciones[k]]+letraAelim1+nue1[posiciones[k]+1:]
                nue2 = nue2[:posiciones[k]]+letraAelim2+nue2[posiciones[k]+1:]
                camino1.remove(letraAelim1)
                camino2.remove(letraAelim2)
            noposiciones = []
            for k in range(10):
                if k not in posiciones:
                    noposiciones.append(k)
            #print("noposiciones: "+str(noposiciones))
            nopos1 = 0
            nopos2 = 0
            for k in range(10):
                if matPool[sel1][k] in camino1:
                    nue1 = nue1[:noposiciones[nopos1]]+matPool[sel1][k]+nue1[noposiciones[nopos1]+1:]
                    camino1.remove(matPool[sel1][k])
                    nopos1 +=1
                if matPool[sel2][k] in camino2:
                    nue2 = nue2[:noposiciones[nopos2]]+matPool[sel2][k]+nue2[noposiciones[nopos2]+1:]
                    camino2.remove(matPool[sel2][k])
                    nopos2 +=1

            #print("nue1: "+nue1)
            #print("nue2: "+nue2)
                 
        else:
            file.write("Sin Cruzamiento\n")
            nue1 = matPool[sel1]
            nue2 = matPool[sel2] 
        file.write(nue1+" - "+nue2+"\n") 
        
        hayMutacion = random.randrange(100)
        if hayMutacion <= probMutacion:
            file.write("Mutacion 1\n")
            pos1 = random.randrange(10)
            pos2 = pos1
            while pos2==pos1:
                pos2 = random.randrange(10)
            if pos1 > pos2:
                pos1,pos2 = pos2,pos1
            nue1 = nue1[:pos1]+nue1[pos2]+nue1[pos1+1:pos2]+nue1[pos1]+nue1[pos2+1:]  
            file.write("Posicion: "+str(pos1)+" - "+str(pos2)+" => "+ nue1 +"\n")
        else:
            file.write("Sin Mutacion 1\n")
        
        hayMutacion = random.randrange(100)
        if hayMutacion <= probMutacion:
            file.write("Mutacion 2\n")
            pos1 = random.randrange(10)
            pos2 = pos1
            while pos2==pos1:
                pos2 = random.randrange(10)
            if pos1 > pos2:
                pos1,pos2 = pos2,pos1
            nue2 = nue2[:pos1]+nue2[pos2]+nue2[pos1+1:pos2]+nue2[pos1]+nue2[pos2+1:]  
            file.write("Posicion: "+str(pos1)+" - "+str(pos2)+" => "+ nue2 +"\n")
        else:
            file.write("Sin Mutacion 2\n")

        #ya tenemos a los nuevos integrantes
        nuevos.append(nue1)
        nuevos.append(nue2)

    file.write("\nNueva poblacion\n")
    for j in range(individuos):
        file.write(str(j)+") "+str(nuevos[j])+"\n")
    
    #copiar los nuevos a las variables originales para que el ciclo se repita
    for i in range(individuos):
        pool[i] = nuevos[i] 

    #calcular el fitness:
    file.write("\nCalcular el Fitness\n")
    sumTot = 0
    for i in range(individuos):
        poolValFun[i] = fitness(pool[i])
        poolValInv[i] = 1.0/poolValFun[i]
        sumTot += poolValInv[i]
    for i in range(individuos):
        poolPorcent[i] = poolValInv[i]/sumTot
        file.write(str(i)+") "+str(pool[i])+"\t"+str(poolValFun[i])+"\t"+"%.8f" % poolValInv[i] +"\t %.8f" % poolPorcent[i] +"\n")
 

