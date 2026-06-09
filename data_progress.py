import pandas as pd
import numpy as np
    #César Neri
def identificar_hallazgos(df):
    """Muestra un resumen de los errores detectados antes de la limpieza."""
    print("--- IDENTIFICACIÓN DE HALLAZGOS (DATOS ORIGINALES) ---")
    print(f"1. Valores nulos por columna:\n{df.isnull().sum()}")
    
    # Revisión de datos categóricos
    print(f"\n2. Categorías únicas en Educación: {set(df['Nivel_Educación'])}")
    
    # Revisión de valores fuera de lógica
    print(f"\n3. Edad máxima detectada: {df['Edad'].max()} (Posible Outlier)")
    print(f"4. Registros con ingresos negativos: {len(df[df['Ingresos'] < 0])}")
    print(f"5. Registros con hijos negativos: {len(df[df['Hijos'] < 0])}")
    print("-" * 50 + "\n")

def limpiar_datos(url_github):
    """Carga los datos desde GitHub y aplica las funciones de limpieza."""
    # El parámetro index_col=0 elimina la columna 'Unnamed'
    df = pd.read_csv(url_github, index_col=0)
    
    # Identificación previa de errores
    identificar_hallazgos(df)
    
    # 1. Renombrar columnas al inglés (según apoyo1.txt)
    df.columns = ["age", "sex", "income", "height", "city", "education", "children"]
    
    # 2. Corregir columna 'children' (Hijos)
    # Reemplazar negativos por 0 usando apply y lambda
    df['children'] = df['children'].apply(lambda x: 0 if x < 0 else x)
    
    # 3. Corregir columna 'income' (Ingresos)
    # Convertir negativos a positivos (valor absoluto)
    df['income'] = df['income'].abs()
    
    # 4. Corregir columna 'age' (Edad)
    # Sustituir Outliers (>110) y negativos por la media de edades válidas
    media_valida = df[(df['age'] > 0) & (df['age'] <= 110)]['age'].mean()
    df['age'] = df['age'].apply(lambda x: int(media_valida) if x < 0 or x > 110 else x)
    
    # 5. Estandarizar 'education' (Ortografía) y tratar nulos
    def corregir_texto(txt):
        if pd.isna(txt) or txt == "None":
            return "Unknown"
        txt = str(txt).strip().lower()
        if "mastre" in txt:
            return "Master"
        if "bachelor" in txt:
            return "Bachelor"
        return txt.capitalize()
    
    df['education'] = df['education'].apply(corregir_texto)
    
    # 6. Rellenar nulos restantes en Sexo y Ciudad
    df['sex'] = df['sex'].fillna("Unknown")
    df['city'] = df['city'].fillna("Unknown")
    
    return df

if __name__ == "__main__":
    # URL RAW del archivo en tu GitHub
    url = "https://raw.githubusercontent.com/CesarNeri33/Neri_pipol_dataset/main/pipol_datos.csv"
    
    try:
        print("Conectando con GitHub para descargar el dataset...\n")
        df_limpio = limpiar_datos(url)
        
        # Mostrar resumen final
        print("--- RESULTADOS TRAS LA LIMPIEZA ---")
        print(f"¿Existen valores nulos?: {df_limpio.isnull().values.any()}")
        print(f"Categorías de educación normalizadas: {set(df_limpio['education'])}")
        print(f"Edad máxima corregida: {df_limpio['age'].max()}")
        print("\nVista previa de los datos limpios:")
        print(df_limpio.head())
        
        # Guardar localmente el resultado final
        df_limpio.to_csv('pipol_datos_limpios.csv')
        print(f"\n[ÉXITO] Archivo 'pipol_datos_limpios.csv' generado correctamente.")
        
    except Exception as e:
        print(f"[ERROR] No se pudo procesar el archivo: {e}")
