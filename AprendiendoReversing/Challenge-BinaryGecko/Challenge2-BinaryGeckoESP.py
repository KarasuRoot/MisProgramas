user_name = input("Ingresa el nombre de usuario (ej: Karasu): ")


intermediate_key = []
for char in user_name:
    # Obtiene el valor ASCII y le suma 3.
    new_char_code = ord(char) + 3
    new_char = chr(new_char_code)
    intermediate_key.append(new_char)

# La clave intermedia cifrada
ciphered_string = "".join(intermediate_key)

# 2. Inversión de Cadena
# Se invierte la cadena para obtener el serial final.
final_key = ciphered_string[::-1]

# Muestra el resultado
print("\n--- Resultado ---")
print(f"Usuario: {user_name}")
print(f"Clave generada (final): {final_key}")
print("-----------------")