#Concicionales Combinados
edad = int(input('Digite su edad: '))
if 0 < edad < 100: #es lo mismo que edad > 0 and edad < 99:
    if edad >= 18:
        print ('El usuario es mayor de edad')
    else:
        print ('El usuario es menor de edad')
else:
    print('La edad digitada es incorrecta')