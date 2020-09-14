# Autor:  Carlo Corrales Delgado
# usar el Algoritmo del Sistema de Hormigas para calcular TSP

import math
import sys
import random

def pasoPor(i,j,k,caminosHormigas): #paso por i,j la hormiga k
    for m in range(ciudades-1):
        if (caminosHormigas[k][m]==i and caminosHormigas[k][m+1]==j) or (caminosHormigas[k][m]==j and caminosHormigas[k][m+1]==i):
            return True
    return False
def truncate(nro,dec):
    pos = pow(10.0,dec)
    return math.trunc(pos*nro)/pos

#####

file = open("antSystem.txt",'w')
file.write("Algoritmo Ant System\n")
file.write("Parametros:\n")
file.write("- Cantidad de hormigas: 10\n")
file.write("- Una Ciudad inicial igual para todas las hormigas\n")
file.write("- Feromona inicial: 0.1\n")
file.write("- Ciudad inicial: D\n")
file.write("- Valores de Alpha, Beta, Rho y Q: alp = 1, bet = 1, p = 0.01, Q = 1\n")
file.write("- Cantidad de iteraciones: 100\n")
iteraciones = 100 
alp = 1
bet = 1
individuos = 10 #5 para el 1er problema
ciudades = 10 #5 para el 1er problema
ciudadIni = 3 #D
p = 0.01
Q = 1.0

distancia = [[],[12],[3,9],[23,18,89],[1,3,56,87],[5,41,21,46,55],[23,45,12,75,22,21],[56,5,48,17,86,76,11],[12,41,14,50,14,54,57,63],[11,27,29,42,33,81,48,24,9]]
#distancia = [[],[12],[3,9],[23,18,89],[1,3,56,87]]  #para el 1er problema
for i in range(ciudades):
    distancia[i].append(0)
    for j in range(i+1,ciudades):
        distancia[i].append(distancia[j][i])
file.write("\nMatriz de distancias:\n")
for i in range(ciudades):
    file.write("\t"+chr(65+i))
file.write("\n")
for i in range(ciudades):
    file.write(chr(65+i)+"\t"+str(distancia[i])+"\n")

#matriz de visibilidad:
visibilidad = []
file.write("\nmatriz de visibilidad\n")
for i in range(ciudades):
    file.write("\t"+chr(65+i))
file.write("\n")
for i in range(ciudades):
    vis = []
    for j in range(ciudades):
        if i==j:
            vis.append(0)
        else:
            visnro = truncate(1.0/distancia[i][j],5)
            vis.append(visnro)
    visibilidad.append(vis)

for i in range(ciudades):
    file.write(chr(65+i)+"\t"+str(visibilidad[i])+"\n")

#matriz de Feromonas:
feromonas = []
file.write("\nmatriz de feromonas\n")
for i in range(ciudades):
    file.write("\t"+chr(65+i))
file.write("\n")
for i in range(ciudades):
    fer = []
    for j in range(ciudades):
        if i==j:
            fer.append(0.0)
        else:
            fernro = truncate(0.1,5)
            fer.append(fernro)
    feromonas.append(fer)

for i in range(ciudades):
    file.write(chr(65+i)+"\t"+str(feromonas[i])+"\n")

#iteraciones:
for i in range(iteraciones):
    file.write("\n**** Iteracion "+str(i)+" ****\n")

    #matriz de visibilidad:
    file.write("\nmatriz de visibilidad\n")
    for i in range(ciudades):
        file.write("\t"+chr(65+i))
    file.write("\n")
    for i in range(ciudades):
        file.write(chr(65+i)+"\t"+str(visibilidad[i])+"\n")

    #matriz de Feromonas:
    file.write("\nmatriz de feromonas\n")
    for i in range(ciudades):
        file.write("\t"+chr(65+i))
    file.write("\n")
    for i in range(ciudades):
        file.write(chr(65+i)+"\t"+str(feromonas[i])+"\n")

    caminosHormigas = []
    for j in range(individuos):
        file.write("\nHormiga "+str(j)+"\n")
        camino = []
        ciudad = ciudadIni
        file.write("Ciudad Inicial: "+chr(65+ciudad)+"\n")
        ciudadesRestantes = range(ciudades)
        while len(ciudadesRestantes)>1:
            suma = 0
            ciudadesRestantes.remove(ciudad)
            #print(ciudadesRestantes)
            for k in range(ciudades):
                if k in ciudadesRestantes:
                    #file.write("probando..."+str(feromonas)+" ciudad: "+str(ciudad)+ " k: "+str(k)+"\n")
                    tn = pow(feromonas[ciudad][k],alp)*pow(visibilidad[ciudad][k],bet)
                    file.write(chr(65+ciudad)+"-"+chr(65+k)+": t = "+str(feromonas[ciudad][k])+" n = "+str(visibilidad[ciudad][k])+" t*n = "+str(tn)+"\n")
                    suma += tn
            file.write("Suma: "+str(suma)+"\n")
            probab = []
            for k in range(ciudades):
                if k in ciudadesRestantes:
                    if suma!=0:
                        prob = pow(feromonas[ciudad][k],alp)*pow(visibilidad[ciudad][k],bet)/suma
                    else:
                        prob = 0.0
                    file.write(chr(65+ciudad)+"-"+chr(65+k)+": prob = "+str(prob)+"\n")
                    probab.append(prob)
                else:
                    probab.append(0.0)
            Aleat = random.random()
            file.write("Nro aleat para la probabilidad: "+str(Aleat)+"\n")
            acum = 0
            acumCont = 0
            for k in range(ciudades):
                if acum<Aleat:
                    acum += probab[k]
                    acumCont +=1
                else:
                    break
            acumCont -=1
            file.write("Ciudad Siguiente: "+chr(65+acumCont)+"\n")
            #print("Ciudad a elim: "+str(ciudad))
            camino.append(ciudad)
            ciudad = acumCont
        camino.append(ciudadesRestantes[0])
            
        file.write("Hormiga "+str(j)+": "+chr(65+ciudadIni))
        for k in range(1,len(camino)):
            file.write("-"+chr(65+camino[k]))
        file.write("\n")
        caminosHormigas.append(camino)

    file.write("\nResumen de Hormigas:\n")
    costoCaminos = []
    mejorcosto = 999999
    for j in range(individuos):
        file.write("Hormiga "+str(j)+": (")
        costo = 0
        for k in range(ciudades-1):
            file.write(chr(65+caminosHormigas[j][k])+"-")
            costo += distancia[caminosHormigas[j][k]][caminosHormigas[j][k+1]]
        file.write(chr(65+caminosHormigas[j][ciudades-1]))
        file.write(") - Costo: "+str(costo)+"\n")
        costoCaminos.append(costo)
        if mejorcosto > costo:
            mejorcosto = costo

    file.write("\nNuevos valores para Feromonas\n")
    for i in range(individuos):
        for j in range(individuos):
            if i!=j:
                evap = feromonas[i][j]*(1-p)
                file.write(chr(65+i)+"-"+chr(65+j)+": Feromona = "+str(evap))
                sumTot = evap
                for k in range(individuos):
                    if pasoPor(i,j,k,caminosHormigas):
                        costoIf = Q/costoCaminos[k] 
                    else:
                        costoIf = 0.0
                    file.write(" + "+str(costoIf))
                    sumTot += costoIf
                file.write(" = "+str(sumTot)+"\n")
                feromonas[i][j] = sumTot

print("La mejor hormiga hizo un camino de "+str(mejorcosto))
file.close()