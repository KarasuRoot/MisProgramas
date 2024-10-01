'''
Version1 
nombre = input('Indique el Usuario: ')
long = len(nombre)
serial = long * 4
print('La Clave para tu usuario', nombre, 'es:', serial)
'''
#Version2
nombre = input('Indique el Usuario: ')
print('La Clave para tu usuario', nombre, 'es:', len(nombre) * 4)