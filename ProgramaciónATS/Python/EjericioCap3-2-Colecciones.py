'''Ejercicio 2
Escriba un programa que tenga dos listas y que, a continuacion, cre las siguientes listas (en las que no debe haber repeticiones)
- Lista de palabras que aparecen en todas las listas
- Lista de palabras que aparecen en la primera lista, pero no en la segunda
- Lista de palabras que aparecen en la segunda lista, pero no en la primea
- Lista de palabras que aparecen en ambas listas.
'''
list1 = [1,2,3,4,5,4,3,2,2,1,5]
list2 = [4,5,6,7,8,4,5,6,7,7,8]

#Elimino los elementos repetidos de las listas
conj1 = set(list1)
conj2 = set(list2)
union = list(conj1 | conj2)
soloConj1 = list(conj1 - conj2)
soloConj2 = list(conj2 - conj1)
interseccion = list(conj1 & conj2)
print(f'Lista de palabras que aparecen en todas las listas: {union}')
print(f'Lista de palabras que aparecen en la primera lista, pero no en la segunda: {soloConj1}')
print(f'Lista de palabras que aparecen en la segunda lista, pero no en la primea: {soloConj2}')
print(f'Lista de palabras que aparecen en ambas listas: {interseccion}')
