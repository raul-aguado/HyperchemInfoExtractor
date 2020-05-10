import os
import sys

#Generar una lista llamada mylines
mylines = []

#Guardar cada linea como un elemento de la lista
with open ('TS.log', 'rt') as myfile: 
    for myline in myfile:                
        mylines.append(myline)

#Preguntar que parte del archivo hay que buscar
print("::::::::::::::::::::::::::::::::::::")
print()
print("1. Simetria de la molecula")
print("2. Energias")
print("3. Análisis de Orbitales Moleculares")
print("4. ZPE (Zero Point Energy) de vibracion")
print()
print("::::::::::::::::::::::::::::::::::::")
print()
o=int(input("Indica la opcion a buscar: "))
print()
print()
print()

#Se define la cadena a buscar para 
if o==1:
    cadena="MOLECULAR POINT GROUP\n"
    
else:
    if o==2:
        cadena="ENERGIES AND GRADIENT\n"
    if o==4:
        cadena="         ==== Zero Point Energy of Vibration in kcal / mol ====\n"
#Para buscar el analisis de orbitales se debe saber si se deben bucar dos tablas (correlacion MP2 activada) o si se debe buscar una sola
    if o==3:
        print("¿Está la correlacion MP2 activada?")
        print("1. Si")
        print("2. No")
        print()
        MP2=int(input())
        print(MP2)
        if MP2==1:
            cadena="                    Alpha Eigenvalues(a.u.) and Eigenvectors\n"
        elif MP2==2:
            cadena="                       Eigenvalues(a.u.) and Eigenvectors\n"
        else:
            exit

#Indicar el metodo computacional utilizado
print()
print("::::::::::::::::::::::::::::::::::::::::::::::")
print(":::::::::::::Parámetros empleados:::::::::::::")
print("::::::::::::::::::::::::::::::::::::::::::::::")
print()
print(mylines[1])
print("::::::::::::::::::::::::::::::::::::::::::::::")
print()
print()

#Guardar cada linea como un elemento de la lista
with open ('prueba.txt', 'rt') as myfile: 
    for myline in myfile:                
        mylines.append(myline)

#Definir el parametro que nos va a ayudar a buscar lineas
n=1

#Comprar la linea n con un valor determinado de cadena de texto
while mylines[n]!=cadena:
    n=n+1
else:
    print(mylines[n])
    n=n+1
    if o==1:
        m=n+1
        while n<m:
            n=n+1
            print(mylines[n])
        else:
            exit
    if o==2:
        m=n+8
        while n<m:
            n=n+1
            print(mylines[n])
        else:
            exit
            
    if o==3 and mylines[n]!=cadena:
        while mylines[n]!="                        Full Mulliken population analysis\n":
            print(mylines[n])
            n=n+1
        else:
            exit
            
    if o==4 and mylines[n]!=cadena:
        m=n+2
        while n<m:
            n=n+1
            print(mylines[n])
        else:
            exit
