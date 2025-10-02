import re
usu = input('Indique nombre de usuario: ')
permitido = r"[a-zA-Z0-9:]"
usu = usu.upper()
if re.match(f"^{permitido}+$", usu):
    if usu[0] == 'Z':
        usu = ':' + usu[1:]
key = 0
if usu:
    for c in usu:
        key = key + ord(c)
    key = key^int(0x444C)
    print('Su serial es: ' + str(key))
else:
    print ("El usuario debe contener solo letras")



