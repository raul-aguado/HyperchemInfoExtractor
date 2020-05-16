import os
from os import scandir, getcwd
import sys
import time

#Definir la funcion que va a indexar los archivos
def indexador_archivos(ruta=getcwd()):
    return[arch.name for arch in scandir(ruta) if arch.is_file()]

#La promosió 1
def info_creador():
    print("########################################################")
    print("Resumen generado mediante Hyperchem File Extractor 2.1.1")
    print()
    print("Creado por Raul Aguado                              2020")
    print("########################################################")
    print()
    print()

#Inicio del programa
info_creador()


#Preguntar por la ruta que hay que comprobar
print("Por el momento este programa solo resumirá las energias")
print("Mas funciones mas adelante :D")
print()
ruta=input("Introduce la ruta para comprobar: ")
print()
print("Buscando archivos de registro en la ruta selecionada...")
print()
time.sleep(1)
print()

#Se crea el archivo que va a contener nuestro resumencito
file = open(ruta+"/Resumen Hyperchem.txt", "w")

#Se indexan todos los archivos de la carpeta mediante la funcion definida antes
filepaths = (indexador_archivos(ruta))
num_archivos=len(filepaths)
print("En la carpeta existen " + str(num_archivos) + " arhivos")
time.sleep(1)

#La promosió 2
file.write("########################################################" + os.linesep)
file.write("Resumen generado mediante Hyperchem File Extractor 2.1.1" + os.linesep)
file.write(os.linesep)
file.write("Creado por Raul Aguado                              2020" + os.linesep)
file.write("########################################################" + os.linesep)
file.write(os.linesep)

#Se crea la lista que va a contener las lineas del archivo que se esta analizando (fp)
mylines=[]
for fp in filepaths:
    # Split the extension from the path and normalise it to lowercase.
    ext = os.path.splitext(fp)[-1].lower()
    ruta_completa=ruta+"/"+fp
    
    # Now we can simply use == to check for equality, no need for wildcards.
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
        
        time.sleep(4)
        
    #Si el archivo es un .txt podria contener informacion de Hyperchem
    elif ext == ".txt":
        #Con la siguiente linea se evita que el programa analice el propio resumen
        if fp!="Resumen Hyperchem.txt":
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
            
                while mylines[n]!="ENERGIES AND GRADIENT\n":
                    n=n+1
                else:
                    print(mylines[n])
                    m=n+8
                    n=n+1
                    while n<m:
                        file.write(mylines[n] + os.linesep)
                        n=n+1
                file.write("==========" + os.linesep)
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
