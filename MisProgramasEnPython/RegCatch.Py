import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import winreg
import datetime
import os
import sys  # Importa el módulo sys

class RegCatch:
    def __init__(self, root):
        self.root = root
        self.root.title("RegCatch V1.0") #Titulo de la ventana

        # --- Sección para cambiar el icono en Windows 
        if getattr(sys, 'frozen', False):
            # Si la aplicación está empaquetada como .exe
            ruta_icono = os.path.join(sys._MEIPASS, "Cam.ico")
        else:
            # Si la aplicación se ejecuta como script
            ruta_icono = os.path.join(os.path.expanduser("~"), "Desktop", "Cam.ico")

        try:
            self.root.iconbitmap(ruta_icono)
        except tk.TclError as e:
            print(f"Error al cargar el icono: {e}")
        # --- Fin de la sección de cambio de icono ---

        self.instantanea1_data = None
        self.instantanea2_data = None
        self.filename1 = None
        self.filename2 = None

        # Botones de acción
        frame_botones = ttk.Frame(root)
        frame_botones.pack(pady=10)

        self.boton_instantanea1 = ttk.Button(frame_botones, text="Captura1",
                                                command=lambda: self.tomar_instantanea(1))
        self.boton_instantanea1.pack(side="left", padx=5)

        self.boton_instantanea2 = ttk.Button(frame_botones, text="Captura2",
                                                command=lambda: self.tomar_instantanea(2))
        self.boton_instantanea2.pack(side="left", padx=5)

        self.boton_comparar = ttk.Button(frame_botones, text="Comparar",
                                                command=self.seleccionar_y_comparar, state="normal") # Habilitado por defecto
        self.boton_comparar.pack(side="left", padx=5)

        # Nuevo botón "Adiós"
        self.boton_adios = ttk.Button(frame_botones, text="Adiós", command=self.cerrar_aplicacion)
        self.boton_adios.pack(side="left", padx=5)

    def mostrar_mensaje_guardado(self, filename):
        if filename:
            messagebox.showinfo(
                "Guardado Exitoso",
                f"Su archivo '{os.path.basename(filename)}' se guardó en '{os.path.dirname(filename)}'."
            )

    def tomar_instantanea(self, numero_instantanea):
        instantanea = self.capturar_registro()

        if instantanea:
            now = datetime.datetime.now()
            timestamp_sin_segundos = now.strftime("%Y%m%d_%H%M")
            nombre_base = f"Cambio{numero_instantanea}"

            filetypes = [
                ('Texto plano', '*.txt')
            ]
            filename = filedialog.asksaveasfilename(
                defaultextension=".txt",
                initialfile=f"{nombre_base}_{timestamp_sin_segundos}",
                title=f"Guardar Captura {numero_instantanea}",
                filetypes=filetypes
            )
            if filename:
                self.guardar_instantanea(instantanea, filename)
                self.mostrar_mensaje_guardado(filename)
                if numero_instantanea == 1:
                    self.filename1 = filename
                elif numero_instantanea == 2:
                    self.filename2 = filename

    def guardar_instantanea(self, data, filename):
        self.guardar_instantanea_txt(data, filename)

    def guardar_instantanea_txt(self, data, filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write("--- Captura del Registro ---\n")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"Fecha y Hora: {timestamp}\n\n")
            for (ruta, nombre), (valor, tipo) in sorted(data.items()):
                f.write(f"[{ruta}]\n")
                f.write(f"  \"{nombre}\" = ({self.get_type_name(tipo)}) \"{valor}\"\n\n")

    def capturar_registro(self, hkey_base=winreg.HKEY_LOCAL_MACHINE, path="", datos=None):
        if datos is None:
            datos = {}

        try:
            key = winreg.OpenKeyEx(hkey_base, path)
            info = winreg.QueryInfoKey(key)

            # Capturar valores de la clave actual
            for i in range(info[1]):  # Valores
                try:
                    nombre, valor, tipo = winreg.EnumValue(key, i)
                    datos[(self.ruta_completa(hkey_base, path), nombre)] = (valor, tipo)
                except OSError:
                    pass  # Algunos valores pueden no ser accesibles

            # Recorrer las subclaves
            for i in range(info[0]):  # Subclaves
                subkey_name = winreg.EnumKey(key, i)
                subkey_path = f"{path}\\{subkey_name}" if path else subkey_name
                self.capturar_registro(hkey_base, subkey_path, datos)

            winreg.CloseKey(key)
        except OSError as e:
            print(f"Error al acceder a {self.ruta_completa(hkey_base, path)}: {e}")

        return datos

    def ruta_completa(self, hkey_base, path):
        hkey_str = ""
        if hkey_base == winreg.HKEY_CLASSES_ROOT:
            hkey_str = "HKEY_CLASSES_ROOT"
        elif hkey_base == winreg.HKEY_CURRENT_CONFIG:
            hkey_str = "HKEY_CURRENT_CONFIG"
        elif hkey_base == winreg.HKEY_CURRENT_USER:
            hkey_str = "HKEY_CURRENT_USER"
        elif hkey_base == winreg.HKEY_LOCAL_MACHINE:
            hkey_str = "HKEY_LOCAL_MACHINE"
        elif hkey_base == winreg.HKEY_USERS:
            hkey_str = "HKEY_USERS"
        return f"{hkey_str}\\{path}" if path else hkey_str

    def seleccionar_archivo(self, title):
        filetypes = [
            ('Archivos de Texto', '*.txt')
        ]
        filename = filedialog.askopenfilename(title=title, filetypes=filetypes)
        return filename

    def seleccionar_y_comparar(self):
        filename1 = self.seleccionar_archivo("Seleccionar la primera captura para comparar")
        if not filename1:
            return

        filename2 = self.seleccionar_archivo("Seleccionar la segunda captura para comparar")
        if not filename2:
            return

        data1 = self.cargar_instantanea(filename1)
        data2 = self.cargar_instantanea(filename2)

        if data1 and data2:
            cambios = self.comparar(data1, data2)
            self.mostrar_comparacion(cambios)
        else:
            messagebox.showerror("Error", "No se pudieron cargar los archivos para comparar.")

    def cargar_instantanea(self, filename):
        try:
            if filename.endswith(".txt"):
                return self.cargar_instantanea_txt(filename)
            return None
        except Exception as e:
            print(f"Error al cargar el archivo {filename}: {e}")
            messagebox.showerror("Error al cargar archivo", f"Ocurrió un error al cargar el archivo:\n{e}")
            return None

    def cargar_instantanea_txt(self, filename):
        data = {}
        try:
            with open(filename, "r", encoding="utf-8") as f:
                lines = f.readlines()
                i = 0
                while i < len(lines):
                    if lines[i].startswith("["):
                        ruta = lines[i].strip()[1:-1]
                        i += 1
                        while i < len(lines) and lines[i].strip().startswith("\""):
                            linea_valor = lines[i].strip()
                            partes = linea_valor.split("=")
                            if len(partes) == 2:
                                nombre_con_comillas = partes[0].strip()
                                nombre = nombre_con_comillas.strip().strip('"')
                                valor_tipo_str = partes[1].strip()
                                if valor_tipo_str.startswith("("):
                                    tipo_str_end = valor_tipo_str.find(")")
                                    if tipo_str_end != -1:
                                        tipo_str = valor_tipo_str[1:tipo_str_end].strip()
                                        valor_con_comillas = valor_tipo_str[tipo_str_end + 1:].strip()
                                        # Intentar eliminar comillas solo si existen
                                        if valor_con_comillas.startswith('"') and valor_con_comillas.endswith('"'):
                                            valor = valor_con_comillas[1:-1]
                                        else:
                                            valor = valor_con_comillas
                                        tipo = self.get_reg_type_from_name(tipo_str)
                                        if ruta and nombre:
                                            data[(ruta, nombre)] = (valor, tipo)
                            i += 1
                    else:
                        i += 1
        except Exception as e:
            print(f"Error al leer archivo TXT {filename}: {e}")
        return data

    def get_reg_type_from_name(self, type_name):
        if type_name == "String":
            return winreg.REG_SZ
        elif type_name == "DWORD":
            return winreg.REG_DWORD
        elif type_name == "Binary":
            return winreg.REG_BINARY
        elif type_name == "Multi-String":
            return winreg.REG_MULTI_SZ
        elif type_name == "Expandable String":
            return winreg.REG_EXPAND_SZ
        elif type_name == "QWORD":
            return winreg.REG_QWORD
        try:
            return int(type_name) # Try to convert if it's a raw integer value
        except ValueError:
            return None

    def comparar(self, antes, despues):
        cambios = {"agregado": {}, "eliminado": {}, "modificado": {}}

        # Buscar claves/valores agregados y modificados
        for (ruta, nombre), (valor_despues, tipo_despues) in despues.items():
            if (ruta, nombre) not in antes:
                cambios["agregado"][(ruta, nombre)] = (None, None, valor_despues, tipo_despues)
            elif (ruta, nombre) in antes:
                valor_antes, tipo_antes = antes[(ruta, nombre)]
                if valor_antes != valor_despues or tipo_antes != tipo_despues:
                    cambios["modificado"][(ruta, nombre)] = (valor_antes, tipo_antes, valor_despues, tipo_despues)

        # Buscar claves/valores eliminados
        for (ruta, nombre), (valor_antes, tipo_antes) in antes.items():
            if (ruta, nombre) not in despues:
                cambios["eliminado"][(ruta, nombre)] = (valor_antes, tipo_antes, None, None)

        return cambios

    def mostrar_comparacion(self, cambios):
        top = tk.Toplevel(self.root)
        top.title("Comparación de Capturas")
        text_area = tk.Text(top, wrap="word")
        scrollbar = ttk.Scrollbar(top, command=text_area.yview)
        text_area.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        text_area.pack(fill="both", expand=True, padx=10, pady=10)

        text_area.insert(tk.END, "--- Cambios en el Registro ---\n\n")
        for tipo, detalles in cambios.items():
            text_area.insert(tk.END, f"{tipo.upper()}:\n")
            for (ruta, nombre), (valor_antes, tipo_antes, valor_despues, tipo_despues) in detalles.items():
                if tipo == "modificado":
                    text_area.insert(tk.END, f"  - [{ruta}, '{nombre}']:\n")
                    text_area.insert(tk.END, f"    - Antes: ({self.get_type_name(tipo_antes)}) '{valor_antes}'\n")
                    text_area.insert(tk.END, f"    - Después: ({self.get_type_name(tipo_despues)}) '{valor_despues}'\n")
                elif tipo == "agregado":
                    text_area.insert(tk.END, f"  + [{ruta}, '{nombre}'] = ({self.get_type_name(tipo_despues)}) '{valor_despues}'\n")
                elif tipo == "eliminado":
                    text_area.insert(tk.END, f"  - [{ruta}, '{nombre}'] (({self.get_type_name(tipo_antes)}) '{valor_antes}')\n")
            text_area.insert(tk.END, "\n")
        text_area.config(state="disabled")

        # Botón de Exportar Informe
        boton_exportar = ttk.Button(top, text="Exportar Informe", command=lambda: self.exportar_informe(text_area.get("1.0", tk.END)))
        boton_exportar.pack(pady=10)

    def exportar_informe(self, informe_texto):
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            initialfile="Informe_Comparacion.txt",
            title="Guardar Informe de Comparación",
            filetypes=[('Archivo de texto', '*.txt'), ('Todos los archivos', '*.*')]
        )
        if filename:
            try:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(informe_texto)
                messagebox.showinfo("Exportar Informe", f"El informe se ha guardado en:\n{filename}")
            except Exception as e:
                messagebox.showerror("Error al Exportar", f"Ocurrió un error al guardar el informe:\n{e}")

    def get_type_name(self, reg_type):
        if reg_type == winreg.REG_SZ:
            return "String"
        elif reg_type == winreg.REG_DWORD:
            return "DWORD"
        elif reg_type == winreg.REG_BINARY:
            return "Binary"
        elif reg_type == winreg.REG_MULTI_SZ:
            return "Multi-String"
        elif reg_type == winreg.REG_EXPAND_SZ:
            return "Expandable String"
        elif reg_type == winreg.REG_QWORD:
            return "QWORD"
        return str(reg_type)

    def cerrar_aplicacion(self):
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = RegCatch(root)
    root.mainloop()