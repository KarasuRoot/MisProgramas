cantNom = int(input("Ingrese la cantidad de nombres para su lista: "))
names = []
cont = 0
while cont < cantNom:
	nom = input("Ingrese un nombre: ")
	if nom != "":
		names.append(nom)
		cont = cont + 1
	else:
		print("No se permiten valore en blanco")
print(*names)