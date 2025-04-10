#Solicito 2 numeros al usuario, luego esos numeros son convertidos en Hexadecimal
def DecAHexa():
    num1 = int(input('Ingrese el primer numero: '))
    numhex1 = hex(num1)[2:].upper()
    num2 = int(input('Ingrese el segundo numero: '))
    numhex2 = hex(num2)[2:].upper()
    print('Su primer numero',num1, 'en Hexa es: ',numhex1)
    print('Su segundo numero',num2, 'en Hexa es: ',numhex2)
DecAHexa()