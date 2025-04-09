import pandas as pd

archivo_entrada = 'D:\\IMPO.xlsx'  # Reemplaza con la ruta de tu archivo
archivo_salida = 'D:\\IMPOFINAL.xlsx'  # Reemplaza con la ruta donde quieres guardar el resultado

try:
    # Cargar el archivo Excel
    df = pd.read_excel(archivo_entrada)

    # Lógica para extraer datos del CBU directamente en el DataFrame
    df['bco_codigo'] = df['leg_cbu'].astype(str).str[:3]
    df['bco_sucursal'] = df['leg_cbu'].astype(str).str[3:7]
    df['leg_Cbu1'] = df['leg_cbu'].astype(str).str[7]
    df['leg_ctaban'] = df['leg_cbu'].astype(str).str[8:21]
    df['leg_Cbu2'] = df['leg_cbu'].astype(str).str[21]

    # Guardar el DataFrame modificado en un nuevo archivo Excel
    df.to_excel(archivo_salida, index=False)
    print(f"Archivo procesado y guardado en: {archivo_salida}")

except FileNotFoundError:
    print(f"Error: El archivo {archivo_entrada} no fue encontrado.")
except Exception as e:
    print(f"Ocurrió un error: {e}")