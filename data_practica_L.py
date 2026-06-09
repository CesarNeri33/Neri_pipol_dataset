import sqlite3
import pandas as pd

# URL de datos crudos
URL_DATASET = "https://raw.githubusercontent.com/CesarNeri33/Neri_pipol_dataset/main/members.csv"

DB_NAME = "database_cano.db"
TABLA_NAME = "members"

def cargar_datos_github():
    print("--- Fase 1: Extraccion (Extract) ---")
    print(f"Descargando datos desde: {URL_DATASET}")
    try:
        df = pd.read_csv(URL_DATASET)
        print(f"Exito - Se han cargado {len(df)} filas y {len(df.columns)} columnas en el DataFrame.")
        return df
    except Exception as e:
        print(f"Error al extraer los datos: {e}")
        return None

def ejecutar_fase_load(df):
    print(f"\n--- Fase 2: Carga (Load) en SQLite ---")
    print(f"Estableciendo conexion con la base de datos: {DB_NAME}")
    
    try:
        # 1. Crear conexion a SQLite3
        conexion = sqlite3.connect(DB_NAME)
        
        # 2. Cargar el DataFrame en la tabla 'members'
        # if_exists='replace' recrea la tabla si ya existe
        # index=False evita que el indice numerico de Pandas se guarde como columna
        df.to_sql(TABLA_NAME, conexion, if_exists='replace', index=False)
        print(f"¡Datos guardados correctamente en la tabla '{TABLA_NAME}'!")
        
        # 3. Mostrar el esquema de SQL (Schema) utilizando PRAGMA
        print("\n========================================================")
        print(f"         ESQUEMA DE LA TABLA '{TABLA_NAME.upper()}'")
        print("========================================================")
        cursor = conexion.cursor()
        cursor.execute(f"PRAGMA table_info({TABLA_NAME});")
        columnas = cursor.fetchall()
        
        # Estructura devuelta por PRAGMA: (cid, name, type, notnull, dflt_value, pk)
        print(f"{'ID':<4} | {'Nombre de Columna':<20} | {'Tipo de Dato SQL':<16} | {'PK':<4}")
        print("-" * 55)
        for col in columnas:
            print(f"{col[0]:<4} | {col[1]:<20} | {col[2]:<16} | {col[5]:<4}")
            
        # 4. Mostrar la sentencia de creacion SQL completa generada automaticamente
        print("\n--- Sentencia DDL (Para ver los tipos detectados por Pandas) ---")
        cursor.execute(f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{TABLA_NAME}';")
        sentencia_sql = cursor.fetchone()[0]
        print(sentencia_sql)
        print("========================================================\n")
        
        conexion.close()
        print("Conexion a SQLite cerrada.")
        
    except Exception as e:
        print(f"Error durante el proceso de carga en la BD: {e}")

if __name__ == "__main__":
    df_miembros = cargar_datos_github()
    if df_miembros is not None:
        ejecutar_fase_load(df_miembros)