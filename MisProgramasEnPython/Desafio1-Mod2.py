perfil = input("Ingrese el rol correspondiente")
if perfil == "admin" or  rol == "profesor":
	if clave =="1234":
		nom = input("Ingrese su nombre: ")
		if nom == "":
			print("No puede tener valor en blanco")
		else:
			print("Bienvenido " + nom)
	else:
		print("Error, Clave incorrecta")
else:
	print("El rol informado no existe")
	