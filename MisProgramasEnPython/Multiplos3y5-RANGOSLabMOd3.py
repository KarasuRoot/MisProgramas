#Multiplos
#Se requiere buscar multiplos de 3 y 5 en un rango que ingrese el usuario. Guardar los multiplos en una lista
#Usar for asociado a un range como se vio en la teoria.
#para listar podes usar list(range(5,12)) -> devuelve [0,1,2,3,4,5,6,7,8,9,10,11]
inicio = input("Ingrese el numero de incio del rango: ")
inicio = int(inicio)

final = input("Ingrese el numero del final del rango: ")
final = int(final)

multiplos = []

for n in range(inicio,final+1,1):
	if n%3 == 0 and n%5 == 0:
		multiplos.append(n)

print("Los multiplos de 3 y de 5 en ese rango son: ")
print(multiplos)