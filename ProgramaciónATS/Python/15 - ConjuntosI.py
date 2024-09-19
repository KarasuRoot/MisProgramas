'''
Conjuntos
Grupo de elementos desordenados
No pueden haber duplicados - siempre se guarda como valor unico
Se delimitan con {}
Conjuntos y Dicconarios se delimitan {} entonces, por eso se incializa con set
No pueden haber otro tipo de colecciones como listas
'''
conj = set() #crea un conjunto vacio
conj = {1,3,'hola',5.12}
print(conj)
print('\nPara Agregar un conjunto se usa ADD')
conj.add(5) #Agrega el valor de 5 de forma aleatoria
print(conj)
print('\nPara Eliminar un conjunto se usa DISCARD')
conj.discard(3) #Agrega el valor de 5 de forma aleatoria
print(conj)
#con el metodo CLEAR se vacia el conjunto
print('\nPara Buscar un valor en el conjunto con in - Devuelve valor booleano')
print(1 in conj) #tambien se puede hacer a la inversa si no esta el conjunto print(2 not in conj)