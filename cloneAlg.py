# Autor:  Carlo Corrales Delgado
# usar el algoritmo Clone Alg para calcular solucion al problema TSA


import math
import sys
import random


def gen10(DimV):
    nums = range(DimV)
    genoma = ""
    for i in range(DimV):
        azar = random.randrange(DimV-i)
        genoma = genoma+chr(nums[azar]+65)
        nums.pop(azar)
    return genoma

def costos(distancia,antigeno):
    #print(antigeno)
    costo = 0
    for k in range(len(antigeno)-1):
        orig = ord(antigeno[k])-65
        dest = ord(antigeno[k+1])-65
        costo += distancia[orig][dest]
    return costo
        
#####


file = open("cloneAlg.txt",'w')
file.write("Algoritmo Clone Alg\n")
file.write("Parametros:\n")
file.write("- Tamano de la Poblacion P: 7\n")
file.write("- Tamano de la Poblacion F: 5\n")
file.write("- Tamano de la Poblacion PClone y PHyper: 15\n")
file.write("- Tamano de la Poblacion S: 5\n")
file.write("- Tamano de la Poblacion R: 2\n")
file.write("- Dimension del vector (anticuerpo): 10\n")
file.write("- Cantidad de iteraciones: 200\n")
iteraciones = 200 
P = 7
F = 5
S = 5
R = 2
PClone = 15
DimV = 10
ciudades = 10
#####

distancia = [[],[1],[3,1],[23,18,1],[11,3,56,1],[5,41,21,46,1],[83,20,43,44,93,1],[21,61,17,45,38,90,1],[28,95,83,50,78,92,74,1],[45,58,16,11,41,97,29,28,1]]
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


#######


file.write("\n*** Poblacion P ***\n")
anticuerpoP = []
costoP = []
for i in range(P):
    anticuerpoP.append(gen10(DimV))
    file.write(str(i)+") "+str(anticuerpoP[i])+" Costo: ")
    costoP.append(costos(distancia,anticuerpoP[i]))
    file.write(str(costoP[i])+"\n")

#iteraciones:
for i in range(iteraciones):
    file.write("\n**** Iteracion "+str(i)+" ****\n")

    file.write("\n*** Poblacion F ***\n")
    padreF = []
    costoF = []
    
    poblacionP = anticuerpoP[:]
    costopobP = costoP[:]
    for j in range(F):    
        #print(j,F,poblacionP,costopobP)
        menor = costopobP[0]
        imenor = 0
        for k in range(1,P-j):
            if menor > costopobP[k]:
                menor = costopobP[k]
                imenor = k
        padreF.append(poblacionP[imenor]) 
        costoF.append(costopobP[imenor])
        poblacionP.pop(imenor)
        costopobP.pop(imenor)
    for j in range(F):
        file.write(str(j)+") "+str(padreF[j])+" Costo: "+str(costoF[j]) + "\n")
    
    file.write("\n*** Poblacion PClone ***\n")
    clones_p = []
    for j in range(F):
        for k in range(F-j):
            clones_p.append(padreF[j])
    for j in range(PClone):
        file.write(str(j)+") "+str(clones_p[j])+"\n")

    file.write("\n*** Poblacion PHyper ***\n")
    hyper_p = []
    costoHyperP = []
    k = F
    n = F
    l = 1
    for j in range(PClone):
        intercambios = " "
        hyper_p.append(clones_p[j])
        for m in range(l): 
            orig = random.randrange(10)
            dest = orig
            while dest==orig:
                dest = random.randrange(10)
            intercambios += "["+str(orig)+","+str(dest)+"]; "
            l1 = hyper_p[j][orig]
            l2 = hyper_p[j][dest]
            hyper_p[j] = hyper_p[j][:orig] + l2 + hyper_p[j][orig+1:]
            hyper_p[j] = hyper_p[j][:dest] + l1 + hyper_p[j][dest+1:]
        k -= 1
        #file.write("k:"+str(k)+" n:"+str(n)+" l:"+str(l)+" m:"+str(m)+" j:"+str(j)+"\n")
        if k == 0:
            l += 1
            n -= 1
            k = n
            
        costoHyperP.append(costos(distancia,hyper_p[j]))
        file.write(str(j)+") "+str(clones_p[j])+intercambios+str(hyper_p[j])+" Costo: "+str(costoHyperP[j])+"\n")
    
    file.write("\n*** Poblacion S ***\n")
    poblacionS = []
    costopobS = []
    for j in range(S):
        menor = costoHyperP[0]
        imenor = 0
        for k in range(PClone-j):
            if menor > costoHyperP[k]:  
                menor = costoHyperP[k]
                imenor = k
        poblacionS.append(hyper_p[imenor])
        costopobS.append(costoHyperP[imenor])
        file.write(str(j)+") "+str(poblacionS[j])+" Costo: "+str(costopobS[j])+"\n")
        hyper_p.pop(imenor)
        costoHyperP.pop(imenor)

    file.write("\n*** Poblacion R ***\n")
    poblacionR = []
    costopobR = []
    for j in range(R):
        ind = gen10(DimV)
        cos = costos(distancia,ind)
        poblacionR.append(ind)
        costopobR.append(cos)
        file.write(str(j)+") "+str(poblacionR[j])+" Costo: "+str(costopobR[j])+"\n")

    file.write("\n*** Poblacion P ***\n")
    for j in range(P-F):  # de F
        anticuerpoP[j] = padreF[j]
        costoP[j] = costoF[j]
    for j in range(R):
        poblacionS.append(poblacionR[j])
        costopobS.append(costopobR[j])
    for j in range(F):
        menor = poblacionS[0]
        imenor = 0
        for k in range(S+R-j):  # de S y R
            if menor > costopobS[k]:
                menor = costopobS[k]
                imenor = k
        anticuerpoP[P-F+j] = poblacionS[imenor]
        costoP[P-F+j] = costopobS[imenor]
        poblacionS.pop(imenor)
        costopobS.pop(imenor)
    
    for j in range(P):
        file.write(str(j)+") "+anticuerpoP[j]+" Costo: "+str(costoP[j])+"\n")

file.close()
