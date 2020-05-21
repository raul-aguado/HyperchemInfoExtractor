import os
from os import scandir, getcwd
import sys
import time

#Definir la funcion que va a indexar los archivos
def indexador_archivos(ruta=getcwd()):
    return[arch.name for arch in scandir(ruta) if arch.is_file()]

#La promosió 1
def banner():
    print("########################################################")
    print("Resumen generado mediante Hyperchem Info Extractor 2.2.3")
    print()
    print("Creado por Raul Aguado                              2020")
    print("########################################################")
    print()
    print()

#Inicio del programa
banner()


#Preguntar por la ruta que hay que comprobar
print("¿Analizar las energías?")
opt1=str(input("y/n... "))
while str(opt1)!="y" or "n":
    if opt1=="y":
        bo1=1
        break
    if opt1=="n":
        bo1=0
        break

print("¿Incluir la ZPE?")
opt2=str(input("y/n... "))
while str(opt2)!="y" or "n":
    if opt2=="y":
        bo2=1
        break
    if opt2=="n":
        bo2=0
        break

print("¿Analizar la simetria molecular?")
opt3=str(input("y/n... "))
while str(opt3)!="y" or "n":
    if opt3=="y":
        bo3=1
        break
    if opt3=="n":
        bo3=0
        break

#Se pide la ruta que se debe comprobar y se pregunta si se quiere renombrar el archivo de salida de datos
print()
ruta=input("Introduce la ruta para comprobar: ")
print()
print("¿Quieres seleccionar un nombre para tu archivo de salida?")
output_opt=""
while str(output_opt)!="y" or "n":
    output_opt=str(input("y/n... "))
    if output_opt=="y":
        print()
        nom_resumen=(input("Nombre del output... "))
        break
    if opt3=="n":
        nom_resumen="Resumen Hyperchem"
        break
print()
print("Buscando archivos de registro en la ruta selecionada...")
print()
time.sleep(1)
print()

#Se crea el archivo que va a contener nuestro resumencito
file = open(ruta+"/" + nom_resumen + ".txt", "w")

#Se indexan todos los archivos de la carpeta mediante la funcion definida antes
filepaths = (indexador_archivos(ruta))
num_archivos=len(filepaths)
print("En la carpeta existen " + str(num_archivos) + " arhivos")
time.sleep(1)

#La promosió 2
file.write("########################################################" + os.linesep)
file.write("Resumen generado mediante Hyperchem Info Extractor 2.2.3" + os.linesep)
file.write(os.linesep)
file.write("Creado por Raul Aguado                             2020" + os.linesep)
file.write("########################################################" + os.linesep)
file.write(os.linesep)

#Se crea la lista que va a contener las lineas del archivo que se esta analizando (fp)
mylines=[]
for fp in filepaths:
    # Split the extension from the path and normalise it to lowercase.
    ext = os.path.splitext(fp)[-1].lower()
    ruta_completa=ruta+"/"+fp

    # Si el archivo es un log, se analiza
    if ext == ".log":
        print()
        print(fp+" es un archivo .log!")
        print("Analizando " + fp + "...")
        print()
        mylines=[]

        with open(ruta_completa, 'rt') as myfile:
            for myline in myfile:
                mylines.append(myline)
            myfile.close()

            num_lineas=len(mylines)
            print("El archivo tiene " + str(num_lineas) + " lineas")
            print()

            file.write("==========" + os.linesep)
            file.write(fp + os.linesep)
            file.write("==========" + os.linesep)

            if bo1==1:
                try:
                    n=0
                    while mylines[n]!="ENERGIES AND GRADIENT\n":
                        n=n+1
                    else:
                        m=n+8
                        n=n+1
                        while n<m:
                            file.write(mylines[n] + os.linesep)
                            n=n+1
                except:
                    print("No se ha encontrado ningun dato sobre la energía")
                    file.write("No se ha encontrado ningun dato sobre la energía"+ os.linesep)
                    print("Continuando...")
                    print()

            if bo2==1:
                try:
                    n=0
                    while mylines[n]!="         ==== Zero Point Energy of Vibration in kcal / mol ====\n":
                        n=n+1
                    else:
                        file.write("Zero point energy: "+mylines[n+2] + " (kcal/mol)" + os.linesep)
                except:
                    print("No se ha encontrado ningun dato sobre ZPE")
                    file.write("No se ha encontrado ningun dato sobre ZPE"+ os.linesep)
                    print("Continuando...")
                    print()
            if bo3==1:
                try:
                    n=0
                    while mylines[n]!="MOLECULAR POINT GROUP\n":
                        n=n+1
                    else:
                        m=n+3
                        n=n+1
                        while n<m:
                            file.write(mylines[n] + os.linesep)
                            n=n+1
                except:
                    print("No se ha encontrado ningun dato de simetria molecular")
                    file.write("No se ha encontrado ningun dato de simetria molecular"+ os.linesep)
                    print("Continuando...")
                    print()
        time.sleep(4)

    #Si el archivo es un .txt podria contener informacion de Hyperchem
    elif ext == ".txt":
        #Con la siguiente linea se evita que el programa analice el propio resumen
        if fp!=(nom_resumen + ".txt"):
            print(fp+" es un archivo de texto!")
            print()
            print("Contiene " + fp + " datos de Hyperchem?")
            print()
            res=input("y/n: ")

            if res=="y":
                ruta_completa=ruta+"/"+fp
                with open (ruta_completa, 'rt') as myfile:
                    for myline in myfile:
                        mylines.append(myline)
                num_lineas=len(mylines)
                print("El archivo tiene " + str(num_lineas) + " lineas")
                print()
                n=1
                file.write("==========" + os.linesep)
                file.write(fp + os.linesep)
                file.write("==========" + os.linesep)

                if bo1==1:
                    n=0
                    while mylines[n]!="ENERGIES AND GRADIENT\n":
                        n=n+1
                    else:
                        m=n+8
                        n=n+1
                        while n<m:
                            print(n)
                            file.write(mylines[n] + os.linesep)
                            n=n+1
                if bo2==1:
                    n=0
                    while mylines[n]!="         ==== Zero Point Energy of Vibration in kcal / mol ====\n":
                        n=n+1
                    else:
                        file.write("Zero point energy: "+mylines[n+2] + os.linesep)
                if bo3==1:
                    n=0
                    while mylines[n]!="MOLECULAR POINT GROUP\n":
                        n=n+1
                    else:
                        m=n+3
                        n=n+1
                        while n<m:
                            file.write(mylines[n] + os.linesep)
                            n=n+1
                time.sleep(4)

            else:
                print("No se ha analizado " + fp)
                print()

    #Si el archivo no es ni .txt ni .log no contiene informacion de Hyperchem
    else:
        print(fp + " no contiene datos de Hyperchem")
        print("No se ha analizado " + fp)
        print()
        time.sleep(2)

file.close()
