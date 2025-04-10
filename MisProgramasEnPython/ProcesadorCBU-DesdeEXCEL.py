'''
este programa lee un archivo de Excel, asume que una de sus columnas ('leg_cbu') contiene CBUs,
extrae partes específicas de cada CBU basándose en su posición 
(los primeros 3 caracteres, los siguientes 4, etc.), 
crea nuevas columnas en el DataFrame para almacenar estas partes extraídas, 
y finalmente guarda este DataFrame modificado en un nuevo archivo de Excel.
Es importante destacar que este programa asume una estructura específica para los CBUs 
(longitud y posición de los componentes). Si los CBUs en el archivo de entrada no siguen esta estructura, 
la extracción de los datos en las nuevas columnas podría ser incorrecta.
'''


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