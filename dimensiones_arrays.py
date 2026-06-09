# César Alejandro Neri Orozco - 8SM
import numpy as np

# --- 1. Cambiar Dimensiones del Arreglo ---
array_1d = np.arange(9) 
print("Arreglo original (1D):")
print(array_1d)

# Transformar a 2 dimensiones (Matriz de 3x3)
matriz_2d = array_1d.reshape(3, 3)
print("\nArreglo transformado a 2D (3x3):")
print(matriz_2d)

# Regresar el arreglo a su forma original
array_original = matriz_2d.flatten()
print("\nArreglo regresado a su forma original (1D):")
print(array_original)

print("-" * 30)

# --- 2. Concatenación de Arreglos ---

# Creamos dos arreglos de 2x2 para el ejemplo
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Arreglo A:")
print(A)
print("Arreglo B:")
print(B)

# Concatenación Vertical (uno sobre otro)
vertical = np.vstack((A, B))
print("\nConcatenación Vertical (vstack):")
print(vertical)

# Concatenación Horizontal (uno al lado del otro)
horizontal = np.hstack((A, B))
print("\nConcatenación Horizontal (hstack):")
print(horizontal)