'''
Hacer un programa que pida un caracter e indique si es una volcal o no 
Vocales (A E I O U)
'''
car = input('Ingrese un caracer').lower() #el metodo .lower() lo convierte en minuscula
#el metodo .upper() es para converitr en mayuscula
if car == 'a' or car == 'e' or car == 'i'  or car == 'o'  or car == 'u':
    print('Es una vocal')
else:
    print('No es una vocal')