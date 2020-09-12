# Autor:  Carlo Corrales Delgado
# usar la Programacion Evolutiva para crear Maquinas de estado finito
import math
import sys
import random

def buscaEi(pool):
    for i in range(0,len(pool),7):
        if pool[i]=='2':
            return i
    return -2
def fitness(pool,secIni,sa):
    fi = 0
    for i in range(len(secIni)-1):
        if sa[i]==secIni[i+1]:
            fi +=1
    return 1.0*fi/(len(secIni)-1)
def salida(pool,secIni):
    if len(pool)<35:
        print("error en pool: "+str(pool))
    sa = ''
    #los estados estan en las pos 0,7,14,21,28
    estadoIni = buscaEi(pool)
    for i in range(len(secIni)):
        if estadoIni<0:
            print("estadoIni = "+str(estadoIni)+" en i: "+str(i)+" pool:"+str(pool))
        elif pool[estadoIni]=='0':
            print("Estado desactivado: "+str(pool[estadoIni:estadoIni+7]))
        #else:
        if (secIni[i])==(pool[estadoIni+1]):
            #encontre la entrada, la salida esta en +2
            sa = sa+pool[estadoIni+3]
            estadoAct = pool[estadoIni+5]
        else: #secIni[i]==pool[estadoIni+2]
            sa = sa+pool[estadoIni+4]
            estadoAct = pool[estadoIni+6]
        if estadoAct=='A':
            estadoIni=0
        elif estadoAct=='B':
            estadoIni=7
        elif estadoAct=='C':
            estadoIni=14
        elif estadoAct=='D':
            estadoIni=21
        elif estadoAct=='E':
            estadoIni=28
        else:
            estadoIni=-1
    return sa

def myFunc(e):
    return e[2]
#####

file = open("MaqEstadoFin.txt",'w')
file.write("Programacion Evolutiva\n")
file.write("Parametros:\n")
file.write("- Cantidad de individuos: 8 a 16\n")
file.write("- Cantidad maxima de estados: 5\n")
file.write("- Cantidad de iteraciones: 100\n")
iteraciones = 100 
individuos = 8
estados = 5
secIni = '0111001010011100101001110010100111001010'

#poblacion Inicial:
file.write("\nPoblacion inicial\n")
pool = []
for i in range(individuos):
    poblador = ''
    yaInic = False
    for j in range(estados):
        #el 1ro solo debe haber un 2 de entre los 5 estados
        if yaInic:
            prim = random.randrange(2)
        elif j<(estados-1):
            prim = random.randrange(3)
            if prim==2:
                yaInic = True
        else:
            prim = 2
        if prim==0:
            prim = 1  #inicialmente pondremos todos los estados activos, ningun inactivo
        poblador = poblador + str(prim)
        #el 2do y 3ro deben ser 0 y 1 en cualquier orden
        segu = random.randrange(2)
        if segu==0:
            terc = 1
        else:
            terc = 0
        poblador = poblador + str(segu) + str(terc)
        #el 4to y 5to son 0 o 1 al azar
        poblador = poblador + str(random.randrange(2)) + str(random.randrange(2)) 
        #el 6to y 7mo son estados al azar
        poblador = poblador + chr(65+random.randrange(estados)) + chr(65+random.randrange(estados))
    pool.append(poblador)
    file.write(str(i)+") "+str(pool[i])+"\n")

#calcular la aptitud para cada individuo:
file.write("\nCalcular la aptitud para cada individuo\n")
poolValFun = []
saliPool = []
AscPool = []
for i in range(individuos):
    saliPool.append(salida(pool[i],secIni))
    poolValFun.append(fitness(pool[i],secIni,saliPool[i]))
    file.write(str(i)+") "+str(pool[i])+" - "+str(secIni)+" - "+str(saliPool[i]+" - "+str(poolValFun[i])+"\n"))
    AscPool.append([pool[i] , saliPool[i] , poolValFun[i]])

#iteraciones:
for i in range(iteraciones):
    file.write("\n**** Iteracion "+str(i)+" ****\n")
    file.write("Proceso de Mutacion\n")
    descPool = []
    for j in range(individuos):
        file.write("\nMutacion "+str(j)+"\n")
        file.write(pool[j]+"\n")
        Aleat = random.random()
        file.write("Aleatorio: "+str(Aleat)+"\n")
        if Aleat<=0.1: 
            file.write("Desactivar un estado\n") #cambiar las transiciones que llegan a este, redirigirlos a otros
            nroAlea = random.randrange(estados)
            while pool[j][nroAlea*7]=='2':
                nroAlea = random.randrange(estados)
            file.write("Estado seleccionado: "+chr(65+nroAlea)+"\n")
            file.write("Chequeando las transiciones que llegaban a este estado...\n")
            newpool = pool[j]
            for k in range(estados):
                if newpool[k*7+5]==chr(65+nroAlea):
                    newEstado = nroAlea
                    while newEstado==nroAlea:
                        newEstado = random.randrange(estados)
                    newpool = newpool[:k*7+5] + chr(65+newEstado) + newpool[k*7+6:]
                if newpool[k*7+6]==chr(65+nroAlea):
                    newEstado = nroAlea
                    while newEstado==nroAlea:
                        newEstado = random.randrange(estados)
                    newpool = newpool[:k*7+6] + chr(65+newEstado) + newpool[k*7+7:]
            newpool = newpool[:nroAlea*7] + '0' + newpool[nroAlea*7+1:]
            if len(newpool)<35:
                print("Encontre un newpool errado: "+str(newpool)+" en pool[j]: "+str(pool[j]))
        
        elif Aleat<=0.3: 
            file.write("Cambiar estado inicial\n") #buscar un 1 y volverlo 2
            estadoIni = buscaEi(pool[j])/7
            file.write("Estado inicial: "+chr(65+estadoIni)+"\n")
            nroAlea = estadoIni
            while nroAlea==estadoIni:
                nroAlea = random.randrange(estados)
            file.write("Nuevo estado inicial: "+chr(65+nroAlea)+"\n")
            newpool = pool[j][:estadoIni*7] + '1' + pool[j][estadoIni*7+1:] 
            newpool = newpool[:nroAlea*7] + '2' + newpool[nroAlea*7+1:]
            
        elif Aleat<=0.5: 
            file.write("Cambiar simbolo de entrada\n")  #intercambiar 01 por 10
            nroAlea = random.randrange(estados)
            file.write("Estado seleccionado: "+chr(65+nroAlea)+"\n")
            if pool[j][nroAlea*7+1:nroAlea*7+3]=='01':
                dos = '10'
            else:
                dos = '01'
            newpool = pool[j][:nroAlea*7+1] + dos + pool[j][nroAlea*7+3:]

        elif Aleat<=0.7: 
            file.write("Cambiar simbolo de salida\n") 
            nroAlea = random.randrange(estados)
            file.write("Estado seleccionado: "+chr(65+nroAlea)+"\n")
            file.write("Cambio Salida: "+pool[j][nroAlea*7+3]+"\n")
            uno = pool[j][nroAlea*7+3]
            if uno=='0':
                uno = '1'
            else:
                uno = '0'
            newpool = pool[j][:nroAlea*7+3] + uno + pool[j][nroAlea*7+4:]
            
        elif Aleat<=0.9: 
            file.write("Cambiar estado de salida\n")
            nroAlea = random.randrange(estados)
            file.write("Estado seleccionado: "+chr(65+nroAlea)+"\n")
            file.write("Cambio Estado Salida: "+pool[j][nroAlea*7+5]+"\n")
            uno = pool[j][nroAlea*7+5]
            letraAleat = chr(65+random.randrange(estados))
            newpool = pool[j][:nroAlea*7+5] + letraAleat + pool[j][nroAlea*7+6:]

        else: 
            file.write("Activar un estado\n")
            nroAlea = random.randrange(estados)
            file.write("Estado seleccionado: "+chr(65+nroAlea)+"\n")
            file.write("Activando Estado :"+pool[j][nroAlea*7]+"\n")
            if pool[j][nroAlea*7]=='0':
                newpool = pool[j][:nroAlea*7] + '1' + pool[j][nroAlea*7+1:]
            else: 
                newpool = pool[j]
        file.write(str(newpool)+"\n")
        if len(newpool)<35:
            print("len(newpool) < 35 en "+str(pool[j])+" newpool: "+str(newpool))
        descPool.append(newpool)

    file.write("\nDescendientes\n")
    descPoolValFun = []
    descSaliPool = []
    DesPool = []
    for j in range(individuos):
        descSaliPool.append(salida(descPool[j],secIni))
        descPoolValFun.append(fitness(descPool[j],secIni,descSaliPool[j]))
        file.write(str(j)+") "+str(descPool[j])+" - "+str(secIni)+" - "+str(descSaliPool[j])+" - "+str(descPoolValFun[j])+"\n")
        DesPool.append([descPool[j] , descSaliPool[j] , descPoolValFun[j]])

    file.write("Mejores Ascendentes\n")
    AscPool.sort(key=myFunc,reverse=True)
    for j in range(individuos/2):
        file.write(str(j)+") "+str(AscPool[j][0])+" - "+str(secIni)+" - "+str(AscPool[j][1])+" - "+str(AscPool[j][2])+"\n")
        AscPool.pop()
    file.write("Mejores Descendientes\n")
    DesPool.sort(key=myFunc,reverse=True)
    for j in range(individuos/2):
        file.write(str(j)+") "+str(DesPool[j][0])+" - "+str(secIni)+" - "+str(DesPool[j][1])+" - "+str(DesPool[j][2])+"\n")
        AscPool.append(DesPool[j])
    file.write("Nueva poblacion\n")
    for j in range(len(AscPool)):
        file.write(str(j)+") "+str(AscPool[j][0])+" - "+str(secIni)+" - "+str(AscPool[j][1])+" - "+str(AscPool[j][2])+"\n")
       
file.close()
