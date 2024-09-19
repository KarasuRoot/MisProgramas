''' Los diccionarios se crean {} y se acceden con ["claves"]
	No tienen indice, si clave
	puede camiar - a diferencia de las tuplas
	no puede haber 2 claves iguales
'''
jugadores = {'mesi': 10, 'dimaria': 7,'martinez':1}  #asi se define un diccionario

''' si haces un len da 3 (por que se toma a mesi, 10 como un elemento y asi sucesivamente)
	para agregar es jugadores["aguero"] = 9 y se guarda al final (no importa)
	para eliminar es del jugadores["aguero"] -> se elimina por clave
	si se quiere usar una misma clave, con otro valor, sobreescribe el valor de la clave existente
'''
for n  in jugadores:
	print(n,"-",jugadores[n])		#cunado recorremos un diccionario con un for obtenemos las claves
									#si quiero el valor, se pone asi
"""
Operadores de membresia o pertenecia:
"in"

"mesi" in jugadores --> devuelve true por que esta en el diccionario - si no estaria FALSE

"""
