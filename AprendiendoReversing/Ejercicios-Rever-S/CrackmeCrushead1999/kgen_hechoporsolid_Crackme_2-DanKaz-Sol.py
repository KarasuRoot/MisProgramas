usuario = input("Ingresa tu nombre: ")
usuario = usuario.encode()
serial = sum(usuario)
print("El serial es: {}".format(serial))