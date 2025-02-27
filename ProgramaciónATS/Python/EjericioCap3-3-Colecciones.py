'''
Ejercicio 3
Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos
Nombre:Aaragon
Clase: Guerrero
Raza: Dúnandan del Norte

Nombre:Legolas
Clase:Arquero
Raza:Elfo Sindar

Nombre:Gandalf
Clase:Mago
Raza:Istar

'''

PJ = [] #Creando una lista vacia
p = {'Nombre':'Aaragon','Clase': 'Guerrero','Raza': 'Dúnandan del Norte'}
PJ.append(p) #Agrego a la lista el personaje creado
p = {'Nombre':'Legolas','Clase': 'Arquero','Raza': 'Elfo Sindar'}
PJ.append(p)
p = {'Nombre':'Gandalf','Clase': 'Mago','Raza': 'Istar'}
PJ.append(p)
print(PJ)