import pandas as pd
import datetime

# 0. Cargar el dataset desde el link de GitHub
url = "https://raw.githubusercontent.com/CesarNeri33/Neri_pipol_dataset/main/pipol_dataset.csv"
df = pd.read_csv(url)

# --- Calcular la edad ---
# 0.1. Convertir 'birthday' a datetime. Se especifica el formato día/mes/año
df['birthday'] = pd.to_datetime(df['birthday'], format='%d/%m/%Y')

# 0.2. Calcular 'age' restando el año de nacimiento al año actual
año_actual = datetime.datetime.now().year
df['age'] = año_actual - df['birthday'].dt.year
# -------------------------------

# 4. Agrupaciones multinivel
# Creamos la agrupación principal por país y ciudad
agrupacion_multinivel = df.groupby(['country', 'city'])

# a) Agrupar por país y ciudad (México y Dusty City)
mexico_dusty = agrupacion_multinivel.get_group(('Mexico', 'Dusty City'))

print("Personas en el grupo (Mexico, Dusty City):")
print(mexico_dusty)
print("-" * 30)

# b) Agrupar la edad promedio de cada país usando .agg()
promedio_por_pais_agg = df.groupby('country').agg({'age': 'mean'})

print("Edad promedio por pais (usando .agg):")
print(promedio_por_pais_agg)
print("-" * 30)
