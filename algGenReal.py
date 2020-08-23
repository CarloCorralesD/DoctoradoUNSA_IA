# Autor:  Carlo Corrales Delgado
# usar un AG para calcular el valor minimo de la funcion f(x,y) = (x + 2y -7)2 + (2x + y - 5)2
# con restricciones -10 <= x <= 10      and     -10 <= y <= 10

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

def fitness(x,y):
    return (x + 2*y -7)**2 + (2*x + y - 5)**2

#print(binario(511))
#print(np.random.normal())
#print(fitness(1))
#print("aleatorio 0-10: "+str(random.randrange(10)))

file = open("minimizarReal.txt",'w')
file.write("Parametros:\n")
file.write("Funcion: (x+2y-7)2 + (2x+y-5)2,   rango: -10<=x<=10,   -10<=y<=10"+ minimo()+"\n")
file.write("- Cantidad de individuos: 20\n")
file.write("- Cantidad de genes por individuo: 2\n")
file.write("- Seleccion por torneo (2)\n")
file.write("- Probabilidad de cruzamiento: 0.7\n")
file.write("- Cruzamiento BLX-Alpha, Alpha=0.5   -0.5<=Beta<=1.5\n")
file.write("- Probabilidad de mutacion: 0.05\n")
file.write("- Mutacion Uniforme\n")
file.write("- Cantidad de iteraciones: 5000\n\n")
iteraciones = 5000
individuos = 20
probCruzamiento = 70
probMutacion = 5

#poblacion Inicial:
pool = []
file.write("Poblacion inicial\n")
for i in range(individuos):
    pool.append([random.random()*20 - 10,random.random()*20 - 10]) 
    file.write(str(i)+") "+str(pool[i][0])+" , "+str(pool[i][1])+"\n")

#calcular la aptitud para cada individuo:
poolValFun = []
file.write("\nCalcular la aptitud para cada individuo\n")
for i in range(individuos):
     poolValFun.append(fitness(pool[i][0],pool[i][1]))
     file.write(str(i)+") "+str(pool[i])+"\t"+str(poolValFun[i])+"\n")
 

#iteraciones:
for i in range(iteraciones):
    file.write("\n**** Iteracion "+str(i)+" ****\n")
    file.write("Creacion de Mating Pool\n")
    matPool = []
    matPoolBin = []
    for j in range(individuos):
        sel1 = random.randrange(individuos)
        sel2 = sel1
        while sel2==sel1:
            sel2 = random.randrange(individuos)
        if poolValFun[sel1] < poolValFun[sel2]:  #funcion minimizar, se escoge el menor
            seleccion = sel1 
        else:
            seleccion = sel2
        matPool.append(seleccion) #0-19
        matPoolBin.append(pool[seleccion])  #[x,y]
        file.write(str(sel1)+" - "+str(sel2)+" => "+ str(seleccion)+" => "+str(matPoolBin[j])+"\n")

    nuevos = []
    for j in range(individuos):   
        file.write("\nSeleccion de padres\n")
        sel1 = random.randrange(individuos)
        sel2 = sel1
        while sel2==sel1:
            sel2 = random.randrange(10)
        file.write(str(sel1)+" - "+str(sel2)+" => "+str(matPool[sel1])+" - "+str(matPool[sel2])+" => "+str(matPoolBin[sel1])+" - "+str(matPoolBin[sel2])+"\n")
        hayCruzamiento = random.randrange(100)
        if hayCruzamiento <= probCruzamiento:
            file.write("Cruzamiento\n")
            hijoFactible = False
            cont = 0
            while not hijoFactible and cont<100:
                Beta = random.random()*2 - 0.5
                file.write("Beta "+str(cont)+": "+str(Beta)+"\n")
                nueX = matPoolBin[sel1][0]+Beta*(matPoolBin[sel2][0]-matPoolBin[sel1][0])
                nueY = matPoolBin[sel1][1]+Beta*(matPoolBin[sel2][1]-matPoolBin[sel1][1])  
                if nueX>=-10 and nueX<=10 and nueY>=-10 and nueY<=10:
                    hijoFactible = True
                cont +=1
            nuevo = [nueX,nueY]      
        else:
            file.write("Sin Cruzamiento\n")
            azar = random.randrange(2)
            if azar==0:
                nuevo = matPoolBin[sel1]
            else:
                nuevo = matPoolBin[sel2]
        file.write(str(nuevo)+"\n") 
        
        hayMutacion = random.randrange(100)
        if hayMutacion <= probMutacion:
            file.write("Mutacion\n")
            pos = random.randrange(2)
            if pos==0:
                nuevo = [random.random()*20 -10, nuevo[1]]
            else:
                nuevo = [nuevo[0], random.random()*20 -10]
            file.write(str(nuevo)+"\n")
        else:
            file.write("Sin Mutacion\n")
        
        #ya tenemos al nuevo integrante
        nuevos.append(nuevo)

    file.write("\nNueva poblacion\n")
    for j in range(individuos):
        file.write(str(j)+") "+str(nuevos[j])+"\n")
    
    #copiar los nuevos a las variables originales para que el ciclo se repita
    for i in range(individuos):
        pool[i] = nuevos[i] 

    #calcular el fitness:
    file.write("\nCalcular el Fitness\n")
    for i in range(individuos):
        poolValFun[i] = fitness(pool[i][0],pool[i][1])
        file.write(str(i)+") "+str(pool[i])+"\t"+str(poolValFun[i])+"\n")

