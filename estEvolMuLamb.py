# Autor:  Carlo Corrales Delgado
# usar la estrategia Evolutiva Mu+Lambda para calcular el valor minimo de la funcion f(x,y) = (x + 2y -7)2 + (2x + y - 5)2
# con restricciones -10 <= x <= 10      and     -10 <= y <= 10
import math
import sys
import random

def fitness(x,y):
    return (x + 2*y -7)**2 + (2*x + y - 5)**2
def fun(x,desv):
    return 1/(desv*math.sqrt(2*pi))*math.exp(-(x-mu)**2 / (2*desv**2))
def nroGaus(desv,prob):
    acu = 0
    x = -8
    while acu<prob and x<8:
        area = inter*fun(x,desv)
        acu += area
        x += inter
    return x
def myFunc(e):
    return e[4]
#####

file = open("MuMasLambda.txt",'w')
file.write("Estrategia Evolutiva  Mu+Lambda\n")
file.write("Parametros:\n")
file.write("- Cantidad de individuos (Mu): 8\n")
file.write("- Cantidad de descendientes (Lamb): 6\n")
file.write("- Desviacion estandar inicial: 0.2\n")
file.write("- Cantidad de genes por individuo: 2\n")
file.write("- Seleccion por torneo (2)\n")
file.write("- Cantidad de iteraciones: 300\n")
iteraciones = 300 
desv = 0.2
pi = 3.14159
mu = 8
lamb = 6
inter = 0.0002
n = 2

#poblacion Inicial:
file.write("\nPoblacion inicial\n")
pool = []
desvPool = []
for i in range(mu):
    pool.append([random.random()*20 - 10 , random.random()*20 - 10])
    desvPool.append([desv,desv])
    file.write(str(i)+") ["+str(pool[i][0])+" , "+str(pool[i][1])+"]\t["+str(desvPool[i][0])+" , "+str(desvPool[i][1])+"]\n")

#calcular la aptitud para cada individuo:
file.write("\nCalcular la aptitud para cada individuo\n")
poolValFun = []
individ = []
for i in range(mu):
    poolValFun.append(fitness(pool[i][0],pool[i][1]))
    file.write(str(i)+") "+str(pool[i])+"\t["+str(desvPool[i][0])+" , "+str(desvPool[i][1])+"]\t"+str(poolValFun[i])+"\n")
    individ.append([pool[i][0],pool[i][1],desvPool[i][0],desvPool[i][1],poolValFun[i]])

#iteraciones:
for i in range(iteraciones):
    file.write("\n**** Iteracion "+str(i)+" ****\n")
    for j in range(lamb):
        file.write("Generar Descendiente "+str(j)+"\n")
        file.write("Cruzamiento\n")
        padre1 = random.randrange(mu)
        padre2 = padre1
        while padre2==padre1:
            padre2 = random.randrange(mu)
        fitPadre1 = fitness(individ[padre1][0],individ[padre1][1])
        fitPadre2 = fitness(individ[padre2][0],individ[padre2][1])
        if fitPadre1<fitPadre2:
            ganador1 = padre1
        else:
            ganador1 = padre2
        file.write("Padre 1: "+str(padre1)+" - "+str(padre2)+" => "+str(ganador1)+" => "+str(individ[ganador1])+"\n")

        padre1 = random.randrange(mu)
        padre2 = padre1
        while padre2==padre1:
            padre2 = random.randrange(mu)
        fitPadre1 = fitness(individ[padre1][0],individ[padre1][1])
        fitPadre2 = fitness(individ[padre2][0],individ[padre2][1])
        if fitPadre1<fitPadre2:
            ganador2 = padre1
        else:
            ganador2 = padre2
        file.write("Padre 2: "+str(padre1)+" - "+str(padre2)+" => "+str(ganador2)+" => "+str(individ[ganador2])+"\n")
        nuevo = [(individ[ganador1][0]+individ[ganador2][0])/2 , (individ[ganador1][1]+individ[ganador2][1])/2]
        desvNuevo = [math.sqrt(individ[ganador1][2]*individ[ganador2][2]) , math.sqrt(individ[ganador1][3]*individ[ganador2][3])]
        file.write(str(nuevo)+"\t"+str(desvNuevo)+"\n")
        if nuevo[0]<-10 or nuevo[0]>10 or nuevo[1]<-10 or nuevo[1]>10:
            print("error en nuevo: "+str(nuevo))
        
        file.write("Mutacion\n")
        cont = 0
        nuevoN = [-11,11]
        while (nuevoN[0]<-10 or nuevoN[0]>10 or nuevoN[1]<-10 or nuevoN[1]>10) and cont<5:
            nroAleat1 = random.random()
            nroAleat2 = random.random()
            #file.write("Aleatorio 1: "+str(nroAleat1)+"\t- Aleatorio 2: "+str(nroAleat2)+"\n")
            deltaPhi = 1/(math.sqrt(2*math.sqrt(n)))
            #expon1 = nroGaus(deltaPhi,nroAleat1)
            expon1 = math.exp(nroGaus(deltaPhi,nroAleat1))
            #print("expon1: "+str(expon1))
            #expon2 = nroGaus(deltaPhi,nroAleat2)
            expon2 = math.exp(nroGaus(deltaPhi,nroAleat2))
            desvNuevoN = [desvNuevo[0]*expon1 , desvNuevo[1]*expon2 ]
            nroAleat3 = random.random()
            nroAleat4 = random.random()
            #file.write("Aleatorio 1: "+str(nroAleat3)+"\t- Aleatorio 2: "+str(nroAleat4)+"\n")
            nuevoN = [nuevo[0]+nroGaus(desvNuevoN[0],nroAleat3) , nuevo[1]+nroGaus(desvNuevoN[1],nroAleat4)]
            #file.write(str(nuevoN)+"\t"+str(desvNuevoN)+"\n")
            cont +=1
            #print("nuevoN: "+str(nuevoN))
        file.write("Aleatorio 1: "+str(nroAleat1)+"\t- Aleatorio 2: "+str(nroAleat2)+"\n")
        file.write("Aleatorio 1: "+str(nroAleat3)+"\t- Aleatorio 2: "+str(nroAleat4)+"\n")
        file.write(str(nuevoN)+"\t"+str(desvNuevoN)+"\n")
        if nuevoN[0]<-10 or nuevoN[0]>10 or nuevoN[1]<-10 or nuevoN[1]>10:
            print("error en nuevoN: "+str(nuevoN))
        """
        nuevoN = nuevo
        desvNuevoN = desvNuevo
        """
        fitNuevoN = fitness(nuevoN[0],nuevoN[1])
        #file.write("8) "+str(nuevoN)+"\t"+str(desvNuevoN)+"\t"+str(fitNuevoN)+"\n")
        individ.append([nuevoN[0],nuevoN[1],desvNuevoN[0],desvNuevoN[1],fitNuevoN])
    
    file.write("\nUnir mu individuos con lambda descendientes\n")
    for i in range(len(individ)):
        file.write(str(i)+") "+str(individ[i])+"\n")
    file.write("\nEscoger los mu mejores (nueva poblacion)\n")
    individ.sort(key=myFunc)
    for i in range(lamb):
        individ.pop()
    for i in range(len(individ)):
        file.write(str(i)+") "+str(individ[i])+"\n")
file.close()
