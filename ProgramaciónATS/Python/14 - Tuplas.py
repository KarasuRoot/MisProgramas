'''Tuplas
Son 'Listas inmutables
NO se permipe eliminar, añadir ni modificar los elementos definidos al inicio
Se indican con ()
'''
tupla=(4,5,5.65,'Hola',[1,2,3])

#print(tupla) muestra toda la tupla
print(tupla[2]) #Muestra el elemento segun el indice indicado, tambien se puede con indices negativos
print(4 in tupla) #Podemos buscar un elemento de la tupla, tambien se puede usar index, count - tambien podemos usar len

lista = list(tupla) #Asi puedo transformar una tupla en una lista
lis = [4,5,5.65,'Hola',[1,2,3]]
tup = tuple(lis) #Asi puedo transformar una lista en tupla
