cantNom = int(input("Ingrese la cantidad de nombres para su lista: ")) #Solicito la cantidad de nombres a ingresar
names = []
cont = 0
while cont < cantNom:
	nom = input("Ingrese un nombre: ") #Pedira un numbre dependiendo del numero que se eleigio previamente
	if nom != "":	#Valida que no sea  blanco
		names.append(nom) #Agrega cada nombre a la lista
		cont = cont + 1
	else:
		print("No se permiten valore en blanco")
print(*names)