# Autor:  Carlo Corrales Delgado
# usar un Algoritmo de programacion Genetica para resolver el problema de crear una funcion matematica
# partiendo de una tabla de entradas y salidas

import random

def operacion(op1,ope,op2,X):
    if op1=='X':
        op1=X
    if op2=='X':
        op2=X
    if ope=='+':
        return op1+op2
    elif ope=='-':
        return op1-op2
    elif ope=='*':
        return op1*op2
    elif ope=='/':
        if op2!=0:
            return 1.0*op1/op2
        else:
            return 0
    else:
        print("Error en operacion no Valida: "+ope)
        return 0
    
def valorFun(pool,X):
    #print(pool)
    op1 = operacion(pool[0],pool[1],pool[2],X)
    op2 = operacion(pool[4],pool[5],pool[6],X)
    op3 = operacion(op1,pool[3],op2,X)
    #print(op3)
    return op3

def fitness(difAct):
    dife = 0
    for i in range(len(difAct)):
        dife += difAct[i]**2
    return dife/len(difAct)

def minimo(a,b,c):
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    else:
        return c

inputOutput = [[0,0],[0.1,0.005],[0.2,0.02],[0.3,0.045],[0.4,0.08],[0.5,0.125],[0.6,0.18],[0.7,0.245],[0.8,0.32],[0.9,0.405]]

file = open("funcionMatematica.txt",'w')
file.write("Algoritmo de Programacion Genetica\n")
file.write("Parametros:\n")
file.write("- Cantidad de individuos: 8\n")
file.write("- Cantidad de genes por individuo: 7\n")
file.write("- Funciones: +,-,*,/\n")
file.write("- Terminales (constantes): -5,-4,-3,-2,-1,1,2,3,4,5     (variables): X\n")
file.write("- Funcion de Aptitud: EMC\n")
file.write("- Probabilidad de Replicacion: 0.2\n")
file.write("- Seleccion para Replicacion - Torneo: 3\n")
file.write("- Probabilidad de cruzamiento: 0.4\n")
file.write("- Seleccion para Cruzamiento - Torneo: 2\n")
file.write("- Cruzamiento de un punto (punto aleatorio)\n")
file.write("- Probabilidad de mutacion: 0.4\n")
file.write("- Seleccion para Mutacion - Torneo: 3\n")
file.write("- Mutacion simple.\n")
file.write("- Cantidad de iteraciones: 50\n")
iteraciones = 50 
individuos = 8
probReplicacion = 20
probCruzamiento = 40
probMutacion = 40

#poblacion Inicial:
pool = []
file.write("Poblacion inicial\n")
for i in range(individuos):
    terminales = [-5,-4,-3,-2,-1,1,2,3,4,5,'X']
    funciones = ['+','-','*','/']
    terAzar = random.randrange(len(terminales))
    indiv = []
    indiv.append(terminales[terAzar])
    for j in range(3):
        funAzar = random.randrange(len(funciones))
        terAzar = random.randrange(len(terminales))
        indiv.append(funciones[funAzar])
        indiv.append(terminales[terAzar])
    #print(indiv)
    pool.append(indiv) 
    file.write(str(i)+") |")
    for j in range(7):
        file.write(str(indiv[j])+"|")
    file.write("\n")

#calcular la aptitud para cada individuo:
fitnessAct = []
sumTot = 0
file.write("\nCalcular la aptitud para cada individuo\n")
for i in range(individuos):
    file.write("\n"+str(i)+") |")
    for j in range(7):
        file.write(str(pool[i][j])+"|")
    file.write("\n")
    difAct = []
    for j in range(len(inputOutput)):
        file.write("%.4f" % inputOutput[j][0] +"\t"+"%.4f" % inputOutput[j][1] +"\t")
        funAct = valorFun(pool[i],inputOutput[j][0])
        difAct.append(inputOutput[j][1] - funAct)
        file.write("%.8f" % funAct + "\t" + "%.8f" % difAct[j] + "\n")
    fitnessAct.append(fitness(difAct))
    file.write("Fitness: "+"%.8f" %fitnessAct[i])

file.write("\nResumen:\n")
for i in range(individuos):
    file.write("\n"+str(i)+") |")
    for j in range(7):
        file.write(str(pool[i][j])+"|")
    file.write("\n")
    file.write("Fitness: "+"%.8f" %fitnessAct[i])

#iteraciones:
for i in range(iteraciones):
    nroPoblacion = 0
    nuevos = []
    file.write("\n\n**** Iteracion "+str(i)+" ****\n")
    while nroPoblacion < individuos:
        hayReplicacion = random.randrange(100)
        if hayReplicacion <= probReplicacion:
            file.write("**** Replicacion **\n")
            file.write("Seleccionados para torneo (3): ")
            sel1 = random.randrange(individuos)
            sel2 = sel1
            while sel2==sel1:
                sel2 = random.randrange(individuos)
            sel3 = sel2
            while sel3==sel2 or sel3==sel1:
                sel3 = random.randrange(individuos)
            file.write(str(sel1)+" - "+str(sel2)+" - "+str(sel3)+"\n")
            f1 = fitnessAct[sel1]
            f2 = fitnessAct[sel2]
            f3 = fitnessAct[sel3]
            mej = minimo(f1,f2,f3)
            if mej==f1:
                mejor = sel1
            elif mej==f2:
                mejor = sel2
            else:
                mejor = sel3
            file.write("Mejor del torneo (3): "+str(mejor)+"\n")
            file.write("Insertar individuo: "+str(mejor)+" => "+str(pool[mejor])+"\n")
            nuevos.append(pool[mejor])
            nroPoblacion += 1
            file.write("Tamano de la nueva poblacion: "+str(nroPoblacion)+"\n")

"""

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
 
"""
