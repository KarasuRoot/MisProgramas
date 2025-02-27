#Colas Python simula - FIFO -  lo primero en entrar es lo primero en salir
cola=['Maria','Alejandro','Jose','Mario']
cola.append('Karla') #Agregamos al final de la cola
cola.append('Flor')

cola.pop(0) #Saca el primer valor de la cola
print('Atendiendo a {n}')
print(cola)