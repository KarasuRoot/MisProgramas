
import os
import struct
import sys

# --- CONFIGURACIÓN ---
# La ruta donde se guardará el archivo de licencia.
directorio_destino = r"C:\Users\Administrador\Desktop\BinaryGecko"
nombre_archivo = "licencia.enc"
ruta_completa = os.path.join(directorio_destino, nombre_archivo)

# --- CONSTRUCCIÓN DEL CONTENIDO BINARIO (25 bytes) ---

# 1. 4 bytes: "Lice" (1279869765 en Little-Endian)
# struct.pack("<I", ...) convierte el número entero a los 4 bytes requeridos.
encabezado = struct.pack("<I", 1279869765) 

# 2. 12 bytes: "BinaryGeck0" + Terminador Nulo (\x00)
subcadena_1 = b"BinaryGeck0\x00" 

# 3. 4 bytes: Relleno nulo
relleno = b"\x00\x00\x00\x00" 

# 4. 5 bytes: "9898" + Terminador Nulo (\x00)
subcadena_2 = b"9898\x00" 

# Concatenar todos los bytes para formar el contenido final
contenido_final = encabezado + subcadena_1 + relleno + subcadena_2

# --- CREACIÓN DEL ARCHIVO ---

try:
    # 1. Crear el directorio si no existe (exist_ok=True evita un error si ya existe)
    os.makedirs(directorio_destino, exist_ok=True)
    
    # 2. Escribir el contenido binario (25 bytes) en modo 'wb' (write binary)
    with open(ruta_completa, "wb") as f:
        f.write(contenido_final)

    print(f"✅ ¡Éxito! Archivo '{nombre_archivo}' generado.")
    print(f"   Tamaño: {len(contenido_final)} bytes")
    print(f"   Ruta de guardado: {ruta_completa}")

except PermissionError:
    # Captura si el script no tiene permisos para escribir en la ruta
    print(f"❌ Error de permisos: No se pudo escribir en la ruta '{directorio_destino}'.", file=sys.stderr)
    print("   Asegúrate de ejecutar el script con permisos suficientes.", file=sys.stderr)
except Exception as e:
    # Captura cualquier otro error
    print(f"❌ Error inesperado al escribir el archivo: {e}", file=sys.stderr)