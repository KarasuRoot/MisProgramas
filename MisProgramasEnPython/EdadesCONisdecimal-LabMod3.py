# Programa que indica si una persona es mayor o no - PERO verifica que no sea una edad definida como decimal
edad_str = input("Ingrese su edad: ")

while not edad_str.isdigit():  # Uso isdigit() para verificar solo dígitos
    print("Error en el ingreso. Por favor, ingrese su edad en números enteros.")
    edad_str = input("Volve a ingresar tu edad en números enteros: ")

edad = int(edad_str)  # Valida que sea un entero

if edad >= 18:
    print("Usted es mayor de edad")
else:
    print("Es menor de edad")