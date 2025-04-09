'''
Dado un archivo txt con varios numeros, completar con 0 - haciendo que el formato sea de 4 digitos

'''

with open('D:/Eugenio/archivo1.txt', 'r') as archivo:
    numeros = [line.strip() for line in archivo]

with open('D:/Eugenio/archivo2.txt', 'w') as archivo_formateado:
    for numero in numeros:
        numero_entero = int(numero)
        if numero_entero < 100:
            numero_formateado = '{:04d}'.format(numero_entero)
        else:
            numero_formateado = '{:04d}'.format(numero_entero)
        archivo_formateado.write(numero_formateado + '\n')