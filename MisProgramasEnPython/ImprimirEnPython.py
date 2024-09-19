#Este es el famoso hola mundo en python (para imprimir) + \n hace un salto de linea
""" agregando un signo de menos. Se puede escribir: -11111111, o -11_111_111.

Los números positivos no requieren un signo positivo antepuesto, pero es permitido, si se desea hacer. Las siguientes líneas describen el mismo número: +11111111 y 11111111."""

print('Hola mundo, mehh\n')
print('La Witsi Witsi Araña\nsubió a su telaraña.') 
print('Vino la lluvia\ny se la llevó.')

#print("La Witsi Witsi Araña" , "subió" , "a su telaraña.") este print muestra lo mismo que la linea 4 pero es con 3 argumentos.

print("Mi nombre es", "Python.", end=" ") 
print("Monty Python.")
print('')
""" Sintaxis de un argumento de palabra clave: una palabra clave se identifica el argumento (end aquí); un signo de igual (=); 
y un valor asignado a ese argumento;
cualquier argumento de palabra clave debe colocarse después del último argumento posicional.
end determina los caracteres que la función print() envía a la salida una vez que llega al final de sus argumentos posicionales.
El comportamiento predeterminado refleja la situación en la que el argumento de palabra clave end se usa implícitamente de la siguiente
 manera: end="\n
 Si el argumento end se estableció en nada, la función print() tampoco genera nada, una vez que se han agotado sus argumentos posicionales.
"""

print("Mi", "nombre", "es", "Monty", "Python.", sep="-")
"""El argumento sep produce los siguientes resultados: Mi-nombre-es-Monty-Python.
La función print() ahora usa un guión, en lugar de un espacio, para separar los argumentos de salida.
"""""
