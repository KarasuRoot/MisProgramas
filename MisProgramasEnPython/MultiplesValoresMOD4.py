""" aqui se define una funcion en una lista y luego retorna la lista, de esta manera se pueden tener multiples resultados en un retorno """
def min_max(lista):
	a = min(lista)
	b = max(lista)
	resultado = [a, b]
	return [a,b]



print (min_max ([1000,4,9,1,4,7,10,30,900]))