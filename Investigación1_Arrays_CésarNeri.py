import numpy as np

# =================================================================
# 1. FUNCIÓN np.random
# -----------------------------------------------------------------
# Esta función permite generar números de forma aleatoria. Es muy
# útil para simulaciones, pruebas de algoritmos o inicialización
# de pesos en redes neuronales.
# =================================================================

print("--- 1. Ejemplos de np.random ---")

# Ejemplo A: Generar enteros aleatorios (randint)
# Generamos 5 números enteros entre el 10 y el 50.
enteros_azar = np.random.randint(10, 51, size=5)
print(f"A) Enteros aleatorios (10-50): {enteros_azar}")

# Ejemplo B: Generar números flotantes (rand)
# Genera una matriz de 2x3 con valores aleatorios entre 0 y 1.
matriz_flotantes = np.random.rand(2, 3)
print("B) Matriz de flotantes aleatorios (0-1):")
print(matriz_flotantes)
print("\n")


# =================================================================
# 2. FUNCIÓN np.linspace
# -----------------------------------------------------------------
# Genera una secuencia de números uniformemente espaciados entre 
# dos valores. A diferencia de 'arange', aquí defines cuántos 
# puntos quieres obtener en total.
# =================================================================

print("--- 2. Ejemplos de np.linspace ---")

# Ejemplo A: División equitativa de un rango
# Crea 5 números que dividen el tramo de 0 a 1 de forma exacta.
puntos_equitativos = np.linspace(0, 1, 5)
print(f"A) 5 puntos entre 0 y 1: {puntos_equitativos}")

# Ejemplo B: Preparación de dominio matemático
# Generar 10 valores entre 0 y 100 para ser usados en una gráfica.
eje_x = np.linspace(0, 100, 10)
print(f"B) Dominio de 10 valores (0 a 100): {eje_x}")
print("\n")


# =================================================================
# 3. OPERACIONES MATEMÁTICAS BÁSICAS (Avanzadas en NumPy)
# -----------------------------------------------------------------
# Implementación de funciones vectorizadas para cálculos rápidos 
# sobre arreglos completos.
# =================================================================

print("--- 3. Operaciones Matemáticas ---")

# Arreglo de prueba para las operaciones
datos = np.array([1, 4, 10, 100])
print(f"Arreglo original: {datos}")

# A) Exponenciación (e^x)
# Calcula el número de Euler elevado a cada elemento del arreglo.
exponenciales = np.exp(np.array([1, 2, 3]))
print(f"Exponenciales (e^1, e^2, e^3): {exponenciales}")

# B) Raíz cuadrada (sqrt)
# Obtiene la raíz de cada número en el arreglo 'datos'.
raices = np.sqrt(datos)
print(f"Raíces cuadradas: {raices}")

# C) Logaritmos en varias bases
# Logaritmo Natural (base e)
log_natural = np.log(datos)
# Logaritmo Base 10
log_diez = np.log10(datos)
# Logaritmo Base 2
log_dos = np.log2(datos)

print(f"Logaritmo Natural: {log_natural}")
print(f"Logaritmo Base 10: {log_diez}")
print(f"Logaritmo Base 2:  {log_dos}")