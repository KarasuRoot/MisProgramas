with open('D:\\cbus.txt', 'r') as archivo_entrada, open('D:\\archivo_limpio.txt', 'w') as archivo_salida:
    for linea in archivo_entrada:
        if linea.strip():  # Verifica si la línea no está vacía después de quitar espacios en blanco
            archivo_salida.write(linea)