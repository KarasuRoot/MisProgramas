#Pilas con listas - en Python solo se SIMULA - usa LIFO - el ultimo agregado es el primero en salir
pila = [1,2,3]
pila.append(4) #agregamos el elemento por el final
print(pila)
pila.append(5)
pila.pop() #saca el ultimo elemento
print(pila)
n =pila.pop()
print (f'Sacando el ultimo elemento{n}')
n =pila.pop()
print (f'Sacando el ultimo elemento{n}')