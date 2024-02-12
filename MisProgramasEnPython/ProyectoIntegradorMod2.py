lis1 = []
while True:
	print("1 - Visualizar listado de alumnos")
	print("2 - Añadir nuevo alumno")
	print("3 - Salir")
	print("------------------------------------------------")
	options = input("Ingrese la opcion que corresponda: ")
	if options == "1":
		print("Listado solicitado: ")
		for alumno in lis1:
			nombre = alumno[0]
			curso = alumno[1]
			print(nombre + " | " + " Inscripto en " + str(curso) + " cursos" )
	elif options == "2":
		nomalum = input("Ingrese el nombre del nuevo alumno:")
		cantcurso = int(input("Ingrese la cantidad de cursos a la que esta inscripto el alumno " + nomalum +":"))
		if nomalum == "":
			print("Nombre invalido")
		else:
			lis1.append([nomalum,cantcurso])
			print("Alta del alumno éxitosa")
	elif options == "3":
		input("Muchas gracias, hasta la proxima")
		break
	else:
		print("Opcion incorrecta, ingrese una opcion valida")
