'''
Para resolver el crackme "crackme_2"  el cual pide un nombre y luego un serial -->
Se verifico que ese crackme toma el nombre, lo convierte con valores decimales segun la tabla ascii -> 
los suma entre si y el resultado es el serial buscado 
Por ejemplo si el usaurio es pepe -> el serial es 426 = ¿por que?
'p' -> 112 (ASCII) -> '70' (hexadecimal) -> 112 (decimal)
'e' -> 101 (ASCII) -> '65' (hexadecimal) -> 101 (decimal)
'p' -> 112 (ASCII) -> '70' (hexadecimal) -> 112 (decimal)
'e' -> 101 (ASCII) -> '65' (hexadecimal) -> 101 (decimal)
112 + 101 + 112 + 101 = 426
'''

def serial(usu):  #Defino mi funcion
    conta = 0       #inicializo mi variable para contar en 0
    for letra in usu: #Recorro el string que el usuario indico como 'su usuario'
        valor_hexadecimal = hex(ord(letra))[2:]  # Elimino el prefijo '0x'
        conta += int(valor_hexadecimal, 16)  #suma el contador en hexa
    return conta

usu = (input('Indique su usuario: ')) #Solicita un usuario
resultado = serial(usu) #aplica la funcion previamente definida
print('Su serial es: ', resultado) #imrpimo resultado




