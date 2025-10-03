# --- SCRIPT GENÉRICO DE GENERACIÓN DE CLAVE (FÓRMULA: (Par1 + Par2) * 2) ---

# 1. Solicitar la entrada y realizar validación
entrada_valida = False
while not entrada_valida:
    entrada = input("➡️ Ingresa un número de 4 dígitos (ej: 1933): ")
    
    # Validar que sean exactamente 4 caracteres y que todos sean dígitos
    if len(entrada) == 4 and entrada.isdigit():
        entrada_valida = True
    else:
        print("❌ Error: Por favor, ingresa exactamente 4 dígitos. Intenta de nuevo.")

# 2. Separar la entrada en dos pares de 2 dígitos
# La primera mitad son los dígitos en las posiciones 0 y 1.
par1_str = entrada[0:2]
# La segunda mitad son los dígitos en las posiciones 2 y 3.
par2_str = entrada[2:4]

# 3. Convertir las cadenas de pares a números enteros
par1 = int(par1_str)
par2 = int(par2_str)

# 4. Aplicar la fórmula de la clave: (Par1 + Par2) * 2
# a. Sumar los dos pares:
resultado_suma = par1 + par2
# b. Multiplicar el resultado por 2:
resultado_final = resultado_suma * 2

# 5. Formatear la clave final
clave_final = "KEY" + str(resultado_final)

# 6. Mostrar el resultado
print("\n--- DETALLES DEL CÁLCULO ---")
print(f"Número ingresado: {entrada}")
print(f"   - Primer Par: {par1}")
print(f"   - Segundo Par: {par2}")
print(f"   - Suma: {par1} + {par2} = {resultado_suma}")
print(f"   - Resultado Final: {resultado_suma} x 2 = {resultado_final}")
print(f"\n✅ La clave generada es: {clave_final}")