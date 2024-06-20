''' 
Segunda parte de conjuntos
Podemos definir un conjunto con valores preestablecidos sin el set
'''

a = {1,2,3}
b = {5,7,4}
print('Definidos el conjunto A como 1,2 y 3 y el conjunto B como 5,3 y 7 -indica con valor booleano si son o no iguales ambos conjuntos')
print (a == b) #¿El conjunto a es igual al conjunto b?
#tambien se puede usar len para saber la cantidad de elementos print(len(a))
#Union de todos los conjuntos - sin repetir
c = a | b
print('\nIndica la union(|) entre los conjuntos dados')
print(c)

#Interseccion es para ver los elmentos que estan entre los dos conjuntos
d = a & b
print('\nIndica la intereccion(&) entre conjuntos (ver los elementos que estan en los dos conjuntos)')
print(d)

#Diferencia del conjunto - solo muestra los elementos que estan en un determinado conjunto
e = a - b
print('\nIndica la Diferencia(-) entre conjuntos, solo muestra los elementos del conjunto especificado')
print (e)

#Diferencia simetrica - solo muestra los elementos que estan en conjuntos deteminados, pero no muestra aquellos que estan en ambos conjuntos
f =  a ^ b
print ('\nDiferencia simetrica(^) indica los elementos que estan en dos conjuntos, pero no muestra los elementos que son iguales entre ambos conjuntos')
print(f)

#Determinar si un conjunto es un subconjunto de otro
g = {1,2,3,4,5}
print('\nIndica un booleano si un conjunto es un subconjunto de otro determinado')
print(a.issubset(g))

#Determinar si un conjunto es el superconjunto de otro
print('\nIndica un booleano si un conjunto es un superconjunto de otro determinado')
print(g.issuperset(a))

#Determinar si un conjunto es Disconexio de otro - no comparten nigun elemento en comun
print('\nIndica un booleano si un conjunto es un conjunto disconexo de otro determinado')
print(a.isdisjoint(b))

#Hacer que un conjunto sea inmutable
o = frozenset({8,9,10})
