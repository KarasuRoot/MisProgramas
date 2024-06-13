#Hacer un programa para ingrear el radio de un circulo y luego informar el area y longitud de dicha cirtcunferencia
import math
r = float(input('Indique el radio a calcular por favor: '))
area = math.pi *(r**2)
long = 2 * math.pi * r
print(f'El radio es de {r}, entonces, el area del ciurculo es de {area:.2f} y su longitud es de {long:.2f}') #Para indicar que sean solo 2 decimales por ejemplo en la variable se inidca :.52f
