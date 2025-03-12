import pandas as pd
from datetime import datetime
from tqdm import tqdm  # Para la barra de progreso en la terminal
import time
import archivo

def ventas_generales(df):
    # Verificar si las columnas necesarias están presentes
    if ('falta_fac' not in df.columns or 'ventacan' not in df.columns or 'cve_prod' not in df.columns or 'desc_prod' 
        not in df.columns):
        print("El archivo no contiene las columnas necesarias ('falta_fac', 'ventacan', 'cve_prod', 'desc_prod').")
        return df

    # Convertir la columna 'falta_fac' a tipo datetime
    df['falta_fac'] = pd.to_datetime(df['falta_fac'])
    df = df[(df['cse_prod'] == 'ALIANZA') | (df['cse_prod'] == 'PAKET')]

    # Crear nuevas columnas para cada combinación de año y mes
    for year in range(2021, 2026):  # Años de 2021 a 2025
        for month in range(1, 13):  # Meses de 1 (enero) a 12 (diciembre)
            #Nombrar Columna de mes
            col_name = f"{datetime(year, month, 1).strftime('%B_%Y').upper()}"
            
            # Filtrar los datos para el año y mes correspondientes
            filtro = (df['falta_fac'].dt.year == year) & (df['falta_fac'].dt.month == month)
            
            # Sumar las ventas por producto para el mes y año actual
            df[col_name] = df.loc[filtro].groupby('cve_prod')['ventacan'].transform('sum')

    # Agrupar por producto y mantener solo una fila por producto
    df = df.groupby('cve_prod', as_index=False).first()

    # Eliminar columnas innecesarias (como 'falta_fac' y 'ventacan')
    df.drop(columns=['falta_fac', 'ventacan'], inplace=True)

    # Reorganizar las columnas en el orden deseado
    columnas_finales = archivo.columnas(1)

    # Seleccionar solo las columnas que existen en el DataFrame
    columnas_finales = [col for col in columnas_finales if col in df.columns]

    # Reorganizar el DataFrame
    df = df[columnas_finales]

    return df

def venta_vendedores(df):
    vendedores = ['OSCAR RAMIREZ HERNANDEZ', 'ING. JOSE ANTONIO ZUGASTI', 'ARIANA MELCHOR CABRERA']
    
    # Verificar si las columnas necesarias están presentes
    if ('falta_fac' not in df.columns or 'ventacan' not in df.columns or 'cve_prod' not in df.columns or 'desc_prod' 
        not in df.columns):
        print("El archivo no contiene las columnas necesarias ('falta_fac', 'ventacan', 'cve_prod', 'desc_prod').")
        return df
    
    data = df
    for i in vendedores:
        #Filtrar por vendedores
        daf = data[(data['nom_age'] == i)]
        #
        # Convertir la columna 'falta_fac' a tipo datetime
        daf['falta_fac'] = pd.to_datetime(daf['falta_fac'])
        df = df[(df['cse_prod'] == 'ALIANZA') | (df['cse_prod'] == 'PAKET')]

        for year in range(2021, 2026):
            for month in range(1, 13):  # Meses de 1 (enero) a 12 (diciembre)
            #Nombrar Columna de mes
                col_name = f"{datetime(year, month, 1).strftime('%B_%Y').upper()}"
                # Filtrar los datos para el año y mes correspondientes
                filtro = (daf['falta_fac'].dt.year == year) & (daf['falta_fac'].dt.month == month)
                # Sumar las ventas por producto para el mes y año actual
                daf[col_name] = daf.loc[filtro].groupby('cve_prod')['ventacan'].transform('sum')
        #
        # Agrupar por producto y mantener solo una fila por producto
        daf = daf.groupby('cve_prod', as_index=False).first()

        # Eliminar columnas innecesarias (como 'falta_fac' y 'ventacan')
        daf.drop(columns=['falta_fac', 'ventacan', 'nom_age'], inplace=True)

        # Reorganizar las columnas en el orden deseado
        columnas_finales = archivo.columnas(1)

        # Seleccionar solo las columnas que existen en el DataFrame
        columnas_finales = [col for col in columnas_finales if col in daf.columns]

        # Reorganizar el DataFrame
        daf = daf[columnas_finales]
        archivo.guardar_archivo(daf)
        
    return daf

def ventas_clientes(df):
    # Verificar si las columnas necesarias están presentes
   
    
    # Crear nuevas columnas para cada combinación de año y mes
    for year in range(2021, 2026):  # Años de 2021 a 2025
        for month in range(1, 13):  # Meses de 1 (enero) a 12 (diciembre)
            #Nombrar Columna de mes
            col_name = f"{datetime(year, month, 1).strftime('%B_%Y').upper()}"
            
            # Filtrar los datos para el año y mes correspondientes
            filtro = (df['falta_fac'].dt.year == year) & (df['falta_fac'].dt.month == month)
            
            # Sumar las ventas por producto para el mes y año actual
            df[col_name] = df.loc[filtro].groupby('nom_cte')['ventamon'].transform('sum')

    # Agrupar por producto y mantener solo una fila por producto
    df = df.groupby('nom_cte', as_index=False).first()

    # Eliminar columnas innecesarias (como 'falta_fac' y 'ventacan')
    df.drop(columns=['falta_fac', 'ventamon', 'cse_prod'], inplace=True)

    # Reorganizar las columnas en el orden deseado
    columnas_finales = archivo.columnas(2)

    # Seleccionar solo las columnas que existen en el DataFrame
    columnas_finales = [col for col in columnas_finales if col in df.columns]

    # Reorganizar el DataFrame
    df = df[columnas_finales]
    
    return df