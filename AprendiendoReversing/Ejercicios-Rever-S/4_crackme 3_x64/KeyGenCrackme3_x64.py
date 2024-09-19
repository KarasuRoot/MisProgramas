def keygen(nombre):
  bytesnomb = nombre.encode('utf-8')
  longitud = len(bytesnomb)
  suma = 0
  for byte in bytesnomb:
    suma += ((byte + longitud) ^ 0x41)
  resultado = (suma * 2) ^ 0xFECA
  return resultado
nombre = input("Ingrese un nombre: ")
serial = keygen(nombre)
print("El serial calculado es:", serial)