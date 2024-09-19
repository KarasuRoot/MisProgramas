'''Hacer un programa que simule ser un cajero automatico
Con un saldo inicail de $1000 y tendra el siguiente menu de operaciones:
1 - Ingresar dinero en la cuenta
2 - Retirar dinero de la cuenta
3 - Mostrar dinero disponible
4 - Salir 
'''
saldo = 1000
print('\t.:MENU:.') #\t. espacio o tabulacion inical
print('1. Ingrese dinero a la cuenta')
print('2. Retire dinero a la cuenta')
print('3. Visualizar dinero a la cuenta')
print('4. Salir')
menu = int(input('Ingrese el numero de la operacion que desea realizar: '))
if menu == 1:
    s = float(input('\nIndique la cantidad de dinero que desea ingresar: '))
    saldo +=s #es lo mismo que s = saldo + s
    print(f'\nSu saldo actual es de: {saldo}')
elif menu == 2:
    r = float(input('\nIndique la cantidad de dinero que desea retirar: '))
    if r > saldo:
        print('\nSaldo insuficiente')
    else:
        saldo -=r
        print(f'\nSu saldo actual es de: {saldo}')
elif menu == 3:
    print(f'\nSu saldo actual es de: {saldo}')
elif menu == 4:
    print('\nGracias por usar nuestro cajero. Que tenga buen dia')
else:
    print('\nOperacion no valida')

    