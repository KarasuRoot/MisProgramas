#Programa que indica si una persona es mayor o no - PERO verifica que no sea una edad definida como decimal
edad = input("ingrese su edad: ")
while edad.isdecimal() == False:
	print("error enel ingreso")	
	edad =input("volve a ingresar tu edad en numeros enteros")
	if edad < 18:
		print("used es mayor de edad")
	else:
		print("es menor de edad")