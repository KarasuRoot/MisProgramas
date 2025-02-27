''' Diccionarios - otro tipo de coleccion, los elementos se guardan desordenados - poseen dos elemento por posicion (clave y valor) - la clave no puede duplicarse
diccionario = {'azul':'blue','rojo':'red','verde':'green'} azul = clave / blue = valor - primer elemento - se separan por :
diccionario['amarillo'] = 'yellow' agrega el elemento amarillo
del (diccionario['verde']) elimina la clave y tambien el valor)
print(diccionario['azul']) asi se muestra por ejemplo blue en la terminal
print (diccionario) - muestra todos los elementos del diccionario

Ejemplo de una agenda con listas y diccionario
dic = {'Alejandro':[22,1.71], 'Jose':[21,1.75],'Maria':[19,1.60]}
print (dic)

Ejemplo de diccionarios dentro de otro diccionario
dic = {'Alejandro':{'Edad':22,'estatura':1.71}, 'Jose':[21,1.75],'Maria':[19,1.60]}
print (dic['Alejandro'])

Parte 2 Diccionarios 
equipo ={10:'Paulo Dybala',11:'Douglas Costa',7:'Cristiano Ronaldo', 17:'Mario Manzuki'}
print(equipo[10]) Le pasa la clave, no es el elemento del inidce 10 -

Si no existe la clave -> da exepcion, pero podemos hacer que nos de un mensaje con .get
print(equipo.get(2,'No existe ese jugador')) 
print (10 in equipo) Comprueba si existe la clave 10 en el diccionario equipo - devuelve valor booleano
print(equipo.keys) asi solo muestra las claves, no los valores
print(equipo.values) asi solo muestra los valores, no las claves
con (len(equipo)) dice cuantos elementos existe en el diccionario
.clear para vaciar el diccionario
.items() rcecorre diccionarios con FOR

'''