# Autor:  Carlo Corrales Delgado
# usar el algoritmo DCA para calcular el algoritmo de celulas dentriticas


import math
import sys
import random
    

def separa(linea):
    dato = []
    pos = 0 
    while(True):
        nro = ""
        while len(linea)>pos and linea[pos]!=',' and linea[pos]!='?':
            nro += linea[pos]
            pos +=1
        #print(dato)
        if len(nro)>0:
            dato.append(int(nro))
        if len(linea)==pos:
            return dato
        if linea[pos]=='?':
            return False
        pos +=1


#####

file = open("DCA.txt",'w')
file.write("Algoritmo DCA\n")
file.write("Parametros:\n")
file.write("- Base de datos: UCI Wisconsin Breast Cancer (sin valores faltantes)\n")
file.write("- PAMP y SS: Atributo CT\n")
file.write("- DS: Atributos CS, CH, BN y NN\n")
file.write("- Limite de migracion: 50.0\n")
file.write("- Cantidad de Iteraciones: 10000\n")
file.write("- at: 0.3\n")

iteraciones = 10000 
lim = 50.0
at = 0.3

#######

arch = open("breast-cancer-wisconsin.data",'r')
file.write("\n*** Datos ***\n")
lines = arch.readlines()
cont = 0
CTsum = 0
CSsum = 0    
CHsum = 0
BNsum = 0
NNsum = 0
basedato = []
for i in lines:
    dato = separa(i)
    #print(dato)
    if dato:
        file.write(str(dato[0])+"\t\t")
        for j in range(1,11):
            file.write(str(dato[j])+"\t")
        file.write("\n")
        basedato.append(dato)
        #id,CT,CS,CH,MA,SE,BN,BC,NN,MM,clase
        cont +=1
        CTsum += dato[1]
        CSsum += dato[2]    
        CHsum += dato[3]
        BNsum += dato[6]
        NNsum += dato[8]
        
bd2 = basedato[:]
bd2.sort(key=lambda x:x[1])
CTmed = bd2[len(bd2)/2][1]
bd2 = basedato[:]
bd2.sort(key=lambda x:x[2])
CSmed = bd2[len(bd2)/2][2]
bd2 = basedato[:]
bd2.sort(key=lambda x:x[3])
CHmed = bd2[len(bd2)/2][3]
bd2 = basedato[:]
bd2.sort(key=lambda x:x[6])
BNmed = bd2[len(bd2)/2][6]
bd2 = basedato[:]
bd2.sort(key=lambda x:x[8])
NNmed = bd2[len(bd2)/2][8]
file.write("Total :"+ str(len(basedato))+"\n")

file.write("\n*** Estadisticas ***\n")
file.write("Nombre: CT\t Mediana: "+str(CTmed)+"\t Media: "+str(1.0*CTsum/cont)+"\n")
file.write("Nombre: CS\t Mediana: "+str(CSmed)+"\t Media: "+str(1.0*CSsum/cont)+"\n")
file.write("Nombre: CH\t Mediana: "+str(CHmed)+"\t Media: "+str(1.0*CHsum/cont)+"\n")
file.write("Nombre: BN\t Mediana: "+str(BNmed)+"\t Media: "+str(1.0*BNsum/cont)+"\n")
file.write("Nombre: NN\t Mediana: "+str(NNmed)+"\t Media: "+str(1.0*NNsum/cont)+"\n")

file.write("\n*** Signal Data Set (PAMP, Safe signal, Danger Signal) ***\n")
PampSsDs = []
for i in basedato:
    if i[1] > CTmed:
        pamp = 0.000000
        ss = abs(1.0*CTsum/cont - i[1])
    else:
        pamp =abs(1.0*CTsum/cont - i[1])
        ss = 0.000000
    ds = (abs(1.0*CSsum/cont-i[2]) + abs(1.0*CHsum/cont-i[3]) + abs(1.0*BNsum/cont-i[6]) + abs(1.0*NNsum/cont-i[8]))/4
    file.write(str(i[0])+"\t\t"+str(pamp)+"\t\t\t"+str(ss)+"\t\t\t"+str(ds)+"\n")
    PampSsDs.append([pamp,ss,ds]) 

file.write("\n*** Pesos para cada senal ***\n")
pesos= [[2.0,0.0,2.0],[1.0,0.0,1.0],[0.5,1.2,0.5]]
file.write("2.0\t 0.0\t 2.0\n")
file.write("1.0\t 0.0\t 1.0\n")
file.write("0.5\t 1.2\t 0.5\n")

#Iteraciones
MCAV = []
for i in range(iteraciones):
    file.write("\n****  Iteracion "+str(i)+" ****\n")
    acumCSM = 0
    acumsmDC = 0
    acummDC = 0
    dataCSM = []
    while acumCSM < lim:
        azar = random.randrange(len(PampSsDs))
        acumCSM += pesos[0][0]*PampSsDs[azar][0] + pesos[0][1]*PampSsDs[azar][1] + pesos[0][2]*PampSsDs[azar][2]
        acumsmDC += pesos[1][0]*PampSsDs[azar][0] + pesos[1][1]*PampSsDs[azar][1] + pesos[1][2]*PampSsDs[azar][2]
        acummDC += pesos[2][0]*PampSsDs[azar][0] + pesos[2][1]*PampSsDs[azar][1] + pesos[2][2]*PampSsDs[azar][2]
        dataCSM.append(basedato[azar][0])
    file.write("Acumulado CSM: "+str(acumCSM)+" Acumulado smDC: "+str(acumsmDC)+" Acumulado mDC: "+str(acummDC)+"\n")
    
    if acumsmDC > acummDC:
        clase = 2.0 #"sm"
    else:
        clase = 4.0 #"m" 
    file.write("Clase: "+str(clase)+"\n")
    for j in range(len(dataCSM)):
        file.write(str(dataCSM[j])+" ")
        encontrado = False
        for k in range(len(MCAV)):
            if MCAV[k][0]==dataCSM[j]:
                MCAV[k][1] +=1
                if clase==4.0:
                    MCAV[k][2] +=1
                encontrado = True
        if not encontrado:
            if clase==4.0:
                cl = 1
            else:
                cl = 0
            MCAV.append([dataCSM[j],1,cl,0]) #id,nb-antigen,nb-mature,MCAV  
    file.write("\n")

file.write("\n**** Clasificacion final ****\n")
cl4 = 0 
cl2 = 0
for i in range(len(MCAV)):
    MCAV[i][3] = 1.0*MCAV[i][2]/MCAV[i][1]
    file.write(str(MCAV[i][0])+"\t"+str(MCAV[i][1])+"\t"+str(MCAV[i][2])+"\t"+str(MCAV[i][3])+"\t")
    if MCAV[i][3] > at:
        file.write("Clase 4.0\n")
        cl4 +=1
    else:
        file.write("Clase 2.0\n")
        cl2 +=1

file.write("\nTotal Clase 4.0: "+str(cl4)+"\n")
file.write("Total Clase 2.0: "+str(cl2)+"\n")
file.write("Gran Total: "+str(cl2+cl4)+"\n")


arch.close()
file.close()
