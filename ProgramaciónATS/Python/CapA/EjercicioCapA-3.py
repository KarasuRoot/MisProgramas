#Hacer un programa para intercambiar el valor de 2 variables
# Ej a = 10     -> a = 5
#    b = 5      -> b = 10
a =(input ('Indique valor de a: '))
b =(input ('Indique valor de b: '))
a, b = b, a

print(f'El nuevo valor de a es: {a}')
print(f'El nuevo valor de a es: {b}')