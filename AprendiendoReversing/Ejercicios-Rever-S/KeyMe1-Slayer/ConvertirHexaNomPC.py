'''nombre_pc = "DESKTOP-REVER"
constante_xor = 1234
conta = 0
for caracter in nombre_pc:
    valor_decimal = ord(caracter)
    valor_hexadecimal = hex(valor_decimal)
    conta += valor_decimal
sumaHEX = conta ^ constante_xor
print(f"La suma total en decimal es: {conta}")
print(f"La suma total en hexadecimal es: {hex(conta)}")
print(f"El resultado XOR en Hexadecimal es: {hex(sumaHEX)}")
print(f"El resultado XOR en Decimal es: {sumaHEX}")
'''

'''import socket
import subprocess
nombre_pc = socket.gethostname()
constante_xor = 0x1234
conta = 0
# Calculo la suma hexadecimal directamente
for caracter in nombre_pc:
    valor_decimal = ord(caracter)
    valor_hexadecimal = hex(valor_decimal)
    conta += valor_decimal
sumaHEX = conta ^ constante_xor
# Copio solo el nombre de la PC al portapapeles
subprocess.run(["clip"], input=nombre_pc.encode(), check=True)

# Imprimo los resultados por consola
print("El nombre de tu computadora es:", nombre_pc)
print("Se ha copiado el nombre al portapapeles.")
print(f"El resultado XOR en Hexadecimal es: {hex(sumaHEX)}")
print(f"El resultado XOR en Decimal es: {sumaHEX}")
'''

import socket
import subprocess
import time
import os
import struct
nombre_pc = socket.gethostname().upper()#Tomo el nombre de la PC en mayus
constante_xor = 1234 #Defino una constante para luego operar
contador = 0
for caracter in nombre_pc: # Calculo la suma hexadecimal directamente
    valor_decimal = ord(caracter)
    valor_hexadecimal = hex(valor_decimal)
    contador += valor_decimal
sumaHEX = contador ^ constante_xor #Aca realizo la operacion de hacer la CONSTANTE XOR el resultado 
estru0 = struct.pack("<I",constante_xor) #Converto datos de Python en una cadena de bytes, siguiendo un formato específico.
estru1 = struct.pack("<I", sumaHEX) #<: Indica que se usará el orden de bytes "little-endian"
final = estru1 + estru0 #Sumo las dos variables donde converti cada cadena de bytes
subprocess.run(["clip"], input=nombre_pc.encode(), check=True)# Copiamos solo el nombre de la PC al portapapeles
print("El nombre de tu computadora es:", nombre_pc)# Imprimimos los resultados por consola
print("Se ha copiado el nombre al portapapeles.")
print(f"El resultado XOR en Hexadecimal es: {sumaHEX:X}")
print(f"El resultado XOR en Decimal es: {sumaHEX}")
ruta_escritorio = os.path.join(os.environ['USERPROFILE'], 'Desktop')# Creo el archivo
ruta_archivo = os.path.join(ruta_escritorio, "reg.key")
with open(ruta_archivo, "wb") as archivo:
    archivo.write(final)
# Mantener la consola abierta hasta que el usuario presione Enter
input("Presiona Enter para salir...")