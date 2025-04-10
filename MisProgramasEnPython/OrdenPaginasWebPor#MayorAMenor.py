import pandas as pd
import re

def extraer_numero(url):
    """Extrae el número después del '#' de una URL. Devuelve None si no lo encuentra."""
    match = re.search(r'#(\d+)$', url)
    if match:
        return int(match.group(1))
    return None

def ordenar_urls_excel_menor_mayor(archivo_entrada, archivo_salida):
    """
    Lee URLs de un archivo Excel, las ordena por el número después de '#'
    de menor a mayor y guarda el resultado en otro archivo Excel de una sola columna.

    Args:
        archivo_entrada (str): Ruta del archivo Excel de entrada.
        archivo_salida (str): Ruta del archivo Excel de salida.
    """
    try:
        # Leer el archivo Excel. Asumimos que las URLs están en la primera columna (índice 0)
        df = pd.read_excel(archivo_entrada, header=None, names=['URL'])

        # Aplicar la función para extraer el número a cada URL
        df['Numero'] = df['URL'].apply(extraer_numero)

        # Filtrar las URLs que tienen un número para ordenar
        df_con_numero = df.dropna(subset=['Numero']).copy()

        # Ordenar el DataFrame según la columna 'Numero' de menor a mayor
        df_ordenado = df_con_numero.sort_values(by='Numero', ascending=True)

        # Crear un nuevo DataFrame con solo la columna 'URL' ordenada
        df_resultado = df_ordenado[['URL']]

        # Guardar el DataFrame resultante en un nuevo archivo Excel sin encabezado ni índice
        df_resultado.to_excel(archivo_salida, header=False, index=False)

        print(f"Las URLs de '{archivo_entrada}' han sido ordenadas por el número después de '#' (de menor a mayor) y guardadas en '{archivo_salida}'.")

    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__": 
    archivo_entrada_excel = 'D:\\Libro1.xlsx'  # Reemplaza con el nombre de tu archivo de entrada
    archivo_salida_excel = 'D:\\Libro2.xlsx' # Reemplaza con el nombre deseado para el archivo de salida

    ordenar_urls_excel_menor_mayor(archivo_entrada_excel, archivo_salida_excel)