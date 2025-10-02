# Keygen Slayer_Crackme 
# Author: Solid
import os
import struct
import subprocess

hostname = os.getenv('COMPUTERNAME')  # Obtengo el nombre de la computadora

process = subprocess.Popen(['clip'], stdin=subprocess.PIPE, text=True) #  Copio el nombre de la computadora
process.communicate(input=hostname)                                    #  al portapapeles


hostname = hostname.encode()              # convierto el nombre de la computadora a bytes para poder sumarlos luego
print("hostname: {}".format(hostname))




hostkey = hex(sum(hostname))                 # Sumo los caracteres del nombre de la computadora
print("Hostkey: {}".format(hostkey))
intkey = int(hostkey, 16)                    # Lo paso a int hexadcimal
seed = 1234                                  # Un valor constante para xorear con la suma de los caracteres del nombre de la computadora 
result = seed ^ intkey

print("resultado: {}".format(result))

# Paso el seed y el resultado a entero hexadecimal
n1 = hex(seed)
n2 = hex(result)

n1 = int(n1, 16)
n2 = int(n2, 16)

print("n1 {}\nn2 {}".format(n1, n2))

# convierto ambos valores (seed y result) a dword little endian para luego escribirlos en el archivo reg.key
n1 = struct.pack("<I", (n1))
n2 = struct.pack("<I", (n2))

print("n1 {}\nn2 {}".format(n1, n2))

try:
    with open("reg.key", "wb") as f:
        f.write(n1+n2)
except IOError as e:
    print("Ocurrio un error al intentar crear el archivo: {}".format(e))
    
print("Archivo creado correctamente ! puedes ejecutar el crackme !")

    








