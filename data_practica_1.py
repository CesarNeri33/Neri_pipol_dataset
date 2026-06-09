import sqlite3
import pandas as pd

# URL de datos crudos
URL_DATASET = "https://raw.githubusercontent.com/CesarNeri33/Neri_pipol_dataset/main/members.csv"

def cargar_datos():
    print("--- Inicializando Datos ---")
    df = pd.read_csv(URL_DATASET)
    return df

def encontrar_codigo_62(df, columna="phone_number"):
    print("\n--- Punto 1: Busqueda de '+62' ---")
    df[columna] = df[columna].astype(str)
    # Patron RegEx
    patron = r'\+62'
    # Filtramos el DataFrame para ver solo los que cumplen el patron
    resultados = df[df[columna].str.contains(patron, regex=True, na=False)]
    print(f"Se encontraron {len(resultados)} registros con el patron '{patron}'.")
    if not resultados.empty:
        print(resultados[['first_name', columna]].head(5))
    return resultados

def encontrar_corchetes_y_guiones(df, columna="phone_number"):
    print("\n--- Punto 2: Busqueda de corchetes y guiones ---")
    df[columna] = df[columna].astype(str)
    # Patron RegEx
    patron = r'[\[\]\-]'
    # Filtramos el DataFrame para ver solo los que cumplen el patron
    resultados = df[df[columna].str.contains(patron, regex=True, na=False)]
    print(f"Se encontraron {len(resultados)} registros con el patron '{patron}'.")
    if not resultados.empty:
        print(resultados[['first_name', columna]].head(5))
    return resultados

def encontrar_espacios_vacios(df, columna="phone_number"):
    print("\n--- Punto 3: Busqueda de espacios vacios ---")
    df[columna] = df[columna].astype(str)
    # Patron RegEx
    patron = r'\s'
    # Filtramos el DataFrame para ver solo los que cumplen el patron
    resultados = df[df[columna].str.contains(patron, regex=True, na=False)]
    print(f"Se encontraron {len(resultados)} registros con el patron '{patron}'.")
    if not resultados.empty:
        print(resultados[['first_name', columna]].head(5))
    return resultados

if __name__ == "__main__":
    # 1. Cargar datos
    df_miembros = cargar_datos()
    if df_miembros is not None:
        # --- Guardar en SQLite3 ---
        conexion = sqlite3.connect("mlearning.db")
        df_miembros.to_sql("members_exploracion", conexion, if_exists='replace', index=False)
        conexion.close()
        print("Datos cargados en SQLite3 (Tabla: members_exploracion).")
        # 2. Ejecutar las funciones de busqueda
        encontrar_codigo_62(df_miembros)
        encontrar_corchetes_y_guiones(df_miembros)
        encontrar_espacios_vacios(df_miembros)