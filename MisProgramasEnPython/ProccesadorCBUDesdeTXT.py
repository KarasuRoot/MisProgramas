'''
lee una lista de CBUs desde un archivo de texto, 
intenta validar su formato, extrae información relevante (códigos de banco, sucursal, cuenta, dígitos verificadores) 
y luego escribe esta información, junto con el CBU original, en un archivo de Excel. 
Los CBUs que no coinciden con el formato esperado son omitidos y se muestra una advertencia.'''
import openpyxl
import re

archivo_txt = 'D:\\cbus.txt'  # Hay que reemplazar donde esta el TXT con los CBU
archivo_excel = 'D:\\cbus.xlsx'

try:
    with open(archivo_txt, 'r') as archivo:
        cbus = [linea.strip() for linea in archivo]
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{archivo_txt}'.")
    exit()

libro_excel = openpyxl.Workbook()
hoja = libro_excel.active

# Escribir encabezados
encabezados = ['bco_codigo', 'bco_sucursal', 'leg_ctaban', 'leg_CBU1', 'leg_cbu2', 'leg_CBU']
hoja.append(encabezados)

for cbu in cbus:
    resultado = re.match(r'(\d{3})(\d{4})(\d{13})(\d)(\d)', cbu)
    if resultado:
        bco_codigo, bco_sucursal, leg_ctaban, leg_CBU1, leg_cbu2 = resultado.groups()
        hoja.append([bco_codigo, bco_sucursal, leg_ctaban, leg_CBU1, leg_cbu2, cbu])
    else:
        print(f"Advertencia: CBU inválido '{cbu}'. Se omitirá.")

libro_excel.save(archivo_excel)
print(f"Se ha guardado el archivo Excel: '{archivo_excel}'")