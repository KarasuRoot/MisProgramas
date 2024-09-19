#Matrices
m1 =[[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]] 	#Se define una matriz
print (m1)								#Se imprime la matriz
fil = int(input("Fila: "))				#Se espera por teclado el nro de fila q hay en esa posicion
col = int(input("Columna: "))			#Se espera por teclado el nro de columnna q hay en esa posicion
if fil < len(m1):						#Evalua si la fila tiene valores validos
	if col < len(m1[fil]):				#Evalua si la columna tiene valores validos
		print(m1[fil][col])				#Imprime la matriz correspondiedo con la fila y columna 
	else:
		print("Error en las columnas")	#Si la columna no es valida imprime error
else:
	print ("Error en las filas")		#Si la fila no es valida imprime error