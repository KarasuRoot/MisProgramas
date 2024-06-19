#Hace un programa que pida 2 numeros y se de cuenta cual de ellos es par o si ambos lo son
num1=int (input('Ingrese el primer numero: '))
num2=int (input('Ingrese el segundo numero: '))

if num1 %2 and num2 ==0:
    print(f'Los numeros {num1} y {num2} son par')
elif num1 %2 == 0 and num2 %2 !=0
    print(f'El numeros {num1} es par y {num2} es impar')
elif num1 %2  !=0 and num2 %2 ==0
    print(f'El numeros {num1} es impar y {num2} es par')   

else:
    print('Los dos numeros son impares')
