#Programa para dar de alta un alumno y definir cantidad de cursos a las cuales esta inscripto
lis1 = [] #Se define una lista vacia
while True: #Se crea un menu que seguira interactuadno hasta que salga del mismo
	print("1 - Visualizar listado de alumnos")
	print("2 - Añadir nuevo alumno")
	print("3 - Salir")
	print("------------------------------------------------")
	options = input("Ingrese la opcion que corresponda: ") #Se indica la opcion que se quiere hacer
	if options == "1":
		print("Listado solicitado: ")
		for alumno in lis1:		#Si se indica la opcion de ver los alumnos -> Entra en un bucle FOR para mostrar el nombre y el/ cursos a los que pertenece el alumno
			nombre = alumno[0]
			curso = alumno[1]
			print(nombre + " | " + " Inscripto en " + str(curso) + " cursos" )
	elif options == "2":  #Esta parte es para dar de alta un nuevo alumno e indicar a cuantos cursos esta inscripto
		nomalum = input("Ingrese el nombre del nuevo alumno:")
		cantcurso = int(input("Ingrese la cantidad de cursos a la que esta inscripto el alumno " + nomalum +":"))
		if nomalum == "": #Verifica que el nombre no sea vacio
			print("Nombre invalido")
		else:
			lis1.append([nomalum,cantcurso]) #Agrega el nuevo alumno con la cantidad de cursos indicada al final de la lista
			print("Alta del alumno éxitosa")
	elif options == "3":
		input("Muchas gracias, hasta la proxima") #Si se indica que se desea salir, se imprime un mensaje y el brak interrumpe la ejecuccion
		break
	else:
		print("Opcion incorrecta, ingrese una opcion valida")
