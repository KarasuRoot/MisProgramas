import socket
import getpass
import pyperclip  # Importamos la librería para el portapapeles

# --- 1. Obtención y Procesamiento del Nombre del Equipo (PC Name) ---

nombre_pc_completo = socket.gethostname()

# Lógica asumida: Tomar el último segmento después del guion medio ('-').
if '-' in nombre_pc_completo:
    # Dividimos y tomamos el último elemento de la lista [-1]
    nombre_pc_segmento = nombre_pc_completo.split('-')[-1]
else:
    # Si no hay guion, tomamos el nombre completo
    nombre_pc_segmento = nombre_pc_completo
    
# Normalizar a MAYÚSCULAS para el segmento de la PC
nombre_pc_segmento = nombre_pc_segmento.upper()


# --- 2. Obtención del Nombre del Usuario (User Name) ---

nombre_usuario = getpass.getuser()
# Mantenemos el nombre de usuario Case-Sensitive.


# --- 3. Formateo de la Cadena Final (Patrón: PC_SEGMENTO-USUARIO-REV) ---
cadena_base = nombre_pc_segmento + "-" + nombre_usuario + "-REV"


# --- 4. Copiar al Portapapeles y Notificar ---
try:
    pyperclip.copy(cadena_base)
    
    # 5. Informe del Resultado
    print("\n=== Simulador de Generación de Cadena (FINAL) ===")
    print(f"Nombre del Equipo (Segmento, Mayúsculas): {nombre_pc_segmento}")
    print(f"Nombre del Usuario (Case-Sensitive): {nombre_usuario}")
    print("------------------------------------------")
    print(f"✨ La cadena ha sido copiada al portapapeles: {cadena_base}")
    print("------------------------------------------")

except pyperclip.PyperclipException as e:
    # Este error ocurre a menudo si no hay un entorno gráfico disponible (ej. SSH)
    print("\n❌ ERROR: No se pudo acceder al portapapeles.")
    print("Asegúrate de tener un entorno gráfico o las dependencias necesarias (ej. xclip/xsel en Linux).")
    print(f"La cadena generada es: {cadena_base}")
    print(f"Detalle del error: {e}")