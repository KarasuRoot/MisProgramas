'''
Escriba un programa donde tenga una lista y que, a continuacion, 
elimine los elementos repetidos, por ultimo mostrar lista

'''

lista = ['1','2','3','2','3','5']
print(lista)
'''Version 1
conjunto = set(lista) #tasnfomo la lista en un conjunto para quitar los elementos repetidos
lista = list(conjunto) #lo trasnformo a una  lista de nuevo
print(conjunto)
'''

lista =list(set(lista)) #version 2
