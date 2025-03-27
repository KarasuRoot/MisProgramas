''' Bucle While (Mientras) - Raiz cuadrada - se ejecuta N veces - mientras la condicion sea verdadera
Se puede interrumpir en cualquier momento la ejecución del bloque de código con la instrucción break.

import math
numer = int(input('Digite un numero: '))
while numer < 0: #Nos aseguramos que no sea negativo
    print ('Error, debe ser un numero positivo')
    numer = int(input('Digite un numero: '))
print(f'\nSu raiz cuadrada de ' {number} ' es: {(math.sqrt(numer)):.2f}') '''


'''Ejemplo 1 
i = 0
while i < 10:
    print   ('Hola Mundo')
    i += 1
'''
#Ejemplo 2
i = 0
while i < 10:
    print(i)
    i +=1