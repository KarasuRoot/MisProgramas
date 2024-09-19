#Escribir la Formula de Bhaskara en forma de expresion algoritmica
'''
Se requieren 3 valriables

'''

a = float(input('Ingrese su primer numero: '))
b = float(input('Ingrese su segundo numero: '))
c = float(input('Ingrese su tercer numero: '))
bhaska = (a**3 * (b**2 - 2*a*c))/(2*b)
print(f'Tomando los numeros {a}, {b} y {c} y luego usando Bhaskara, el resultado es: {bhaska}')