# Autor:  Carlo Corrales Delgado
# usar el Algoritmo de Colonias de Hormigas para calcular TSP

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

file = open("antColony.txt",'w')
file.write("Algoritmo Ant Colony System\n")
file.write("Parametros:\n")
file.write("- Cantidad de hormigas: 3\n")
file.write("- Una Ciudad inicial igual para todas las hormigas\n")
file.write("- Feromona inicial: 0.1\n")
file.write("- Ciudad inicial: E\n")
file.write("- Valores de Alpha, Beta, Rho, Q, q0, e_phi : alp = 1, bet = 1, p = 0.5, Q = 1, q0 = 0.5, e_phi = 0.5\n")
file.write("- Cantidad de iteraciones: 100\n")
iteraciones = 100 
alp = 1
bet = 1
individuos = 3
ciudades = 10 #6 para el 1er problema 
ciudadIni = 4 #E
p = 0.5
Q = 1.0
q0 = 0.5
e_phi = 0.5

distancia = [[],[12],[3,9],[23,18,89],[1,3,56,87],[5,41,21,46,55],[23,45,12,75,22,21],[56,5,48,17,86,76,11],[12,41,14,50,14,54,57,63],[11,27,29,42,33,81,48,24,9]]
#distancia = [[],[12],[3,9],[23,18,89],[1,3,56,87],[5,41,21,46.5,55]]  #para el 1er problema
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
            ciudadOrig = ciudad
            ciudadesRestantes.remove(ciudad)
            q = random.random()
            file.write("\nValor de q: "+str(q))
            if q < q0:
                file.write("\nRecorrido por Intensificacion\n")
                mayor = 0
                mayortn = 0
                for k in range(ciudades):
                    if k in ciudadesRestantes:
                        tn = feromonas[ciudad][k] * pow(visibilidad[ciudad][k],bet)
                        file.write(chr(65+ciudad)+"-"+chr(65+k)+": t = "+str(feromonas[ciudad][k])+" n = "+str(visibilidad[ciudad][k])+" t*n = "+str(tn)+"\n")
                        if mayortn < tn:
                            mayortn = tn
                            mayor = k
                file.write("Ciudad Siguiente: "+chr(65+mayor)+"\n")
                camino.append(ciudad)
                ciudad = mayor

            else:
                file.write("\nRecorrido por Diversificacion\n") #igual que AS
                suma = 0
                for k in range(ciudades):
                    if k in ciudadesRestantes:
                        tn = feromonas[ciudad][k] * pow(visibilidad[ciudad][k],bet)
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
                camino.append(ciudad)
                ciudad = acumCont
            ciudadDest = ciudad
            antFer = feromonas[ciudadOrig][ciudadDest]
            feromonas[ciudadOrig][ciudadDest] = (1-e_phi)*antFer + e_phi*0.1 
            feromonas[ciudadDest][ciudadOrig] = feromonas[ciudadOrig][ciudadDest]
            file.write("Actualizamos el arco "+chr(65+ciudadOrig)+"-"+chr(65+ciudadDest)+"(v):(1-e)*"+str(antFer)+" + e*0.1 = "+str(feromonas[ciudadOrig][ciudadDest])+"\n")
        camino.append(ciudadesRestantes[0])
            
        file.write("Hormiga "+str(j)+": "+chr(65+ciudadIni))
        for k in range(1,len(camino)):
            file.write("-"+chr(65+camino[k]))
        file.write("\n")
        caminosHormigas.append(camino)

    file.write("\nResumen de Hormigas:\n")
    costoCaminos = []
    mejorcosto = 99999999
    mejorj = 0
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
            mejorj = j
    file.write("-----------\n")
    file.write("Mejor Hormiga Global: "+str(mejorj)+":  ")
    for j in range(ciudades):
        file.write(chr(65+caminosHormigas[mejorj][j])+" - ")
    file.write(" Costo: "+str(mejorcosto)+"\n")
    file.write("-----------\n")

    file.write("\nNuevos valores para Feromonas\n")
    for i in range(ciudades):
        for j in range(ciudades):
            if i!=j:
                if pasoPor(i,j,mejorj,caminosHormigas):
                    evap = feromonas[i][j] * (1-p)
                    deposito = p * mejorcosto
                else:
                    evap = feromonas[i][j]
                    deposito = 0.0     
                sumTot = evap + deposito
                feromonas[i][j] = sumTot  #hay que actualizar [j][i] tambien
                feromonas[j][i] = sumTot
                file.write(chr(65+i)+"-"+chr(65+j)+": Feromona = "+str(evap)+" + "+str(deposito)+" = "+ str(sumTot)+"\n")

print("La mejor hormiga hizo un camino de "+str(mejorcosto))
file.close()
