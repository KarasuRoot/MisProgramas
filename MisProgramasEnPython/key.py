usu = input('Indique nombre de usuario: ')
usu = usu.upper()
key = 0
if usu.isalpha() == True:
    for c in usu:
        key = key + ord(c)
    key = key^int(0x444C)
    print('Su serial es: ' + str(key))
else:
    print ("El usuario debe contener solo letras")



