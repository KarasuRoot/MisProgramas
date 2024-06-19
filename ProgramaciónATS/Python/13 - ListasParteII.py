lista = [1,2,4,5]
print('\nIndico la cantidad de elementos que tiene la lista')
print(len(lista))  #Para saber cuantos elementos tiene - devuelve un valor entero
print('\nPuedo agregar un elemento al final de la lista')
lista.append(6) #Agrega un elemento al final de la lista
print('\nAqui puedo agregar un elemento al final de la lista pero otro tipo de dato')
lista.append("Dan") #Se puede agregar cualquier tipo de dato
print(lista)
print('\nInserto un valor en la lista en la posicion 2')
lista.insert(2,'Prueba') #Inserta un elemento en la lista, primero el indice(2) y luego el valor (3)
print(lista)
print('\nAgrego varios elementos al final de la lista')
lista.extend([7,8,9])  #Agrega varios elementos a la lista al final - se pasa una lista y la concatena con la anterior
print(lista)
print('\nConcateno dos listas')
lis1 = [1,2,3]
lis2 = [4,5,6]
lis3 = lis1 + lis2 #Asi se concatenan dos listas
print(lis3)
listabusca = [1,2,3,4,5,'Alan',1,1,4,2,5,6]
print('\nBusco si existe un valor en la lista si esta devuelve TRUE sino FALSE')
print(3 in listabusca)  #Devuelve un valor booleano indicando si esta o no el elelemnto buscado en la lista
print('\nDevuelve el indice indicado de la lista')
print(listabusca.index(5)) #Devuelve el indice del valor indicado
print('Indica cuantas veces aparece un valor en la lista')
print(listabusca.count(1)) #Se le indica el valor que estamos buscando y nos indica cuantas veces se repite en la lista
listaelimina=[1,2,3,4,5,'Dan']
#listaelimina.pop() -> Eliminaria Dan por que es el ultimo elemento
listaelimina.pop(2) #Elimina el ultimo valor de la lista si no se indica el INDICE en los ()
print('\nSe elimina el valor de la lista indicado por el inice')
print(listaelimina)
print('\nCon el metodo REMOVE elimina el valor de la lista sin saber que indice tiene')
listaelimina.remove(5) #Elimina el valor de la lista que se indica en () - si no sabemos que indice tiene
print(listaelimina)
print('\nborro toda la lista con el metodo CLEAR')
listaelimina.clear() #Borra toda la lista
print(listaelimina)
listarever = [1,2,3,4,5]
print('\nTeniendo la siguiente lista')
print(listarever)
print('\nPodemos Invertir la lista con el metodo REVERSE')
listarever.reverse() #Invierte la lista
print(listarever)
print('\nTeniendo la siguiente lista')
listacopy = ['uno','dos','tres',4,5]
print(listacopy)
listacopy = ['uno','dos','tres',4,5]*2 #asi podemos copiar la lista
print('Podemos copiar la lista asi')
print(listacopy)
lisorden = [5,7,2,1,9,-4] 
print('\nDada una lista desordenada')
print(lisorden)
print('Podemos ordenarla con el metodo SORT de forma ascendente')
lisorden.sort() #Ordena de menor a mayor
print(lisorden)
print('Podemos ordenarla tambien de forma decendente')
lisorden.sort(reverse=True)#Asi logramos que ordene de mayor a menor
print(lisorden)
print('\nLista Origen')
lisorigen=[1,2,3,4]
print(lisorigen)
print('\nSe puede reemplazar un valor de la lista - se reempalzara el 1 por 9')
lisorigen[0]=9 #Se reemplaza el valor 1 por 9 por que se inidca que el indice 0 sea igual a 9 - anteriormente era 1
print(lisorigen)