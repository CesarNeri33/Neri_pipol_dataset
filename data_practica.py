import sqlite3
import pandas as pd
from datetime import datetime

# URL de tus datos crudos en GitHub
URL_DATASET = "https://raw.githubusercontent.com/CesarNeri33/Neri_pipol_dataset/main/members.csv"

def conectar_y_cargar_sqlite(url_csv, db_name="mlearning.db", tabla_name="members_raw"):
    print("--- Paso 2: Conexión y Carga a SQLite3 ---")
    try:
        df = pd.read_csv(url_csv)
        print(f"Datos descargados con éxito. Registros: {len(df)}")
        conexion = sqlite3.connect(db_name)
        df.to_sql(tabla_name, conexion, if_exists='replace', index=False)
        print(f"Base de datos '{db_name}' guardada correctamente.")
        conexion.close()
        return df
    except Exception as e:
        print(f"Error en Paso 2: {e}")
        return None


def extraer_codigo_postal(df, columna_origen="address", columna_destino="codigo_postal"):
    print("\n--- Paso 3: ETL - Extracción de Código Postal ---")
    df[columna_origen] = df[columna_origen].astype(str)
    # Patrón: busca un grupo de exactamente 5 dígitos consecutivos
    df[columna_destino] = df[columna_origen].str.extract(r'(\d{5})', expand=False)
    print("Columna 'codigo_postal' generada.")
    return df


def formatear_telefono(df, columna_telefono="phone_number"):
    print("\n--- Paso 4: ETL - Limpieza de Teléfono ---")
    df[columna_telefono] = df[columna_telefono].astype(str)
    # Clase de caracteres: detecta cualquiera de estos símbolos y los elimina
    patron_limpieza = r'[\+\(\)\s\-]'
    df[columna_telefono] = df[columna_telefono].str.replace(patron_limpieza, '', regex=True)
    print("Columna 'phone_number' formateada.")
    return df


def formatear_fecha_nacimiento_regex(df, columna_origen="birth_date", columna_destino="fecha_nac_formato"):
    print("\n--- Paso 5 (Función 1): Formato de Nacimiento con RegEx ---")
    # Creamos una copia en texto para manipularla
    df[columna_destino] = df[columna_origen].astype(str)
    # 1. Diccionario de patrones RegEx para convertir texto del mes a número.
    # El (?i) le dice a RegEx que ignore mayúsculas/minúsculas (ej. Jan, jan, JAN).
    meses_regex = {
        r'(?i)jan': '01', r'(?i)feb': '02', r'(?i)mar': '03',
        r'(?i)apr': '04', r'(?i)may': '05', r'(?i)jun': '06',
        r'(?i)jul': '07', r'(?i)aug': '08', r'(?i)sep': '09',
        r'(?i)oct': '10', r'(?i)nov': '11', r'(?i)dec': '12'
    }
    # Aplicar los reemplazos de meses
    for patron, numero in meses_regex.items():
        df[columna_destino] = df[columna_destino].str.replace(patron, numero, regex=True)
    # 2. Reorganizar la fecha a DD/MM/AAAA.
    # Patrón: (2 dígitos para día) (2 dígitos para mes) (2 o 4 dígitos para año)
    patron_grupos = r'(\d{2})[-\s](\d{2})[-\s](\d{2,4})'
    df[columna_destino] = df[columna_destino].str.replace(patron_grupos, r'\1/\2/\3', regex=True)
    # Patrón: Busca una diagonal "/" seguida de exactamente 2 dígitos al final del texto "$"
    df[columna_destino] = df[columna_destino].str.replace(r'/(\d{2})$', r'/19\1', regex=True)
    print(f"Columna '{columna_destino}' formateada exitosamente.")
    return df


def calcular_edad_regex(df, col_nac="fecha_nac_formato", col_reg="register_time", col_destino="edad"):
    print("\n--- Paso 5 (Función 2): Calcular Edad/Años ---")
    # 1. Extraer el año de nacimiento (los últimos 4 dígitos de la cadena limpia)
    # Patrón: (\d{4}) justo al final de la línea $
    df['anio_nac'] = df[col_nac].str.extract(r'(\d{4})$', expand=False).astype(int)
    # 2. Convertir el timestamp a texto y extraer el año de registro
    fecha_reg_str = pd.to_datetime(df[col_reg], unit='s').astype(str)
    # Patrón: ^(\d{4}) busca los 4 dígitos justo al INICIO de la fecha
    df['anio_reg'] = fecha_reg_str.str.extract(r'^(\d{4})', expand=False).astype(int)
    # 3. Calcular la edad
    df[col_destino] = df['anio_reg'] - df['anio_nac']
    # Limpiamos las columnas temporales
    df = df.drop(columns=['anio_nac', 'anio_reg'])
    print(f"Columna '{col_destino}' calculada exitosamente.")
    return df


if __name__ == "__main__":
    # 2. Cargar datos en SQLite3 y memoria
    df_miembros = conectar_y_cargar_sqlite(URL_DATASET)
    
    if df_miembros is not None:
        # 3. Extracción de Código Postal
        df_miembros = extraer_codigo_postal(df_miembros)    
        # 4. Formatear Teléfono
        df_miembros = formatear_telefono(df_miembros)
        # 5. Transformaciones de Fecha y Edad con RegEx
        df_miembros = formatear_fecha_nacimiento_regex(df_miembros)
        df_miembros = calcular_edad_regex(df_miembros)
        # --- Guardar datos limpios en una nueva tabla de SQLite3 (Cierre del proceso ETL) ---
        conexion = sqlite3.connect("mlearning.db")
        df_miembros.to_sql("members_clean", conexion, if_exists='replace', index=False)
        conexion.close()
        print("\n[Éxito] ¡Proceso ETL finalizado! Datos limpios guardados en la tabla 'members_clean'.")
        # --- Impresión de Resultados Finales ---
        print("\n==================== REPORTE DE VISTA PREVIA ====================")
        columnas_finales = ['first_name', 'codigo_postal', 'phone_number', 'fecha_nac_formato', 'edad']
        print(df_miembros[columnas_finales].head(10))