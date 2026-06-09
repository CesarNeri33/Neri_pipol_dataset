import numpy as np 

# 1. Crear la matriz
array = np.array([ 
    [0, 1, 2, 3], 
    [4, 5, 6, 7], 
    [8, 9, 10, 11], 
]) 
print("Matriz Original:")
print(array)
print("-" * 20)

# 2. Extraer el elemento "5"
# El 5 está en la fila 1, columna 1 (empezando desde 0)
elemento_5 = array[1, 1]
print(f"Elemento '5': {elemento_5}")

# 3. Extraer la segunda fila
segunda_fila = array[1, :]
print(f"Segunda fila: {segunda_fila}")

# 4. Extraer la tercera columna
# El índice es 2 para la tercera columna
tercera_columna = array[:, 2]
print(f"Tercera columna: {tercera_columna}")

# 5. Submatriz de las 2 columnas centrales
# Columnas con índice 1 y 2 (el stop es exclusivo, por eso usamos 3)
columnas_centrales = array[:, 1:3]
print("Columnas centrales:")
print(columnas_centrales)

print("-" * 20)
# --- Indexación (Mask) ---

# 6. Datos mayores que "3"
mayores_a_3 = array[array > 3]
print(f"Datos mayores que 3: {mayores_a_3}")

# 7. Datos pares
# Usamos el operador módulo % 2 == 0
datos_pares = array[array % 2 == 0]
print(f"Datos pares: {datos_pares}")