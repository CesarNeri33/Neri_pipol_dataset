# César Alejandro Neri Orozco
# Ejemplos básicos de uso de Pandas: DataFrames y Series

import pandas as pd

print("===================================")
print("EJEMPLOS DE SERIES EN PANDAS")
print("===================================\n")

# -------------------------
# Ejemplo 1: Crear una Series simple
# -------------------------
print("Ejemplo 1: Series con lista de datos")

edades = pd.Series([20, 25, 30, 22, 28])

print(edades)
print("\nMedia de edades:", edades.mean())

print("\n-----------------------------\n")

# -------------------------
# Ejemplo 2: Series con índices personalizados
# -------------------------
print("Ejemplo 2: Series con índices personalizados")

ventas = pd.Series([100, 150, 200], index=["Enero", "Febrero", "Marzo"])

print(ventas)
print("\nVentas en Febrero:", ventas["Febrero"])

print("\n===================================")
print("EJEMPLOS DE DATAFRAMES EN PANDAS")
print("===================================\n")

# -------------------------
# Ejemplo 1: Crear un DataFrame
# -------------------------
print("Ejemplo 1: DataFrame de estudiantes")

datos_estudiantes = {
    "Nombre": ["Ana", "Luis", "Carlos"],
    "Edad": [23, 25, 22],
    "Carrera": ["Ingeniería", "Arquitectura", "Informática"]
}

df_estudiantes = pd.DataFrame(datos_estudiantes)

print(df_estudiantes)

print("\n-----------------------------\n")

# -------------------------
# Ejemplo 2: Filtrar datos en un DataFrame
# -------------------------
print("Ejemplo 2: Filtrar productos con precio mayor a 1000")

datos_productos = {
    "Producto": ["Laptop", "Mouse", "Teclado", "Monitor"],
    "Precio": [15000, 300, 800, 4000]
}

df_productos = pd.DataFrame(datos_productos)

print("\nTabla original:")
print(df_productos)

productos_caros = df_productos[df_productos["Precio"] > 1000]

print("\nProductos con precio mayor a 1000:")
print(productos_caros)

print("\n===================================")
print("FIN DEL PROGRAMA")
print("===================================")