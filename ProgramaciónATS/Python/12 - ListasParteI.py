'''
Listas (arreglos o vectores)
Ademas se puede almacenar varios tipos de datos incluyendo otras listas
Las listas se limitan por [] y los elementos se separan por ","
Comienzan con indice 0 y se incrementa de izq a derecha
'''
lista = ['Lunes','Martes','Miercoles','Jueves','Viernes',40,10.1,[1,2,3],True] #Asi se define una lista
print(lista)                                              #Asi se imprime una lista
print(lista[2])                                           #Asi se imprime un solo elemento, en este caso es el indice 2 por lo que muestra Miercoles
print(lista[-1])                                          #Con -1 de inice podemos acceder desde el final al principio
print(lista[0:3])                                         #Podemos dar un rango para listar - No incluye el final
print(lista[:4])                                          #Si le indicamos solo el final, comienza desde el comienzo hasta la posicion -1
print(lista[1:4])                                         #Asi se imprime desde el inidcio indicado hasta -1 indice indicado como final
