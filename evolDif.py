# Autor:  Carlo Corrales Delgado
# usar la Evolucion Diferencial para calcular el valor minimo de la funcion f(x,y,a,b) = (x + 2y -7)2 + (2x + y - 5)2 + (a + 2b -7)2 + (2a + b - 5)2
# con restricciones -10 <= x <= 10      and     -10 <= y <= 10     and   -10 <= a <= 10      and     -10 <= b <= 10
import math
import sys
import random

def fitness(x,y,a,b):
    return (x + 2*y -7)**2 + (2*x + y - 5)**2 + (a + 2*b -7)**2 + (2*a + b - 5)**2

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

file = open("EvolucDiferencial.txt",'w')
file.write("Evolucion Diferencial\n")
file.write("Parametros:\n")
file.write("- Cantidad de individuos: 10\n")
file.write("- Cantidad de dimensiones: 4\n")
file.write("- Constante de mutacion (F): 0.8\n")
file.write("- Constante de cruzamiento (CR): 0.5\n")
file.write("- Cantidad de iteraciones: 200\n")
iteraciones = 200 
individuos = 10
F = 0.8
CR = 0.5

#poblacion Inicial:
file.write("\nPoblacion inicial\n")
pool = []
for i in range(individuos):
    pool.append([random.random()*20 - 10 , random.random()*20 - 10 , random.random()*20 - 10 , random.random()*20 - 10])
    file.write(str(i)+") "+str(pool[i])+"\n")

#calcular la aptitud para cada individuo:
file.write("\nCalcular la aptitud para cada individuo\n")
poolValFun = []
individ = []
for i in range(individuos):
    poolValFun.append(fitness(pool[i][0],pool[i][1],pool[i][2],pool[i][3]))
    file.write(str(i)+") "+str(pool[i])+"\t"+str(poolValFun[i])+"\n")
    individ.append([pool[i][0],pool[i][1],pool[i][2],pool[i][3],poolValFun[i]])

#iteraciones:
for i in range(iteraciones):
    file.write("\n**** Iteracion "+str(i)+" ****\n")
    for j in range(individuos):
        file.write("**** Vector "+str(j)+"***\n")
        file.write("Mutacion\n")
        xm = j
        while xm==j:
            xm = random.randrange(individuos)
        xk = xm
        while xk==xm or xk==j:
            xk = random.randrange(individuos)
        xl = xk
        while xl==xk or xl==xm or xl==j:
            xl = random.randrange(individuos)
        file.write("xm = "+str(xm)+"; xk = "+str(xk)+"; xl = "+str(xl)+"\n")
        xk_xl = [pool[xk][0]-pool[xl][0],pool[xk][1]-pool[xl][1],pool[xk][2]-pool[xl][2],pool[xk][3]-pool[xl][3]]
        file.write("xk - xl (Vector de diferencias): "+str(xk_xl)+"\n")
        F = random.random()*2
        Fxk_xl = [F*xk_xl[0],F*xk_xl[1],F*xk_xl[2],F*xk_xl[3]]
        file.write("F*(xk - xl) (Vector de diferencias ponderado): "+str(Fxk_xl)+"\n")
        xm_Fxk = [pool[xm][0]+Fxk_xl[0],pool[xm][1]+Fxk_xl[1],pool[xm][2]+Fxk_xl[2],pool[xm][3]+Fxk_xl[3]]
        file.write("xm + F*(xk - xl) (Vector Mutado): "+str(xm_Fxk)+"\n")
        file.write("Cruzamiento\n")
        cruzam = []
        for k in range(4):
            aleat = random.random()
            file.write(str(aleat)+"\n")
            if aleat<CR:
                cruzam.append(xm_Fxk[k])
            else:
                cruzam.append(pool[j][k])
        fitCruzam = fitness(cruzam[0],cruzam[1],cruzam[2],cruzam[3])
        file.write("Vector trial: "+str(cruzam)+" - fitness: "+str(fitCruzam)+"\n")
        if poolValFun[j]<fitCruzam:
            file.write("El vector target continua en la siguiente poblacion\n")
        else:
            file.write("El vector target es reemplazado por el vector trial en la sig poblacion\n")
            pool[j] = cruzam
            poolValFun[j] = fitCruzam
            individ[j] = [cruzam[0],cruzam[1],cruzam[2],cruzam[3],fitCruzam]

    file.write("**** Nueva poblacion ****\n")
    for i in range(individuos):
        file.write(str(i)+") "+str(individ[i])+"\n")

file.close()
