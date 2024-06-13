#Funciones Integradas
'''
n = str(10.98)  Asi puedo pasar un flotante por ejemplo a cadena
print(type(n))
'''

#Convertir un valor entero a binario
nu = bin(10)
print(f'El numero entero 10, ahora en binario es: {nu}')


#Convertir un valor entero a hexadecimal
nuhex = hex(10)
print(f'El numero entero 10, ahora en Hexadecimal es: {nuhex}')

#Convertir un valor binario a entero
nuint = int('0b1010', 2) #el 2 indica la base en la cual esta el numero
print (f'El numero en binaro 0b1010, ahora es: {nuint}')

#Convertir un valor hexadecimal a entero
nuint2 = int('0xa', 16)
print(f'El numero en hexadecimal 0xa, ahora es: {nuint2}')



#Valor absoulto de un numero
n = abs(-8)
print(f'El valor absoluto de -8 es: {n} ')

redon = round (5.6) #redondea siempre al numero mas cercano
print(f'Su numero fue 5.6, pero se redondea y queda en {redon}')

#Funcion len cuenta cuantos caracteres tiene una cadena que se le pasa en argumento
cuenta = len('Eugenio')
print (f'El nombre Eugenio posee {cuenta} caracteres')