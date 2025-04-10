'''
Dado un archivo txt con varios numeros, completar con 0 - haciendo que el formato sea de 4 digitos

'''

with open('D:/Eugenio/archivo1.txt', 'r') as archivo: #Lee El archivo
    numeros = [line.strip() for line in archivo]

with open('D:/Eugenio/archivo2.txt', 'w') as archivo_formateado: #Genera un archivo nuevo donde completa con 0000 para formar 4 digitos
    for numero in numeros:
        numero_entero = int(numero)
        if numero_entero < 100: #Si el nmero por ejemplo es 101 -> 0101 sera el resultado
            numero_formateado = '{:04d}'.format(numero_entero)
        else:
            numero_formateado = '{:04d}'.format(numero_entero)
        archivo_formateado.write(numero_formateado + '\n')