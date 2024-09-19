import os
def crear_archivo(nomfile, contenido, pathejecutable):
    #Se obtiene la ruta de la carpeta donde sta el ejecutable
    ruta_carpeta = os.path.dirname(pathejecutable)
    #Se construye la ruta completa del nuevo archivo
    ruta_completa = os.path.join(ruta_carpeta,nomfile)
    #Creacion del archivo y luego postermimente escribimos el contenido
    with open(ruta_completa, 'w') as archivo:
        archivo.write(contenido)
pathejecutable = "D:\\Programas\\Programacion\\MisProgramas\\AprendiendoReversing\\Ejercicios-Rever-S\\crackme_solid_04\\crackme_solid_04.exe"
#Dependiendo de la ruta esto es modificable
nombre_archivo = "test.txt" #se indica el nombre del archivo que va a ser creado
contenido = "ZZZZZZZZZZZ" #Este es el contenido del archivo ya creado
crear_archivo(nombre_archivo, contenido, pathejecutable)