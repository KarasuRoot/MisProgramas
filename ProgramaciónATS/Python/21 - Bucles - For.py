#Bucle FOR (PARA) - se sabe cauntas veces se va a repetir
#se puede trabajar con listas, tuplas, conjuntos - trabnaja con colecciones

'''Ejemplo 1
for i in [1,2,3,4,5]: Recorre elemento por elemento
    print('Hola')

'''


'''Ejemplo 2
for i in [2,10,3,4,'Alejandro']: Recorre elemento por elemento
    print(f'Elementos: {i}')

'''

'''Ejemplo 3

coleccion = [2,10,3,4,'Alejandro']
for i in coleccion: Recorre elemento por elemento
    print(f'Elementos: {i}')
'''

'''Ejemplo 4
coleccion = {'Alejandro':22,'Maria':23,'Jose':45,'Luis':12] # de esta forma solo veriamos la clave
for i in coleccion: Recorre elemento por elemento
    print(f'Elementos: {i}')
'''

'''Ejemplo 5
coleccion = {'Alejandro':22,'Maria':23,'Jose':45,'Luis':12] # de esta forma solo veriamos el valor
for i in coleccion: Recorre elemento por elemento
    print(f'{coleccion[i]}')
'''

'''Ejemplo 6.0
coleccion = {'Alejandro':22,'Maria':23,'Jose':45,'Luis':12] # de esta forma veriamos el valor y la clave
for i in coleccion: Recorre elemento por elemento
    print(f'{i} -> {coleccion[i]}')
'''

'''Ejemplo 6.1
coleccion = {'Alejandro':22,'Maria':23,'Jose':45,'Luis':12] # de esta forma veriamos el valor y la clave
for clave,valor in coleccion.items(): Recorre elemento por elemento - el metodo items() es solo de los diccionarios
    print(f'{clave} -> {valor}')
'''
''' Ejemplo 7.0 - recorriendo cadenas
coleccion = 'Alejandro'    va a recorrer elemnto por elemento o caracter por caracter
for i in coleccion:         como Alejandro tiene 9 caracteres, entonces va a repertir 9 veces
    print(f'Hola')      va a salir 9 veces

'''

''' Ejemplo 7.1 - recorriendo cadenas
coleccion = 'Alejandro'    va a recorrer elemnto por elemento o caracter por caracter
for i in coleccion:         
    print(f'{i}')      imrpime elemento por elemnto de toda la cadena

'''


''' Ejemplo 7.2 - recorriendo cadenas
coleccion = 'Alejandro'   para imprimir cada caracter en una sola linea y separando cada caracter
for i in coleccion:         
    print(f'{i}',end = ' ')      
'''

''' Si quiseramos hacer que se reptia una cantidad grande de veces, por ejemopplo 50 veces
no hace falta generar una coleccion de 50 elementos - se puede realizar con range
'''