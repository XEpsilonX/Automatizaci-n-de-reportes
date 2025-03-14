import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime
from tqdm import tqdm  # Para la barra de progreso en la terminal
import time
import procesamiento

# Función para seleccionar un archivo
def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    root.attributes('-topmost', True)  # Asegura que el diálogo esté por encima
    
    archivo_seleccionado = filedialog.askopenfilename(
        title="Selecciona un archivo",
        filetypes=[("Excel", "*.xlsx"), ("CSV", "*.csv")]
    )
    
    root.destroy()  # Destruye la ventana raíz después de seleccionar
    return archivo_seleccionado

# Función para guardar el DataFrame en un archivo Excel
def guardar_archivo(df):
    if df is None:
        messagebox.showerror("Error", "No hay datos para guardar.")
        return
    
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    root.attributes('-topmost', True)  # Asegura que el diálogo esté por encima
    
    archivo_guardado = filedialog.asksaveasfilename(
        title="Guardar archivo",
        defaultextension=".xlsx",
        filetypes=[("Excel", "*.xlsx")]
    )
    
    if archivo_guardado:
        try:
            # Barra de progreso en la terminal
            with tqdm(total=100, desc="Guardando archivo", unit="%") as pbar:
                df.to_excel(archivo_guardado, index=False)
                for i in range(10):  # Simular progreso
                    time.sleep(0.1)  # Simular un retraso
                    pbar.update(10)  # Actualizar la barra de progreso
            messagebox.showinfo("Éxito", f"Archivo guardado correctamente en {archivo_guardado}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")
    
    root.destroy()  # Destruye la ventana raíz después de guardar

def columnas(op):
    if op == 1:
        col = [
            'cse_prod', 'cve_prod', 'des_sub', 'dessubsub', 'desc_prod',
            'JANUARY_2021','JANUARY_2022','JANUARY_2023','JANUARY_2024','JANUARY_2025','FEBRUARY_2021','FEBRUARY_2022', 
            'FEBRUARY_2023','FEBRUARY_2024','FEBRUARY_2025','MARCH_2021','MARCH_2022','MARCH_2023','MARCH_2024','MARCH_2025', 
            'APRIL_2021','APRIL_2022', 'APRIL_2023','APRIL_2024','APRIL_2025', 'MAY_2021','MAY_2022','MAY_2023','MAY_2024',
            'MAY_2025', 'JUNE_2021','JUNE_2022','JUNE_2023','JUNE_2024','JUNE_2025', 'JULY_2021','JULY_2022','JULY_2023','JULY_2024',
            'JULY_2025', 'AUGUST_2021','AUGUST_2022','AUGUST_2023','AUGUST_2024','AUGUST_2025', 'SEPTEMBER_2021', 'SEPTEMBER_2022', 
            'SEPTEMBER_2023', 'SEPTEMBER_2024','SEPTEMBER_2024', 'OCTOBER_2021','OCTOBER_2022', 'OCTOBER_2023', 'OCTOBER_2024',
            'OCTOBER_2025', 'NOVEMBER_2021', 'NOVEMBER_2022', 'NOVEMBER_2023', 'NOVEMBER_2024', 'NOVEMBER_2025', 'DECEMBER_2021', 
            'DECEMBER_2022', 'DECEMBER_2023', 'DECEMBER_2024', 'DECEMBER_2025', 'des_tial', 'uni_med'
        ]
    elif op == 2:
        col = [
            'cve_cte', 'nom_cte', 'rfc_cte', 'cve_age', 'nom_age','JANUARY_2022', 'FEBRUARY_2022', 'MARCH_2022', 'APRIL_2022', 
            'MAY_2022', 'JUNE_2022', 'JULY_2022', 'AUGUST_2022', 'SEPTEMBER_2022', 'OCTOBER_2022', 'NOVEMBER_2022', 'DECEMBER_2022', 
            'JANUARY_2023', 'FEBRUARY_2023', 'MARCH_2023', 'APRIL_2023', 'MAY_2023','JUNE_2023', 'JULY_2023', 'AUGUST_2023', 
            'SEPTEMBER_2023', 'OCTOBER_2023', 'NOVEMBER_2023', 'DECEMBER_2023', 'JANUARY_2024', 'FEBRUARY_2024', 'MARCH_2024', 
            'APRIL_2024', 'MAY_2024', 'JUNE_2024', 'JULY_2024', 'AUGUST_2024', 'SEPTEMBER_2024', 'OCTOBER_2024', 'NOVEMBER_2024', 
            'DECEMBER_2024', 'JANUARY_2025', 'FEBRUARY_2025', 'MARCH_2025', 'Total' ]

    return col

# Función para mostrar el DataFrame y procesar los datos
def mostrar(direccion, columnas, opcion):
    try:
        # Leer el archivo Excel
        df = pd.read_excel(direccion, usecols=columnas)
        #Filtrar por Divisiones que se manejan
        print("Datos leídos correctamente:")
        # Procesar los datos para agregar nuevas columnas
        df = procesar_datos(df, opcion)
        # Mostrar el DataFrame con las nuevas columnas
        print('Datos procesados')
        print(df.head())
        return df
    except Exception as e:
        print(f'Ocurrio un error verifica tu archivo: {e}')

# Función para procesar los datos y agregar nuevas columnas
def procesar_datos(df,opcion):
    if opcion == 1:
        df = procesamiento.ventas_generales(df)
    elif opcion == 2:
        df = procesamiento.venta_vendedores(df)
    elif opcion == 3:
        df = procesamiento.ventas_clientes(df)
    else:
        print ('Revisa tu documento')
        return df
    
    return df

# Función para la opción 1: Reporte de ventas generales
def opcion_1():
    opcion = 1
    archivo = seleccionar_archivo()
    if archivo:
        columnas = ['falta_fac', 'ventacan', 'cse_prod', 'cve_prod', 'des_sub', 'dessubsub', 'desc_prod', 'des_tial', 'uni_med']
        reporte = mostrar(archivo, columnas, opcion)
        if reporte is not None:
            guardar_archivo(reporte)  # Guardar el archivo procesado

# Función para la opción 2: Reporte de ventas por agentes
def opcion_2():
    archivo = seleccionar_archivo()
    opcion = 2

    if archivo:
        columnas = ['falta_fac', 'ventacan', 'cse_prod', 'cve_prod', 'des_sub', 'dessubsub', 'desc_prod', 'des_tial', 
                    'uni_med', 'nom_age']
        reporte = mostrar(archivo, columnas, opcion)
        

# Función para la opción 3: MRP
def opcion_3():
    opcion = 3
    archivo = seleccionar_archivo()
    if archivo:
        columnas = ['ventamon', 'cve_cte', 'cve_age', 'nom_cte', 'nom_age', 'rfc_cte', 'cse_prod', 'falta_fac']
        reporte = mostrar(archivo,columnas,opcion)
        if reporte is not None:
            guardar_archivo(reporte)

def opcion_4():
    return 

# Función para salir
def salir():
    print('Saliendo del programa...')
    exit()

# Función para mostrar el menú
def mostrar_menu():
    opciones = {
        "1": {'Descripcion': "Reporte Venta Generales", 'Funcion': opcion_1},
        "2": {'Descripcion': "Reporte Venta por Agentes", 'Funcion': opcion_2},
        "3": {'Descripcion': "Reporte por Clientes", 'Funcion': opcion_3},
        "4": {'Descripcion': "MRP", 'Funcion': opcion_4},
        "5": {'Descripcion': "Salir", 'Funcion': salir}
    }

    while True:
        print('\n------ Menú ------')
        for clave, valor in opciones.items():
            print(f"{clave}. {valor['Descripcion']}")

        opcion = input('Elije una opción: ')
        if opcion in opciones:
            opciones[opcion]['Funcion']()
            if opcion == "5":
                break
        else:
            print('Opción no válida. Inténtalo de nuevo.')

# Ejecutar el menú
if __name__ == "__main__":
    mostrar_menu()