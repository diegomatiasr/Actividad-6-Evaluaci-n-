import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Función para cargar un archivo como un dataframe

def cargar_dataset(archivo):
    import funciones as pd
    # Si se desea agregar un input se coloca:
    # archivo = input("Por favor, ingresa el nombre del archivo: ")
    extension = os.path.splitext(archivo)[1].lower()
# Cargar el archivo según su extensión
    if extension == '.csv':
        df = pd.read_csv(archivo)
        return(df)
    elif extension == '.xlsx':
        df = pd.read_excel(archivo)
        return(df)
    else:
        raise ValueError(f"Este formato no está soportado para esta función: {extension}")
    


def sustitucion_promedio(df):
    import funciones as pd
    cuantitativas = df.select_dtypes(include=['float64', 'int64', 'int'])
    cualitativas = df.select_dtypes(exclude=['float64', 'int64', 'int'])
    
    df_cuantitativas = cuantitativas.copy()
    
    # Sustituir impares numéricas con "99"
    for i, col in enumerate(df_cuantitativas.columns):
        if (i + 1) % 2 == 0: 
            df_cuantitativas[col] = df_cuantitativas[col].fillna(round(df_cuantitativas[col].mean(), 1))
        else:  
            df_cuantitativas[col] = df_cuantitativas[col].fillna(99)
    
    # Sustituir columnas que no sean de tipo numérico con "Este_es_un_valor_nulo"
    df_cualitativas = cualitativas.fillna("Este_es_un_valor_nulo")
    
    # Unimos el dataframe limpio con el dataframe cualitativo
    datos_sin_nulos = pd.concat([df_cuantitativas, df_cualitativas], axis=1)
    
    return datos_sin_nulos


def cuenta_valores_nulos(data1):
    # valores nulos por columna
    valores_nulos_cols = data1.isnull().sum()
    # valores nulos por dataframe
    valores_nulos_df = data1.isnull().sum().sum()

    return("Valores nulos por columna", valores_nulos_cols,
           "Valores nulos por dataframe", valores_nulos_df)
