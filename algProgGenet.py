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
        dife = difAct[i]**2 + dife
    sol = dife/len(difAct)
    #print("sol: "+str(sol)+" difAct: "+str(difAct))
    return sol

def minimo(a,b,c):
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    else:
        return c

def printIndividuo(file,i,pool):
    file.write(str(i)+") |")
    for j in range(7):
        file.write(str(pool[i][j])+"|")
    file.write("\n")

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
    printIndividuo(file,i,pool)


#calcular la aptitud para cada individuo:
fitnessAct = []
file.write("\nCalcular la aptitud para cada individuo\n")
for i in range(individuos):
    printIndividuo(file,i,pool)
    difAct = []
    for j in range(len(inputOutput)):
        #print("inputOutput[j]: "+str(inputOutput[j]))
        file.write("%.4f" % inputOutput[j][0] +"\t"+"%.4f" % inputOutput[j][1] +"\t")
        funAct = valorFun(pool[i],inputOutput[j][0])
        #print("funAct: "+str(funAct))
        difAct.append(inputOutput[j][1] - funAct)
        #print("difAct[j]: "+str(difAct[j]))
        file.write("%.8f" % funAct + "\t" + "%.8f" % difAct[j] + "\n")
    fitnessAct.append(fitness(difAct))
    #print("fitnessAct[i]: "+str(fitnessAct[i]))
    file.write("Fitness: "+"%.8f" %fitnessAct[i]+"\n")

file.write("\nResumen:\n")
for i in range(individuos):
    printIndividuo(file,i,pool)
    file.write("Fitness: "+"%.8f" %fitnessAct[i]+"\n")

#iteraciones:
for i in range(iteraciones):
    nroPoblacion = 0
    nuevos = []
    file.write("\n\n**** Iteracion "+str(i)+" ****\n")
    while nroPoblacion < individuos:
        hayReplicacion = random.randrange(100)
        if hayReplicacion <= probReplicacion:
            file.write("Aleatorio: "+str(1.0*hayReplicacion/100)+"\n")
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
            file.write("Insertar individuo: ")
            printIndividuo(file,mejor,pool)
            nuevos.append(pool[mejor])
            nroPoblacion += 1
            file.write("Tamano de la nueva poblacion: "+str(nroPoblacion)+"\n")
            if nroPoblacion==individuos:
                break

        hayCruzamiento = random.randrange(100)
        if hayCruzamiento <= probCruzamiento:
            file.write("Aleatorio: "+str(1.0*hayCruzamiento/100)+"\n")
            file.write("**** Cruzamiento **\n")
            file.write("Seleccionados para torneo (2): ")
            sel1 = random.randrange(individuos)
            sel2 = sel1
            while sel2==sel1:
                sel2 = random.randrange(individuos)
            file.write(str(sel1)+" - "+str(sel2)+" => ")
            f1 = fitnessAct[sel1]
            f2 = fitnessAct[sel2]
            if f2>f1:
                mejor = sel1
            else:
                mejor = sel2
            printIndividuo(file,mejor,pool)
            mejpool1 = pool[mejor]

            file.write("Seleccionados para torneo (2): ")
            sel1 = random.randrange(individuos)
            sel2 = sel1
            while sel2==sel1:
                sel2 = random.randrange(individuos)
            file.write(str(sel1)+" - "+str(sel2)+" => ")
            f1 = fitnessAct[sel1]
            f2 = fitnessAct[sel2]
            if f2>f1:
                mejor = sel1
            else:
                mejor = sel2
            printIndividuo(file,mejor,pool)
            mejpool2 = pool[mejor]

            ptoCruz = random.randrange(7)
            file.write("Punto para el cruzamiento: "+str(ptoCruz)+"\n")
            nuevo1 = mejpool1[:ptoCruz]+mejpool2[ptoCruz:]
            nuevo2 = mejpool2[:ptoCruz]+mejpool1[ptoCruz:]
            file.write("Descendiente 1: |")
            for j in range(7):
                file.write(str(nuevo1[j])+"|")
            file.write("\n")
            file.write("Descendiente 2: |")
            for j in range(7):
                file.write(str(nuevo2[j])+"|")
            file.write("\n")
            if nroPoblacion+2 <= individuos:
                nuevos.append(nuevo1)
                nuevos.append(nuevo2)
                nroPoblacion += 2
                file.write("Insertar ambos descendientes\n")
            else:
                nroPoblacion += 1
                nroAzar = random.randrange(2)
                if nroAzar==0:
                    descen = nuevo1
                else:
                    descen = nuevo2
                nuevos.append(descen)
                file.write("Insertar 1 descendiente al azar: |")
                for j in range(7):
                    file.write(str(descen[j])+"|")
                file.write("\n")
            file.write("Tamano de la nueva poblacion: "+str(nroPoblacion)+"\n") 
            if nroPoblacion==individuos:
                break
        
        hayMutacion = random.randrange(100)
        if hayMutacion <= probMutacion:
            file.write("Aleatorio: "+str(1.0*hayMutacion/100)+"\n")
            file.write("**** Mutacion **\n")
            file.write("Seleccion para torneo (3): ")
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
            file.write("Individuo a mutar: ")
            printIndividuo(file,mejor,pool)
            alAzar = random.randrange(7)
            file.write("Gen a mutar: "+str(alAzar)+"\n")
            nuevo = pool[mejor]
            if alAzar%2==0:
                valMutar = random.randrange(len(terminales))
                nuevo[alAzar] = terminales[valMutar]
            else:
                valMutar = random.randrange(len(funciones))
                nuevo[alAzar] = funciones[valMutar]
            #print("nuevo por Mutacion: "+str(nuevo)+"\n")

            file.write("Individuo a insertar: |")
            for j in range(7):
                file.write(str(nuevo[j])+"|")
            file.write("\n")
            nuevos.append(nuevo)
            nroPoblacion += 1
            file.write("Tamano de la nueva poblacion: "+str(nroPoblacion)+"\n") 

    file.write("\nNueva poblacion\n")
    for j in range(individuos):
        file.write(str(j)+") |")
        for k in range(7):
            file.write(str(nuevos[j][k])+"|")
        file.write("\n")
        #+str(nuevos[j])+"\n")
    
    #copiar los nuevos a las variables originales para que el ciclo se repita
    for i in range(individuos):
        pool[i] = nuevos[i] 

    #calcular la aptitud para cada individuo:
    file.write("\nCalcular la aptitud para cada individuo\n")
    for i in range(individuos):
        printIndividuo(file,i,pool)
        difAct = []
        for j in range(len(inputOutput)):
            file.write("%.4f" % inputOutput[j][0] +"\t"+"%.4f" % inputOutput[j][1] +"\t")
            funAct = valorFun(pool[i],inputOutput[j][0])
            difAct.append(inputOutput[j][1] - funAct)
            file.write("%.8f" % funAct + "\t" + "%.8f" % difAct[j] + "\n")
        fitnessAct[i] = fitness(difAct)
        file.write("Fitness: "+"%.8f" %fitnessAct[i]+"\n")

    file.write("\nResumen:\n")
    for i in range(individuos):
        printIndividuo(file,i,pool)
        file.write("Fitness: "+"%.8f" %fitnessAct[i]+"\n")

