edad = input("ingrese su edad: ")
while edad.isdecimal() == false:
	print("error enel ingreso")	
	edad =input("volve a ingresar tu edad en numeros")
	if edad < 18:
		print("used es mayor de edad")
	else:
		print("es menor de edad")