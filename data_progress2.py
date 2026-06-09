import pandas as pd
import datetime

# 0. Cargar el dataset desde el link de GitHub
url = "https://raw.githubusercontent.com/CesarNeri33/Neri_pipol_dataset/main/pipol_dataset.csv"
df = pd.read_csv(url)

# 1. Transformar la columna 'birthday' de string a objeto de tipo tiempo
# Se utiliza el comando pd.to_datetime
df['birthday'] = pd.to_datetime(df['birthday'])

# Realizar un print para verificar el cambio de objeto
print("Información del DataFrame tras la conversión:")
print(df.info()) 
print("-" * 30)

# 2. Calcular la edad ('age')
# Se resta el año actual (2026) menos el año de nacimiento  
df['age'] = datetime.datetime.now().year - df['birthday'].dt.year

# Visualizar las primeras filas para verificar la nueva columna
print("Dataset con columna 'age' calculada:")
print(df.head())
print("-" * 30)

# 3. Agrupar por país y extraer la edad promedio
# Se utiliza la función 'groupby' para organizar los datos por 'country'
# Luego se aplica el método .mean() para obtener el promedio de edad
promedio_por_pais = df.groupby('country')['age'].mean()

print("Edad promedio por cada país:")
print(promedio_por_pais)