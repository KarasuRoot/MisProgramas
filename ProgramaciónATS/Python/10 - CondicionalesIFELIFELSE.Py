#Condicionales (IF ELIF Y ELSE) (compara dos valores y el resultado es un valor logico)

num = int(input('Digite un numero: '))
if num > 0:
    print(f'El numero {num} es positivo')
elif num == 0:
    print(f'El numero es 0')
else: #caso contrario
    print(f'El numero {num} es negativo')

print('### Fin del programa ###')