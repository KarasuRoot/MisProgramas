'''Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.'''

nom = input('Escribe tu nombre:')
num = input('Indica un numero:')
print((nom + "\n") * int(num))