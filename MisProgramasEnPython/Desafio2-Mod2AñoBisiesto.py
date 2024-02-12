an = int(input("Ingrese el año deseado: "))
if an % 400 == 0:
	print("El año " + str(an) + " es bisiesto")
elif an % 4 == 0 and an % 100!=0:
	print("El año " + str(an) + " es bisiesto")
else:
	print("El año " + str(an) + " no es bisiesto")