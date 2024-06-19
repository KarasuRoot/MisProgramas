'''
Construir un programa que simule el funcionamiento
de una calculadora que pueda realizar cuatro operaciones aritmeticas basicas (suma, resta, multiplicacion y division)
El usuario debe especificar la operacion con el primer caracter del nombre de la operacion
S,s - Suma
R,r - Resta
P,p,M,m - Multriplicacion
D, d - Division
'''
num1= float(input('Ingrese el primer numero: '))
num2= float(input('Ingrese el segundo numero: '))
print('\nLas Operaciones son S (Suma) - R (Resta) - P o M (Multiplicacion) y D (Division)')
oper = (input('\nIngrese la operacion que desea realizar: ')).upper()
if oper == 'S':
    suma = num1 + num2
    print(f'\nEl Resultado de la suma entre {num1} y {num2} es {suma}')
elif oper == 'R':
    resta = num1 - num2
    print(f'\nEl Resultado de la resta entre {num1} y {num2} es {resta}')
elif oper == 'M' or oper =='P':
    mul = num1 * num2
    print(f'\nEl Resultado de la Multiplicacion entre {num1} y {num2} es {mul:.2f}')
elif  oper == 'D':
    div = num1 / num2
    print(f'\nEl Resultado de la Division entre {num1} y {num2} es {div:.2f}')
else:
 print("\nOperacion no Valida")